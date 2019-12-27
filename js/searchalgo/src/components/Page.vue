<template>
    <div class="padding-sides-1-rem">
        <search></search>
        <card-list :files="files"></card-list>
    </div>
</template>

<script>
    import files from '../../../../data/description.json';
    import Search from './search/Search.vue';
    import CardList from './card-list/Card-list.vue';

    export default {
        name: 'page',
        components: {
            Search,
            CardList,
        },
        props: {
        },
        data() {
            return {
                files: [],
            }
        },
        methods: {
        },
        computed: {

        },
        mounted() {
            console.log(files);
            this.files = files
        }
    }
</script>

<style>
</style>