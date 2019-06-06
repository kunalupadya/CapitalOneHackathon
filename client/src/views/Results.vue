<template>
  <div class='results-container'>
    <div class="list-view">
      <card class="information-tile" shadow gradient="primary">
        <p>
            <span class="operation">
              {{tileData.operation}}
            </span>
          <span class="cost">
              {{tileData.cost}}
            </span>
        </p>
        <p>{{tileData.city}}</p>
        <p>{{tileData.description}}</p>
      </card>
    </div>
    <div id="map">
      <GmapMap
        :center="center"
        :zoom="2"
        map-type-id="terrain"
        style="width: 100%; height: calc(100% - 56px)"
      >
        <GmapMarker
          :key="index"
          v-for="(m, index) in markers"
          :position="m.position"
          :clickable="true"
          :draggable="true"
          @click="center=m.position"
        />
        <gmap-polyline
                        v-for="path in markers"
                       :path="[originalCenter, path.position]"
                       :options="{ strokeColor:'#008000'}"></gmap-polyline>
      </GmapMap>
    </div>
  </div>
</template>

<script>

  export default {

    data() {
      return {
        tileData: {
          operation: 'Lung Cancer Treatment',
          city: 'London, Texas',
          description: 'This treatment consists of using scissors',
          cost: '$ 140'
        },
        center: {
          lat: 47,
          lng: 70
        },
        originalCenter: {
          lat: 47,
          lng: 70
        },
        markers: [
          {
            position: {
              lat: 10,
              lng: 10
            }
          },
          {
            position: {
              lat: 12,
              lng: 12
            }
          },
          {
            position: {
              lat: 24,
              lng: 24
            }
          }
        ]
      }
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
