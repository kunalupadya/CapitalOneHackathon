<template>
    <header class="header-global">
        <base-nav class="navbar-main" transparent :type="solid? 'default': ''" effect="dark" expand>
            <router-link slot="brand" class="navbar-brand mr-lg-5" to="/">
                <img src="img/brand/white.png" alt="logo">
            </router-link>
        </base-nav>
    </header>
</template>
<script>
import BaseNav from "@/components/BaseNav";
import BaseDropdown from "@/components/BaseDropdown";
import CloseButton from "@/components/CloseButton";

export default {
  components: {
    BaseNav,
    CloseButton,
    BaseDropdown
  },
  props: ['solid'],

};
</script>
<style>
  nav .container {
    margin: auto 3%;
  }
</style>
