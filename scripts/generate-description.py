#!/bin/sh
"exec" "`dirname $0`/../venv/bin/python" "$0" "$@"

import os
import sys
import json
import types
import inspect
import requests

from tqdm import tqdm
from yandex.Translater import Translater

tryalgo_path = os.path.join("..", "tryalgo")
sys.path.append(tryalgo_path)

def args_error():
    """
        Error messages returned when user passes wrong arguments
    """
    print("""
        Possibles arguments:

            --no-translation : disable doc-strings translation
    """)
    sys.exit()

def get_yandex_key():
    """
        Returns the key for the yandex translation api
        located in keys/yandex.txt
    """
    key_file = os.path.join("..", "keys", "yandex.txt")
    try:
        with open(key_file, "r") as f:
            return f.read()
    except FileNotFoundError:
        print("""
            The yandex translator key was not found.
            Add the yandex key in the following file : key/yandex.txt
            A yandex key can be generated at : https://translate.yandex.com/developers
            Otherwise, you can run the script disabling translation: ./generate-description.py --no-translation 
        """)
        sys.exit()

def translate_to_fr(en_text):
    """
        Translate an english string into a french string

        :param en_text: a string containing an english text
        :return: a string containing a french text
    """
    if en_text is None:
        return None
    tr.set_text(en_text)
    return tr.translate()

def get_methods_description(class_obj, translate=False):
    """
        Get the doc-strings of the methods of a class

        :param class_obj: a python class
        :param translate: a boolean. If translate is true,
            the method names and their doc-sting are translated in french 
        :return: a list containing the doc-strings of the methods
    """
    methods_desc = []
    for method_name in dir(class_obj):

        method = getattr(class_obj, method_name)
        if not isinstance(method, types.FunctionType):
            continue
        method_doc = method.__doc__

        if translate:
            method_name = translate_to_fr(method_name)
            method_doc = translate_to_fr(method_doc)

        methods_desc.append({
            "name": method_name,
            "description": method_doc,
        })

    return methods_desc

def get_classes_description(module, translate=False):
    """
        Get the doc-strings of the classes of a module

        :param class_obj: a python module
        :param translate: a boolean. If translate is true,
            the class names and their doc-sting are translated in french 
        :return: a list containing the doc-strings of the classes
    """
    classes_desc = []
    for class_name in dir(module):

        class_obj = getattr(module, class_name)
        if not inspect.isclass(class_obj):
            continue
        class_module_name = inspect.getmodule(class_obj).__name__
        if class_module_name != module.__name__:
            continue
        class_doc = class_obj.__doc__

        if translate:
            class_name = translate_to_fr(class_name)
            class_doc = translate_to_fr(class_doc)

        classes_desc.append({
            "name": class_name,
            "description": class_doc,
            "methods": get_methods_description(class_obj, translate=translate),
        })

    return classes_desc

def get_functions_description(module, translate=False):
    """
        Get the doc-strings of the functions of a module

        :param class_obj: a python module
        :param translate: a boolean. If translate is true,
            the functions names and their doc-sting are translated in french 
        :return: a list containing the doc-strings of the functions
    """
    fonctions_desc = []
    for function_name in dir(module):

        function = getattr(module, function_name)
        if not isinstance(function, types.FunctionType):
            continue
        function_module_name = inspect.getmodule(function).__name__
        if function_module_name != module.__name__:
            continue
        function_doc = function.__doc__

        if translate:
            function_name = translate_to_fr(function_name)
            function_doc = translate_to_fr(function_doc)

        fonctions_desc.append({
            "name": function_name,
            "description": function_doc,
        })       

    return fonctions_desc

def get_tryalgo_descriptions(translate=False):
    """
        Get all the doc-strings of the functions, classes and methods of the tryalgo module

        :param translate: a boolean. If translate is true, the functions, 
            methods ans classes names and their doc-sting are translated in french 
        :return: a list containing the doccstrings
    """
    tryalgo_path = os.path.join("..", "tryalgo", "tryalgo")

    description_obj = []

    for filename in tqdm(os.listdir(tryalgo_path)):
        if not "." in filename:
            continue
        name, extention = filename.split(".")
        if extention != "py" or name == "__init__":
            continue
        module = __import__(f"tryalgo.{name}", fromlist=[None])
        module_doc = module.__doc__

        new_description_obj = {}
        new_description_obj["EN"] = {}
        new_description_obj["EN"]["name"] = name
        new_description_obj["EN"]["description"] = module_doc
        new_description_obj["EN"]["functions"] = get_functions_description(module)
        new_description_obj["EN"]["classes"] = get_classes_description(module)

        if translate:
            name = translate_to_fr(name)
            module_doc = translate_to_fr(module_doc)

            new_description_obj["FR"] = {}
            new_description_obj["FR"]["name"] = name
            new_description_obj["FR"]["description"] = module_doc
            new_description_obj["FR"]["functions"] = get_functions_description(module, translate=True)
            new_description_obj["FR"]["classes"] = get_classes_description(module, translate=True)

        description_obj.append(new_description_obj)

    return description_obj


def generate_json(translate=False):
    """
        Generates a json from the list return by get_tryalgo_descriptions(),
        and saves it in data/description.json

        :param translate: boolean passed to get_tryalgo_descriptions()
    """
    
    description_obj = get_tryalgo_descriptions(translate=translate)

    description_file = os.path.join("..", "data", "description.json")

    with open(description_file, "w") as f:
        f.write(json.dumps(description_obj))

if __name__ == "__main__":

    if len(sys.argv) > 2:
        args_error()
    if len(sys.argv) == 2:
        if sys.argv[1] != "--no-translation":
            args_error()
        generate_json(translate=False)
    else:

        tr = Translater()
        yandex_key = get_yandex_key()
        tr.set_key(yandex_key)
        tr.set_from_lang('en')
        tr.set_to_lang('fr')   

        generate_json(translate=True)