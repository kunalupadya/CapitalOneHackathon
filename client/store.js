import Vue from 'vue';
import Vuex from 'vuex';
Vue.use(Vuex);

const axios = require('axios');

export default new Vuex.Store({
  state: {
    arr: []
  },
  getters: {
    getAll: state=>{
      return state.arr
    }
  },
  mutations: {
    set(state, data) {
      state.arr = data;
    },
    rid(state) {
      state.arr = [];
    }
  },
  actions: {
      sendData ({getters, commit, state}, data) {
        axios.post('http://3.87.217.70:8000/search/', data.data)
          .then(res=>{
            console.log(res);
            console.log('TESTING');
            commit('set', res.data);
            data.router.push('/results');
            // this.$store.state.arr = res;
            console.log(getters.getAll)
          })
      }

  }
});
