<template>
    <div>
        <ul class="nav nav-pills card-header-pills">
            <li class="nav-item" v-for="(tab, index) in tabs" :key="index" @click="selectTab(tab)">
                <div class="nav-link cursor-pointer blue-text blue-text-hover" :class="{active: selectedTab === tab}">
                    {{ tab }}
                </div>
            </li> 
        </ul>
    </div>
</template>

<script>
    export default {
        name: 'app',
        components: {

        },
        props: {

        },
        data() {
            return {
                tabs: ['Description', 'Functions', 'Classes'],
                selectedTab: 'Description',
            }
        },
        methods: {
            selectTab(tab) {
                this.selectedTab = tab;
                this.$emit('select-tab', tab);
            },
        },
        computed: {

        }
    }
</script>

<style>
</style>