<template>
    <div class="modal fade" :id="modalId" tabindex="-1" role="dialog" :aria-labelledby="'#'+modalLabelId" aria-hidden="true">
        <div class="modal-dialog modal-lg" role="document">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title" :id="modalLabelId">Examples {{funcName}}</h5>
                    <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                        <span aria-hidden="true">&times;</span>
                    </button>
                </div>
                <div class="modal-body">
                    <examples-carousel :examples="examples" :fileName="fileName" :funcName="funcName"></examples-carousel>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import ExamplesCarousel from './examples-carousel/Examples-carousel.vue';

    export default {
        name: 'examples-modal',
        components: {
            ExamplesCarousel,
        },
        props: {
            examples: {
                type: Array,
                required: true,
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
                modalId: "examples-modal-" + this.fileName + "-" + this.funcName,
                modalLabelId: "examples-modal-label" + this.fileName + "-" + this.funcName,
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