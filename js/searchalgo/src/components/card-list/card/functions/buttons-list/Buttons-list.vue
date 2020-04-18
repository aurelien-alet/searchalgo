<template>
    <div>
        <div v-if="examples && examples.length > 0">
            <button type="button" class="btn btn-primary" data-toggle="modal" :data-target="modalId">
                Examples
            </button>
            <examples-modal :examples="examples" :fileName="fileName" :funcName="funcName"></examples-modal>
        </div>
    </div>
</template>

<script>
    import ExamplesModal from './examples-modal/Examples-modal.vue';

    export default {
        name: 'buttons-list',
        components: {
            ExamplesModal,
        },
        props: {
            examples: {
                type: Array,
                required: false,
            },
            fileName: {
                type: String,
                required: true,
            },
            funcName: {
                type: String,
                required: true,
            },
            
        },
        data() {
            return {
                modalId: "#examples-modal-" + this.fileName + "-" + this.funcName,    
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