<template>
  <div class='results-container'>
    <div class="list-view">
      <card v-for="tileData in listData" class="information-tile" shadow
            gradient="primary">
        <p>
            <span class="operation">
              {{tileData.Description}}
            </span>
          <span class="cost" style="font-weight: bold; font-size: 24px;">
              ${{tileData.Cost}}
            </span>
        </p>
        <p>{{tileData.Location}}</p>
      </card>
    </div>
    <div id="map">
      <GmapMap
        :center="center"
        :zoom="3"
        map-type-id="terrain"
        style="width: 100%; height: calc(100% - 56px)"
      >
        <GmapCluster>
          <GmapMarker
            :key="index"
            v-for="(m, index) in listData"
            :position="m.coords"
            :clickable="true"
            :draggable="true"
            @click="center=m.coords"
          />
        </GmapCluster>
        <gmap-polyline
          v-for="(path, index) in listData"
          :path="[originalCenter, path.coords]"
          :options="{ strokeColor : 'index === 1' ? '#008000' :
                      'red' }"></gmap-polyline>
      </GmapMap>
    </div>
  </div>
</template>

<script>
  import Vue from 'vue';
  import GmapCluster from 'vue2-google-maps/dist/components/cluster' // replace src with dist if you have Babel issues
  Vue.component('GmapCluster', GmapCluster);

  export default {
    data() {
      return {
        listData: [],
        center: {
          lat: 37.5,
          lng: -77.4
        },
        originalCenter: {
          lat: 37.5,
          lng: -77.4
        }
      }
    },
    computed: {
      markers() {
        const arr = this.listData.filter((el) => {
          return el.coords;
        });

      }
    },
    created() {
      console.log(this.$store.getters.getAll);
      this.listData = this.$store.getters.getAll;
      this.$forceUpdate();
      console.log('hello');
    },
  }
</script>

<style>
  .results-container {
    display: flex;
    transform: translateY(50px);
    margin-top: 15px;
    height: 100%;
    width: 100%;
  }

  .list-view {
    width: 40%;
    height: 100vh;
    overflow-y: scroll;
    background-color: #eff1ff;
  }

  #app {
    overflow: hidden;
    height: 100vh;
  }

  .information-tile {
    margin: 4px 0;
    margin-right: 12px;
    -webkit-user-select: none;
    -moz-user-select: none;
    -ms-user-select: none;
    user-select: none;
    margin: 20px;
    border-radius: 24px;
  }

  .information-tile .card-body {
    padding: 20px 18px;
    border-radius: 27px;
    margin: 20px;
  }

  .information-tile p {
    color: white;
    font-size: 14px;
    margin: 0;
  }

  #map {
    display: inline;
    height: 100%;
    width: 100%;
    position: unset !important;
    overflow: unset !important;

  }
</style>
