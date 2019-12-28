<template>
    <div>
        <card v-for="file in files" :key="file.EN.name"
            :name="file.EN.name"
            :description="file.EN.description"
            :functions="file.EN.functions"
            :classes="file.EN.classes"
        ></card>
    </div>
</template>

<script>
    import Card from './card/Card.vue';

    export default {
        name: 'card-list',
        components: {
            Card,
        },
        props: {
            files: {
                type: Array,
                required: true
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