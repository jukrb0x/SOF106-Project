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
          Essential Links
        </q-item-label>

      </q-list>
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

import {defineComponent, ref} from '@vue/composition-api';

export default defineComponent({
  name: 'MainLayout',
  components: {},
  setup() {
    const leftDrawerOpen = ref(false);
    const name = ref('');
    const team_name = ref('');
    name.value = "Digit Recognition";
    team_name.value = "PAI Group 2-11";
    return {leftDrawerOpen, name, team_name}
  }
});
</script>
