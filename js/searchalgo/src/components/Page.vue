<template>
    <div class="padding-sides-1-rem">
        <search :files="files" @filter-files="filterFiles"></search>
        <card-list :files="filteredFiles"></card-list>
    </div>
</template>

<script>

    import * as Fuse from 'fuse.js';

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
                filteredFiles: [],
                fuse: null,
            }
        },
        methods: {
            filterFiles(filter) {
                if (!filter) {
                    this.filteredFiles = this.files;
                } else {
                    console.log(filter);
                    var s = this.fuse.search(filter);
                    console.log(s);
                    this.filteredFiles = s;
                }
            }
        },
        computed: {

        },
        mounted() {
            console.log(files);
            this.files = files;
            this.filteredFiles = files;

            var options = {
                shouldSort: true,
                keys: [
                    'EN.name',
                    'EN.description',
                    'EN.functions.name',
                    'EN.functions.description',
                    'EN.classes.name',
                    'EN.classes.description',
                    'EN.classes.methods.name',
                    'EN.classes.methods.description',
                    'FR.name',
                    'FR.description',
                    'FR.functions.name',
                    'FR.functions.description',
                    'FR.classes.name',
                    'FR.classes.description',
                    'FR.classes.methods.name',
                    'FR.classes.methods.description',
                ],
            }
            this.fuse = new Fuse(this.files, options);
        }
    }
</script>

<style>
</style>