<template>
    <div>
        <div v-for="(func, index) in functions" :key="index">
            <h4 class="card-title">{{ func.name }}</h4>
            <div class="form-group">
                <textarea class="form-control" v-model="func.description" readonly></textarea>
            </div>
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