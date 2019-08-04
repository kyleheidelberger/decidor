<template>
  <section class="deck">
    <div class="container">
      <button
        id="deckButton"
        v-for="(deck, key) in allDecks"
        :key="`${deck}${key}`"
        class="deckButton"
        @click="getCardsOnClick(key)"
        :class="{ hiddenDick: hiddenDeck }"
      >
        {{ key }}
        <img
          class="netflixLogo"
          src="https://cdn.vox-cdn.com/thumbor/AwKSiDyDnwy_qoVdLPyoRPUPo00=/39x0:3111x2048/1400x1400/filters:focal(39x0:3111x2048):format(png)/cdn.vox-cdn.com/uploads/chorus_image/image/49901753/netflixlogo.0.0.png"
        />
      </button>

      <div v-if="!businesses" class="searchBar">
        <input type="text" v-model.lazy="cityName" v-on:change="getBusinesses" placeholder="City" />
        <button @click="getBusinesses">Get Businesses</button>
        <p>
          Input your current location.
          You are currently looking in: {{ cityName }}
        </p>
      </div>
    </div>

    <div v-if="!hiddenNetflix">
      <!-- <ChoiceLogic 
        v-for='(deck, key) in allDecks'
        :key='`${deck}${key}`'
      :choices='deck'/>-->
      <ChoiceLogic :choices="allDecks.netflixDeck" />
    </div>

    <div v-if="!hiddenFood">
      <ChoiceLogic :choices="allDecks.fastFoodDeck" />
      <!-- <ChoiceLogic :choices='fastFoodDeck'/> -->
    </div>

    <div v-if="!businesses">
      <ChoiceLogic :choices="allDecks.businesses" />
    </div>

    <div v-for="(business, index) in businesses" :key="`${business}${index}`" class="yelp-business">
      <!-- <a :href="business.url"> -->
      {{ business.name }}
      <img :src="business.image_url" class="yelp-business-image" />
      <!-- </a> -->
    </div>
  </section>
</template>

<script>
import ChoiceLogic from "./ChoiceLogic";

import axios from "axios";

const yelpBaseURL =
  "https://cors-anywhere.herokuapp.com/https://api.yelp.com/v3/businesses/search?categories=food,all&location=";
const apiKey =
  "SM6pJx7LlCeKgElTpKU3PgsBDvqZud92PBBhqRBOEunqL9az6MmnAN9GUf4_mjjQva10STsyAlOs6RacEdskjV3qx7X_SjhqtpFVY0G0KzKvDoXcb4s-X2eZHOc5XXYx";

function buildURL(url) {
  return yelpBaseURL + url;
}

export default {
  name: "Decks",
  components: {
    ChoiceLogic
  },
  data: () => {
    return {
      allDecks: {
        netflixDeck: [],
        fastFoodDeck: [],
        businesses: []
      },
      // hiddenCards: true,
      cityName: "",
      hiddenDeck: false,
      businesses: true,
      hiddenNetflix: true,
      hiddenFood: true
    };
  },
  mounted() {
    // this.getBusinesses(this.cityName);
    // Object.keys(this.allDecks).forEach(async (key) => {

    //   console.log(key, this.allDecks[key]);
    // axios.get('api/').then(response => {
    //   app.netflixDeck = response.data.netflixDeck;
    // })
    // axios call to populate
    // try {
    // this.allDecks[key] = await axios.get
    // }
    // });

    this.allDecks.netflixDeck = [
      "Queer Eye",
      "Stranger Things",
      "Bojack Horseman",
      "Orange is the New Black",
      "Unbreakable Kimmy Schmidt",
      "American Vandal",
      "Mindhunter",
      "Russian Doll",
      "Master of None",
      "GLOW",
      "The Umbrella Academy",
      "Big Mouth",
      "Dark",
      "The Crown"
    ];

    this.allDecks.fastFoodDeck = [
      "McDonald's",
      "Wendy's",
      "Burger King",
      "Chick-Fil-A"
    ];
  },
  methods: {
    getCardsOnClick(key) {
      this.hiddenDeck = true;
      if (key.includes("netflixDeck")) {
        this.hiddenNetflix = false;
      } else if (key.includes("fastFoodDeck")) {
        this.hiddenFood = false;
      } else {
        console.log("businesses else", this.businesses);
        this.businesses = false;
      }
    },
    getBusinesses() {
      let apiURL = buildURL(this.cityName);

      // Object.keys(this.allDecks).forEach(async (key) => {
      axios
        .get(apiURL, {
          headers: {
            "Access-Control-Allow-Origin": "*",
            Authorization: `Bearer ${apiKey}`
          }
        })
        .then(response => {
          this.businesses = response.data.businesses;
          console.log("businesses then", this.businesses);
        })
        .catch(error => {
          console.log(error);
        });
      // })
    }
  }
};
</script>