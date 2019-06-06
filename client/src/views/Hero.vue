<template>
    <section class="section-hero section-shaped my-0">
        <div class="shape shape-style-1 shape-primary">
            <span class="span-150"></span>
            <span class="span-50"></span>
            <span class="span-50"></span>
            <span class="span-75"></span>
            <span class="span-100"></span>
            <span class="span-75"></span>
            <span class="span-50"></span>
            <span class="span-100"></span>
            <span class="span-50"></span>
            <span class="span-100"></span>
        </div>
        <div class="container shape-container d-flex ">
            <div class="col px-0">
                <div class="row justify-content-center align-items-center">
                    <div style="width: 60%;">
                      <h1 style="color: white; text-align: center; padding-top: 20px; font-size: 30px" >
                        American healthcare is extremely expensive. Discover cheaper options!
                      </h1>
                    </div>
                </div>
                <search-form></search-form>
            </div>
        </div>

    </section>
</template>
<script>
import searchForm from "./components/SearchForm";

export default {
  components: {
    searchForm
  },
  data() {
    return {

    }
  },


};
</script>

<style>
  .search-form .form-group input, .search-form .submit-container {
    width: 60%;
    margin: 0 auto;
  }
  .section-shaped{
    position: inherit !important;
  }
  .section-shaped .stars-and-coded {
    margin-top: 3rem !important;
  }
</style>
