#!/bin/sh
"exec" "`dirname $0`/../venv/bin/python" "$0" "$@"

import os
import sys

tryalgo_path = os.path.join("..", "tryalgo")
tryalgo_tests_path = os.path.join(tryalgo_path, "tests")
sys.path.append(tryalgo_path)
sys.path.append(tryalgo_tests_path)

examples = {}
wait_list = []

def trace_calls_and_returns(frame, event, arg):
    co = frame.f_code
    func_name = co.co_name
    file_path = co.co_filename

    if func_name == 'write':
        # Ignore write() calls from print statements
        return

    if event == 'call':

        if ("tryalgo" not in file_path) or ("tests" in file_path) or ("<" in func_name):
            return

        if "self" in frame.f_code.co_varnames:
            return

        args = []

        for i in range(frame.f_code.co_argcount):
            arg = {}
            arg_name = frame.f_code.co_varnames[i]
            arg["name"] = arg_name
            try:
                arg_value = frame.f_locals[arg_name]
                arg["value"] = repr(arg_value)
                arg["type"] = type(arg_value).__name__
            except Exception:
                pass
            args.append(arg)

        wait_list.append({
            "file_path": file_path,
            "func_name": func_name,
            "args": args,
        })

        return trace_calls_and_returns

    elif event == 'return':
        example = wait_list.pop(-1)
        file_path_pop = example.pop("file_path")
        func_name_pop = example.pop("func_name")
        assert file_path_pop == file_path
        assert func_name_pop == func_name
        example["return"] = {
            "value": repr(arg),
            "type": type(arg).__name__,
        } 
        file_name_full = file_path.split("/")[-1]
        file_name, _ = file_name_full.split(".")
        if not file_name in examples:
            examples[file_name] = {}
        if not func_name in examples[file_name]:
            examples[file_name][func_name] = []

        for arg in example["args"]:
            if len(arg["value"]) > 200:
                return
        if len(examples[file_name][func_name]) < 10\
            and example not in examples[file_name][func_name]:
            examples[file_name][func_name].append(example)

    return

def generate_examples():
    """

    """
    tests = __import__("tests.test_tryalgo", fromlist=[None])
    test_tryalgo = tests.TestTryalgo()
    methods = [ func for func in dir(test_tryalgo) 
        if callable(getattr(test_tryalgo, func)) and "test" in func
    ]
    print(methods)
    sys.settrace(trace_calls_and_returns)
    # test_tryalgo.test_arithm()
    # test_tryalgo.test_manacher()
    for method in methods:
    # for method in ["test_dfs"]:

        # global examples
        # examples = {}

        if method[0] == "_":
            continue

        getattr(test_tryalgo, method)()

    print(examples)
    
    

if __name__ == "__main__":

    generate_examples()
