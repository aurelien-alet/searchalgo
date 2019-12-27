<template>
        <div>
            <div v-for="(cls, index) in classes" :key="index">
                <h4 class="card-title">{{ cls.name }}</h4>
                <p class="card-text">{{ cls.description }}</p>
                <div v-for="(method, m_idx) in cls.methods" :key="m_idx">
                    <h5 class="card-title">{{ method.name }}</h5>
                    <p class="card-text">{{ method.description }}</p>
                </div>
            </div>
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
    
            }
        }
    </script>
    
    <style>
    </style>