<template>
  <q-page class="row items-center justify-evenly">
    <!--    <example-component-->
    <!--      title="Example component"-->
    <!--      active-->
    <!--      :todos="todos"-->
    <!--      :meta="meta"-->
    <!--    ></example-component>-->
    <div>
      <Canvas/>
    </div>
  </q-page>
</template>

<script lang="ts">
import { Todo, Meta } from 'components/models';
import ExampleComponent from 'components/CompositionComponent.vue';
import { defineComponent, ref } from '@vue/composition-api';
import Canvas from "components/Canvas.vue";

export default defineComponent({
  name: 'PageIndex',
  components: {Canvas, ExampleComponent},
  mounted() {
    if (process.env.DEV) {
      console.log('%c You are currently in the development mode.', 'background: #222; color: #bada55');
    }
  },
  setup() {
    const todos = ref<Todo[]>([
      {
        caption: 1,
        content: 'ct1'
      },
      {
        caption: 2,
        content: 'ct2'
      },
      {
        caption: 3,
        content: 'ct3'
      },
      {
        caption: 4,
        content: 'ct4'
      },
      {
        caption: 5,
        content: 'ct5'
      }
    ]);
    const meta = ref<Meta>({
      totalCount: 1200
    });
    return {todos, meta};
  }
});
</script>
