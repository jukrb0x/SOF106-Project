<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated>
      <q-toolbar>
        <q-btn
          flat
          dense
          round
          icon="menu"
          aria-label="Menu"
          @click="leftDrawerOpen = !leftDrawerOpen"
        />

        <q-toolbar-title>
          {{ name }}
        </q-toolbar-title>

        <div>{{ team_name }}</div>
      </q-toolbar>
    </q-header>

    <q-drawer
      v-model="leftDrawerOpen"
      bordered
      content-class="bg-grey-1"
    >
      <q-list>
        <q-item-label
          header
          class="text-grey-8"
        >
          Group members
        </q-item-label>
        <essential-link caption="SWE1909503" name="Zhang Jinbiao"></essential-link>
        <essential-link caption="SWE1909484" name="Liu Yicen"></essential-link>
        <essential-link caption="DMT1909680" name="Chee Ka Yen"></essential-link>
        <essential-link caption="SWE1909765" name="Teon Wei Jet"></essential-link>
      </q-list>
      <q-item-label
        header
        class="text-grey-8"
      >
        Credits
      </q-item-label>
      <essential-link name="Vue.js" caption="Javascript framework"></essential-link>
      <essential-link name="Quasar Framework" caption="Frontend UI scaffold"></essential-link>
      <essential-link name="Axios.js" caption="Promise based HTTP client"></essential-link>
      <essential-link name="Django Framework" caption="Backend server framework"></essential-link>
      <essential-link name="vue-sign-canvas" caption="The drawing canvas component"
                      link="https://github.com/langyuxiansheng/vue-sign-canvas"></essential-link>
    </q-drawer>

    <q-page-container>
      <router-view/>
      <q-footer bordered class="bg-white text-black row justify-center q-pa-lg-sm">
        <div class="github-link q-ma-sm">
          <a href="https://" target="_blank">
            <q-icon name="fab fa-github"></q-icon>
            Github Repo</a>
        </div>
      </q-footer>
    </q-page-container>
  </q-layout>
</template>

<script lang="ts">

import { Screen } from 'quasar'
import { computed, defineComponent, ref } from '@vue/composition-api';
import EssentialLink from "components/EssentialLink.vue";

export default defineComponent({
  name: 'MainLayout',
  components: {EssentialLink},
  mounted() {
    this.leftDrawerOpen = this.drawerOpen()
  },
  methods: {
    drawerOpen() {
      return !Screen.lt.md
    }
  },
  setup() {
    const leftDrawerOpen = ref(false);
    // computed var is read-only
    // const leftDrawerOpen = computed(() => {
    //     return !Screen.lt.md
    //   });
    const name = ref('');
    const team_name = ref('');
    name.value = "Digit Recognition";
    team_name.value = "PAI Group 2-11";
    return {leftDrawerOpen, name, team_name}
  }
});
</script>

<style lang="sass">
.github-link
  a
    text-decoration: none
    color: #8e8e8e

  a:hover
    transition: ease 0.2s
    color: #1D1D1D


</style>
