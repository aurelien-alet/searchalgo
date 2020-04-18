<template>
    <div>
        <div v-for="(func, index) in functions" :key="index">
            <h4 class="card-title">{{ func.name }}</h4>
            <div class="form-group container">
                <div class="row">
                    <div class="col-11">
                        <textarea class="form-control" v-model="func.description" readonly></textarea>
                    </div>
                    <div class="col-1">
                        <buttons-list :examples="func.examples" :fileName="fileName" :funcName="func.name"></buttons-list>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import ButtonsList from './buttons-list/Buttons-list.vue';

    export default {
        name: 'functions',
        components: {
            ButtonsList,
        },
        props: {
            functions: {
                type: Array,
                required: true,
            },
            fileName: {
                type: String,
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