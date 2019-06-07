<template>
  <div class="row align-items-center justify-content-around stars-and-coded">
    <div class="container mb-1">
      <form @submit.prevent="submitForm" class="search-form">
        <base-input required placeholder="Medical Procedure"
                    v-model="formData.procedure">
        </base-input>
        <base-input required placeholder="Current Location"
                    v-model="formData.location">
        </base-input>
        <base-input required placeholder="Price Limit" v-model="formData.price">
        </base-input>
        <div class="form-group">
          <flat-picker
            :config="{allowInput: true}"
            class="form-control datepicker"
            v-model="formData.surgeryDate"
          ></flat-picker>
        </div>
        <base-input required placeholder="Your Age" v-model="formData.age">
        </base-input>
        <div class="submit-container">
          <base-button nativeType="submit">Submit</base-button>
        </div>
        <FlowerSpinner
          v-show="loading"
          :animation-duration="2500"
          :size="70"
          style="margin: 0 auto;"
          color="#ff1d5e"
        />
      </form>
    </div>
  </div>
</template>

<script>
  // datepicker
  import flatPicker from "vue-flatpickr-component";
  import "flatpickr/dist/flatpickr.css";
  import key from '../../../config';
  import { FlowerSpinner } from 'epic-spinners';
  // http requests
  const axios = require('axios');
  export default {
    components: {
      flatPicker,
      FlowerSpinner
    },
    async mounted() {
      // this.updateLocation();
    },
    data() {
      return {
        formData: {
          procedure: '',
          location: '',
          price: '',
          age: '',
          surgeryDate: new Date(),
        },
        temp: '',
        loading: false
      }
    },
    methods: {
      submitForm(e) {
        this.loading = true;
        this.$store.dispatch('sendData', {data: this.formData,
          router: this.$router});
        // console.log('submit');

      },
      async updateLocation() {
        if (navigator.geolocation) {
          const tosend = await navigator.geolocation.getCurrentPosition((pos) => {
            axios.get('https://maps.googleapis.com/maps/api/geocode/json?latlng=' + pos.coords.latitude + ','
              + pos.coords.longitude + '&sensor=true&key=' + key.APIKEY)
              .then(res => {
                return res.data.results;
              })
          });

          console.log('READ THIS');
          console.log(tosend)
        } else {
          console.log("Geolocation is not supported by this browser.");
        }
      },
    },
    watch: {
      temp() {
        for (let i = 0; i < this.temp.length; ++i) {
          for (let j = 0; j < this.temp[i].types.length; ++j) {
            if (this.temp[i].types[j] === 'locality') {
              break;
            }
          }
          console.log(i);
          this.formData.location = this.temp[i].formatted_address;
          break;
        }
      }
    }
  }
</script>
