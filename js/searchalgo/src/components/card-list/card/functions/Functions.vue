<template>
    <div>
        <div v-for="(func, index) in functions" :key="index">
            <h4 class="card-title">{{ func.name }}</h4>
            <p class="card-text">{{ func.description }}</p>
        </div>
    </div>
</template>

<script>
    export default {
        name: 'functions',
        components: {

        },
        props: {
            functions: {
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