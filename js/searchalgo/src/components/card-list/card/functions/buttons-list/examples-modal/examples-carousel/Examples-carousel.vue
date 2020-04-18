<template>
    <div :id="carouselId" class="carousel slide" data-ride="carousel">
        <ol class="carousel-indicators">
            <li v-for="(example, idx) in examples" :data-target="'#'+carouselId" 
                :data-slide-to="idx" :key="idx" :class="{active: idx === 0}"></li>
        </ol>
        <div class="carousel-inner">
            <div v-for="(example, idx) in examples" :key="idx"
                :class="{'carousel-item': true, active: idx === 0}">
                <h5>Arguments</h5>
                <div v-for="arg in example.args" :key="arg.name" class="form-group">
                    <div class="input-group">
                        <div class="input-group-prepend">
                            <span class="input-group-text min-width-12-ex purple-color bold">
                                {{arg.name}}
                            </span>
                        </div>
                        <input :value="arg.value" class="form-control" disabled>
                        <div class="input-group-append">
                            <span class="input-group-text min-width-12-ex green-color bold">
                                {{arg.type}}
                            </span>
                        </div>
                    </div>
                </div>
                <h5>Return</h5>
                <div class="form-group">
                    <div class="input-group">
                        <input :value="example.return.value" class="form-control" disabled>
                        <div class="input-group-append">
                            <span class="input-group-text min-width-12-ex green-color bold">
                                {{example.return.type}}
                            </span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <a class="carousel-control-prev" :href="'#'+carouselId" role="button" data-slide="prev">
            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        </a>
        <a class="carousel-control-next" :href="'#'+carouselId" role="button" data-slide="next">
            <span class="carousel-control-next-icon" aria-hidden="true"></span>
        </a>
    </div>
</template>

<script>
    export default {
        name: 'examples-carousel',
        components: {

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
                carouselId: "examples-carousel-" + this.fileName + "-" + this.funcName,
            }
        },
        methods: {

        },
        computed: {

        }
    }
</script>

<style>
    .carousel-control-prev-icon,
    .carousel-control-next-icon
    {
        filter: invert(1);
    }

    .carousel-indicators {
        bottom: -20px !important;
    }

    .carousel-indicators li {
        background-color: black !important;
    }

    .carousel-item {
        padding: 0 5em 2em 5em;
    }

    /* .input-group-text {
        min-width: 12ex;
        font-weight: bold !important;
    }

    .input-group-prepend .input-group-text {
        color: purple;
    }

    .input-group-append .input-group-text {
        color: green;
    } */

</style>