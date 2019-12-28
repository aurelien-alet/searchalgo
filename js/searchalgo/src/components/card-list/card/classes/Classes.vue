cl<template>
        <div>
            <ul class="list-group list-group-flush">
                <li class="list-group-item" v-for="(cls, index) in classes" :key="index">
                    <h4 class="card-title">{{ cls.name }}</h4>
                    <div class="form-group">
                        <textarea class="form-control" v-model="cls.description" readonly></textarea>
                    </div>
                    <h4 class="card-title" v-if="cls.methods">Methods:</h4>
                    <div v-for="(method, m_idx) in cls.methods" :key="m_idx">
                        <div class="row padding-sides-5-rem padding-tops-0-5-rem">
                            <div class="col-2">
                                <h5 class="card-title">{{ method.name }}</h5>
                            </div>
                            <div class="col-10">
                                <div v-if="method.description" class="form-group no-margin">
                                    <textarea class="form-control" v-model="method.description" readonly></textarea>
                                </div>
                            </div>
                        </div>
                    </div>
                </li>
            </ul>
        </div>
    </template>
    
    <script>
        export default {
            name: 'classes',
            components: {
    
            },
            props: {
                classes: {
                    type: Array,
                    required: true,
                },
            },
            data() {
                return {
    
                }
            },
            methods: {
    
            },
            computed: {
    
            },
            mounted() {
                this.$el.querySelectorAll('textarea').forEach( function(el) {
                    el.style.height = el.scrollHeight + 2 + "px";
                });
            },
        }
    </script>
    
    <style>
    </style>