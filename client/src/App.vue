<template>
    <div id="app">
        <router-view name="header" ></router-view>
        <router-view @search="renderTiles(data)"
                     ></router-view>
    </div>
</template>
<script>
import { FadeTransition } from "vue2-transitions";

export default {
  components: {
    FadeTransition
  },
  data() {
    return{
      listData: []
    }
  },

};
</script>

