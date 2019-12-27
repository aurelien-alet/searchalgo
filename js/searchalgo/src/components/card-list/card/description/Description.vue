<template>
    <div>
        <p class="card-text">{{ description }}</p>
    </div>
</template>

<script>
    export default {
        name: 'description',
        components: {

        },
        props: {
            description: {
                type: String,
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