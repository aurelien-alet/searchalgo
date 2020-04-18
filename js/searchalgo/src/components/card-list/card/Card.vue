<template>
    <div>
        <div class="card mb-3">
            <!-- <div class="card-header row" data-toggle="collapse" :data-target="'#collapse-' + name" aria-expanded="true" aria-controls="'#collapse-' + name"> -->
            <div class="card-header">
                <div class="row">
                    <div class="col-10">
                            <card-tab @select-tab="selectTab"></card-tab>
                    </div>
                    <div class="col-2">
                        <h5 class="float-right padding-sides-1-rem padding-tops-0-5-rem no-margin">
                            {{ name }}.py
                        </h5>
                    </div>
                </div>
            </div>
            <!-- <div class="card-body collapse" :id="'collapse-' + name"> -->
            <div class="card-body">
                <description v-if="selectedTab == 'Description'" :description="description"></description>
                <functions v-if="selectedTab == 'Functions'" :functions="functions" :fileName="name"></functions>
                <classes v-if="selectedTab == 'Classes'" :classes="classes"></classes>
            </div>
        </div>
    </div>
</template>

<script>
    import CardTab from './card-tab/Card-tab.vue';
    import Description from './description/Description.vue';
    import Functions from './functions/Functions.vue';
    import Classes from './classes/Classes.vue';

    export default {
        name: 'card',
        components: {
            CardTab,
            Description,
            Functions,
            Classes,
        },
        props: {
            name: {
                type: String,
                required: true,
            },
            description: {
                type: String,
                required: true,
            },
            functions: {
                type: Array,
                required: true,
            },
            classes: {
                type: Array,
                required: true,
            },
        },
        data() {
            return {
                selectedTab: 'Description',
            }
        },
        methods: {
            selectTab(tab) {
                this.selectedTab = tab;
            },
        },
        computed: {

        }
    }
</script>

<style>
</style>