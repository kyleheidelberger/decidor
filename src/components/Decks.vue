<template>
  <section class="deck">
    <div class="container">
      <button
        id="deckButton"
        v-for="(deck, key) in allDecks"
        :key="`${deck}${key}`"
        class="deckButton"
        @click="sendKey(key)"
        :class="{ hiddenDick: hiddenDeck }"
      >
        <!-- {{ key }} -->
        <img class="deckImage" :src="deck.image" />
        <span>{{deck.title}}</span>
      </button>

      <div v-if="!hiddenSearch" class="searchBar">
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

    <div v-if="!hiddenActivity">
      <ChoiceLogic :choices="allDecks.activityDeck" />
      <!-- <ChoiceLogic :choices='fastFoodDeck'/> -->
    </div>

    <div v-if="!hiddenFoodTypes">
      <ChoiceLogic :choices="allDecks.foodTypesDeck" />
      <!-- <ChoiceLogic :choices='fastFoodDeck'/> -->
    </div>

    <div v-if="!hiddenBusiness">
      <ChoiceLogic :choices="allDecks.yelpRestaurants" />
    </div>

    <div
      v-for="(business, index) in allDecks.yelpRestaurants"
      :key="`${business}${index}`"
      class="yelp-business"
    >
      <!-- <a :href="business.url"> -->
      {{ business.name }}
      <img :src="business.imageURL" class="yelp-business-image" />
      <!-- </a> -->
    </div>
  </section>
</template>

<script>
import ChoiceLogic from "./ChoiceLogic";

import axios from "axios";

const yelpBaseURL =
  "https://cors-anywhere.herokuapp.com/https://api.yelp.com/v3/businesses/search?";
const apiKey =
  "SM6pJx7LlCeKgElTpKU3PgsBDvqZud92PBBhqRBOEunqL9az6MmnAN9GUf4_mjjQva10STsyAlOs6RacEdskjV3qx7X_SjhqtpFVY0G0KzKvDoXcb4s-X2eZHOc5XXYx";

// function buildURL(url, searchingFor, location) {
//   return `${yelpBaseURL}${this.searchingFor}&location=${this.cityName}`;
// }

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
        activityDeck: [],
        foodTypesDeck: [],
        yelpRestaurants: [],
        yelpShops: [],
        yelpArts: [],
        yelpParks: []
      },
      // hiddenCards: true,
      cityName: "",
      searchingFor: "",
      hiddenDeck: false,
      businesses: [],
      hiddenBusiness: true,
      hiddenNetflix: true,
      hiddenFood: true,
      hiddenActivity: true,
      hiddenFoodTypes: true,
      hiddenSearch: true
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
    this.allDecks.netflixDeck.image =
      "https://cdn.vox-cdn.com/thumbor/AwKSiDyDnwy_qoVdLPyoRPUPo00=/39x0:3111x2048/1400x1400/filters:focal(39x0:3111x2048):format(png)/cdn.vox-cdn.com/uploads/chorus_image/image/49901753/netflixlogo.0.0.png";
    this.allDecks.netflixDeck.title = "Netflix Original Shows";
    this.allDecks.fastFoodDeck = [
      "McDonald's",
      "Wendy's",
      "Burger King",
      "Chick-Fil-A",
      "Bojangles",
      "Sonic",
      "Taco Bell",
      "Moe's",
      "Five Guys",
      "Pizza Hut",
      "Domino's"
    ];
    this.allDecks.fastFoodDeck.image =
      "https://youngwomenshealth.org/wp-content/uploads/2014/02/fast-food.jpg";
    this.allDecks.fastFoodDeck.title = "Fast Food Chains";
    this.allDecks.activityDeck = [
      "Play a Sport",
      "Go to the Movies",
      "Go to a Park",
      "Go out to Eat",
      "Read a Book",
      "Go Bowling",
      "Go for a Walk/Hike",
      "Try a New Recipe",
      "Go to the Gym",
      "Ride a Bike",
      "Go Shopping",
      "Start Learning a New Skill",
      "Go out for a Drink",
      "Plan a Vacation",
      "Draw, Color, or Paint",
      "Do Yoga",
      "Play a Board Game"
    ];
    this.allDecks.activityDeck.image =
      "https://blindgossip.com/wp-content/uploads/2018/05/couple-popcorn-movies.jpg";
    this.allDecks.activityDeck.title = "Activities";
    this.allDecks.foodTypesDeck = [
      "American",
      "Chinese",
      "Thai",
      "Italian",
      "Mexican",
      "Japanese",
      "Seafood",
      "Barbecue",
      "Indian",
      "Pizza",
      "Korean",
      "Cuban",
      "Mediterranean",
      "French",
      "Jamaican",
      "Middle Eastern",
      "Steakhouse",
      "Spanish",
      "Pub",
      "German"
    ];
    this.allDecks.foodTypesDeck.image =
      "https://cafedelites.com/wp-content/uploads/2019/01/Chinese-Lemon-Chicken-IMAGE-42-500x500.jpg";
    this.allDecks.foodTypesDeck.title = "Food Types";
    // this.allDecks.businesses = [];
    this.allDecks.yelpRestaurants.image =
      "https://portal.restodata.ca/delice/gallery/images/Square/01_delice-_375-2018-03-21.jpg";
    this.allDecks.yelpRestaurants.title = "Restaurants Near Me";
    this.allDecks.yelpShops.image =
      "https://s3-eu-west-1.amazonaws.com/brussels-images/content/gallery/visit/article/shopping-brussels-2018_sq_640.jpg";
    this.allDecks.yelpShops.title = "Shops Near Me";
    this.allDecks.yelpArts.image =
      "https://wearewingard.com/wp-content/uploads/2018/04/cummermuseum-1920x1080-gallery3-768x768.jpg";
    this.allDecks.yelpArts.title = "Arts & Entertainment Near Me";
    this.allDecks.yelpParks.image =
      "https://www.discoverdurham.com/imager/s3_us-east-1_amazonaws_com/durham-2019/images/Nature-Science/DUKE_GARDENS_BRIDGE_aea8419375870281fb13854150585c99.jpg";
    this.allDecks.yelpParks.title = "Parks Near Me";
  },
  methods: {
    sendKey(key) {
      this.getCardsOnClick(key);
      this.getSearchParam(key);
    },
    getCardsOnClick(key) {
      this.hiddenDeck = true;
      if (key.includes("netflixDeck")) {
        this.hiddenNetflix = false;
      } else if (key.includes("fastFoodDeck")) {
        this.hiddenFood = false;
      } else if (key.includes("activityDeck")) {
        this.hiddenActivity = false;
      } else if (key.includes("foodTypesDeck")) {
        this.hiddenFoodTypes = false;
      } else {
        // console.log("businesses else", this.businesses);
        this.hiddenSearch = false;
      }
    },
    getSearchParam(key) {
      if (key.includes("yelpRestaurants")) {
        this.searchingFor = "categories=food,all";
        console.log(this.searchingFor);
      } else if (key.includes("yelpShops")) {
        this.searchingFor = "categories=shopping,all";
      } else if (key.includes("yelpArts")) {
        this.searchingFor = "categories=arts,all";
      } else if (key.includes("yelpParks")) {
        this.searchingFor = "categories=active,parks";
      }
    },
    buildURL(url, searchingFor, location) {
      return `${yelpBaseURL}${this.searchingFor}&location=${this.cityName}`;
    },
    getBusinesses(key) {
      let apiURL = this.buildURL(yelpBaseURL, this.searchingFor, this.cityName);
      console.log(this.searchingFor);

      // Object.keys(this.allDecks).forEach(async (key) => {
      axios
        .get(apiURL, {
          headers: {
            "Access-Control-Allow-Origin": "*",
            Authorization: `Bearer ${apiKey}`
          }
        })
        .then(response => {
          this.allDecks.businesses = response.data.businesses;
          this.filterBusinesses(this.allDecks.businesses);
        })
        .catch(error => {
          console.log(error);
        });
      // })
    },
    filterBusinesses() {
      this.allDecks.businesses.map(business => {
        let businessName = business.name;
        let businessImageURL = business.image_url;
        let businessRating = business.rating;
        let businessURL = business.url;

        this.allDecks.yelpRestaurants.push({
          name: businessName,
          imageURL: businessImageURL,
          rating: businessRating,
          url: businessURL
        });
        this.allDecks.businesses = [];
        this.hiddenSearch = true;
        return this.allDecks.yelpRestaurants;
      });
      // for (let business of this.allDecks.businesses) {
      // assigns data from fetch businesses to variables:
    }
  }
};
</script>