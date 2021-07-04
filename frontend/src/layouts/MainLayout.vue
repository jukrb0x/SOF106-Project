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

        <div @click="welcomeDialog=true">{{ team_name }}</div>
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
      <essential-link name="Tensorflow" caption="E2E Machine Learning Platform"
                      link=""></essential-link>
      <essential-link name="Keras" caption="Python Deep Learning APIs"
                      link=""></essential-link>
    </q-drawer>

    <q-page-container>
      <router-view/>
      <!--  Welcome Dialog  -->
      <q-dialog v-model="welcomeDialog">
        <q-card>
          <q-toolbar>
            <q-avatar>
              <img src="~assets/XMUM.png">
            </q-avatar>
            <q-toolbar-title><span class="text-weight-bold">SOF106</span> Project</q-toolbar-title>
            <q-btn flat round dense icon="close" v-close-popup/>
          </q-toolbar>
          <q-card-section>
            <div style="max-width: 550px">
              <p class="text-subtitle2">Presented by Group 2-11</p>
              Welcome to the SOF106 PAI Project - <b>Handwritten digit recognition</b>
              <div class="q-pt-sm">
                This is the frontend server deployed on Vercel, due to the <a
                href="http://devcenter.heroku.com/articles/slug-size" target="_blank">slug-size</a> of backend,<br>
                we did not deploy it on a cloud server. You can download the backend source code (Python) and start the
                server on your machine, it will open the port
                <pre style="display: inline">8000</pre>
                by default. Or you can deploy it on a cloud server and put the host address in the settings, which you
                may
                see later.
              </div>
              <div class="q-mt-sm">
                This program currently only supports the single integer digit recognition, the output range is
                <pre style="display: inline">[0,9]</pre>
                .
              </div>
              <div class="q-mt-lg">
                Check our <a :href="githubRepo" target="_blank">
                <q-icon name="fab fa-github"></q-icon>
                Github Repository</a> for more details
              </div>
            </div>
          </q-card-section>
        </q-card>
      </q-dialog>
      <!--  footer  -->
      <q-footer bordered class="bg-white text-black row justify-center q-pa-lg-sm">
        <div class="github-link q-ma-sm">
          <a :href="githubRepo" target="_blank">
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
  components: { EssentialLink },
  mounted() {
    this.leftDrawerOpen = this.drawerOpen()
  },
  methods: {
    drawerOpen() {
      return !Screen.lt.md
    }
  },
  setup() {
    const githubRepo = ref('')
    githubRepo.value = "https://github.com/jukrb0x/SOF106-Project";
    const welcomeDialog = ref(true);
    const leftDrawerOpen = ref(false);
    // computed var is read-only
    // const leftDrawerOpen = computed(() => {
    //     return !Screen.lt.md
    //   });
    const name = ref('');
    const team_name = ref('');
    name.value = "Digit Recognition";
    team_name.value = "PAI Group 2-11";
    return { welcomeDialog, leftDrawerOpen, name, team_name, githubRepo }
  }
});
</script>

<style lang="sass">
a
  text-decoration: none
  color: #4e4c4c

a:hover
  transition: ease 0.2s
  color: #000000

.github-link
  a
    text-decoration: none
    color: #8e8e8e

  a:hover
    transition: ease 0.2s
    color: #1D1D1D


</style>
