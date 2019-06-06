<template>
    <div id="app">
        <router-view name="header" ></router-view>
        <router-view ></router-view>
    </div>
</template>
<script>
import { FadeTransition } from "vue2-transitions";

export default {
  components: {
    FadeTransition
  },
  mounted() {
    console.log('app moutned');
  }
};
</script>
