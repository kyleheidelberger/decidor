

<template>
  <section class="buttons-container2" id="choice-logic2">
    <button
      v-for="(option, index) in options"
      :key="`${option}${index}`"
      @click="selectOption(index)"
      class="option-buttons button-style"
      :disabled="validated === true"
      :class="{ finalChoice: onlyChoice }"
    >{{option}}</button>

    <div class="searchBar">
      <input type="text" v-model.lazy="cityName" placeholder="City" />
      <button v-on:click="getBusinesses">Get Businesses</button>
      <p>Input your current location. You are in: {{ cityName }}</p>
    </div>

    <div v-for="business in businesses" :key="`${business}`" class="yelp-business">
      <a :href="business.url">
        {{ business.name }}
        <img :src="business.image_url" class="yelp-business-image" />
      </a>
    </div>
  </section>
</template>


<script>
import axios from "axios";

const yelpBaseURL =
  "https://cors-anywhere.herokuapp.com/https://api.yelp.com/v3/businesses/search?categories=food,all&location=";
const apiKey =
  "SM6pJx7LlCeKgElTpKU3PgsBDvqZud92PBBhqRBOEunqL9az6MmnAN9GUf4_mjjQva10STsyAlOs6RacEdskjV3qx7X_SjhqtpFVY0G0KzKvDoXcb4s-X2eZHOc5XXYx";

function buildURL(url) {
  return yelpBaseURL + url;
}

export default {
  name: "YelpDeck",
  data: () => {
    return {
      onlyChoice: false,
      validated: false,
      options: [],
      currentIndex: 0,
      preferences: [],
      copyChoiceList: [],
      endIndex: 2,
      info: null,
      businesses: [],
      cityName: ""
    };
  },
  mounted() {
    this.getCityName();
    // console.log(this.cityName);
    // this.getBusinesses(this.cityName);
    // axios
    //   .get(
    //     `https://cors-anywhere.herokuapp.com/https://api.yelp.com/v3/businesses/search?categories=food,all&cityName=${this.cityName}`,
    //     {
    //       headers: {
    //         "Access-Control-Allow-Origin": "*",
    //         Authorization: `Bearer SM6pJx7LlCeKgElTpKU3PgsBDvqZud92PBBhqRBOEunqL9az6MmnAN9GUf4_mjjQva10STsyAlOs6RacEdskjV3qx7X_SjhqtpFVY0G0KzKvDoXcb4s-X2eZHOc5XXYx`
    //       }
    //     }
    //   )
    //   .then(response => {
    //     this.businesses = response.data.businesses;
    //   });
  },
  methods: {
    getCityName() {
      console.log(this.cityName);
    },
    getBusinesses(cityName) {
      let apiURL = buildURL(this.cityName);
      axios
        .get(apiURL, {
          headers: {
            "Access-Control-Allow-Origin": "*",
            Authorization: `Bearer ${apiKey}`
          }
        })
        .then(response => {
          this.businesses = response.data.businesses;
        })
        .catch(error => {
          console.log(error);
        });
    }
  },
};
</script>