<template>
    <div class="form-group no-margin">
        <textarea class="form-control" v-model="description" readonly></textarea>
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