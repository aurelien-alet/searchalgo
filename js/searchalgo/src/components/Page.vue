<template>
    <div>
        <div class="card bg-light mb-3" v-for="(file, index) in files" :key="index">
            <div class="card-header">{{ file.EN.name }}.py</div>
            <div class="card-body">
                <!-- <h5 class="card-title">Light card title</h5> -->
                <p class="card-text">{{ file.EN.description }}</p>
            </div>
        </div>
    </div>
</template>

<script>
    import files from '../../../../data/description.json'
    export default {
        name: 'app',
        components: {

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