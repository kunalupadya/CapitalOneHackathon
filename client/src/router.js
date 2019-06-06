import Vue from "vue";
import Router from "vue-router";
import AppHeader from "./layout/AppHeader";
import AppFooter from "./layout/AppFooter";
import Hero from "./views/Hero.vue";
import Results from "./views/Results.vue"
import Components from "./views/Components.vue";

Vue.use(Router);

export default new Router({
  mode: 'history',
  routes: [
    {
      path: "/",
      components: {
        header: AppHeader,
        default: Hero
      }
    },
    {
      path: "/results",
      components: {
        header: AppHeader,
        default: Results
      },
      props: {
        header: {
          solid: true
        }
      }
    },
  ]
});
