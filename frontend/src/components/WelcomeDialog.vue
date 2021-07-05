<template>
  <div>
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
              This is the frontend server deployed on Vercel.
              We did not deploy the backend on a cloud server due to the <a
              href="http://devcenter.heroku.com/articles/slug-size" target="_blank">slug-size</a> limitation. You can
              download the backend source code (Python) and start the
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
  </div>
</template>

<script>
import { ref } from "@vue/composition-api";

export default {
  name: "WelcomeDialog",
  props: {
    // TODO: Use Vuex to ensure the communication between parent and child components
    welcomeDialogState: {
      // useless currently
      type: Boolean,
      default: true
    }
  },
  setup() {
    const welcomeDialog = ref(true)
    const githubRepo = ref('');
    githubRepo.value = "https://github.com/jukrb0x/SOF106-Project";
    return { githubRepo, welcomeDialog }
  }
}
</script>

<style scoped>

</style>
