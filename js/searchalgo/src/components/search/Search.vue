<template>
    <div class="form-group width-30-percent">
        <input class="form-control" @keyup="filterFiles" v-model="filter">
    </div>
</template>

<script>
    export default {
        name: 'app',
        components: {

        },
        props: {
            files: {
                type: Array,
                required: true
            },
        },
        data() {
            return {
                filter: "",
            }
        },
        methods: {
            filterFiles() {
                this.$emit('filter-files', this.filter);
            }
        },
        computed: {

        },
    }
</script>

<style>
</style>