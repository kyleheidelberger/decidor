<template>
  <section class="deck">
  <h1 v-if="!hiddenNav" class='decks-info'>Your decks</h1>
  
      <div v-if="!hiddenSearch" class="searchBar">
        <input type="text" v-model.lazy="cityName" v-on:change="getBusinesses" placeholder="City" />
        <button @click="getBusinesses">Get Businesses</button>
        <p>
          Input your current location.
          You are currently looking in: {{ cityName }}
        </p>
      </div>

      <div v-if="!hiddenNetflix">
        <ChoiceLogic :choices="allDecks.netflixDeck" />
      </div>

      <div v-if="!hiddenFood">
        <ChoiceLogic :choices="allDecks.fastFoodDeck" />
    </div>

    <div v-if="!hiddenActivity">
      <ChoiceLogic :choices="allDecks.activityDeck" />
    </div>

    <div v-if="!hiddenFoodTypes">
      <ChoiceLogic :choices="allDecks.foodTypesDeck" />
    </div>

    <div v-if="!hiddenBusiness">
      <ChoiceLogic :choices="yelpDecks.yelpRestaurants" />
    </div>

    <div
      v-for="(business, index) in yelpDecks.yelpRestaurants"
      :key="`${business}${index}`"
      class='deck-container'>
      <!-- <a :href="business.url" target="_blank">       </a>-->
        <h2 class='deckTitle'>{{ business.name }}</h2>
          <div class='overlay'>
            <img :src="business.imageURL" class="deckImage" />
          </div>
    </div>

  <transition appear
  name="bounce">
    <div class="container">

    <h2 v-if="!hiddenNav" class='deckInfo'>Starter Decks</h2>
      <button
        id="deckButton"
        v-for="(deck, key) in allDecks"
        :key="`${deck}${key}`"
        class="deckButton"
        @click="sendKey(key)"
        :class="{ hiddenDick: hiddenDeck }">
          <div class='deck-container'>
            <h2 class='deckTitle'>{{deck.title}}</h2>
              <div class='overlay'>
                <img class="deckImage" :src="deck.image" />
              </div>
          </div>
      </button>

    <h2 v-if="!hiddenNav" class='deckInfo2'>Local Decks</h2>
      <button
      id="deckButton"
      v-for="(deck, key) in yelpDecks"
      :key="`${deck}${key}`"
      class="deckButton"
      @click="sendKey(key)"
      :class="{ hiddenDick: hiddenDeck }">
        <div class='deck-container'>
          <h2 class='deckTitle'>{{deck.title}}</h2>
            <div class='overlay'>
              <img class="deckImage" :src="deck.image" />
            </div>
      </div>
      </button>
    </div>
    </transition>
  </section>
</template>

<script>
import ChoiceLogic from "./ChoiceLogic";

import axios from "axios";

const yelpBaseURL =
  "https://cors-anywhere.herokuapp.com/https://api.yelp.com/v3/businesses/search?";
const apiKey =
  "SM6pJx7LlCeKgElTpKU3PgsBDvqZud92PBBhqRBOEunqL9az6MmnAN9GUf4_mjjQva10STsyAlOs6RacEdskjV3qx7X_SjhqtpFVY0G0KzKvDoXcb4s-X2eZHOc5XXYx";

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
      },
      yelpDecks: {
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
      hiddenSearch: true,
      hiddenNav: false,
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
      {title: "Queer Eye", card_image: "http://static.tvgcdn.net/feed/1/548/118938548.jpg"},
      {title: "Stranger Things", card_image: "https://images-na.ssl-images-amazon.com/images/I/71OB1IywjLL._SY679_.jpg"},
      // {title: "Bojack Horseman", card_image: "https://i.pinimg.com/originals/91/df/30/91df30f6063a67073293864aba9357a9.jpg"},
      // {title: "Unbreakable Kimmy Schmidt", card_image: "https://m.media-amazon.com/images/M/MV5BMTgyNTQyNjUwN15BMl5BanBnXkFtZTgwNjMwNjUzNzM@._V1_.jpg"},
      // {title: "American Vandal", card_image: "https://static2.showtimes.com/poster/540x800/american-vandal-netflix-119343.jpg"},
      // {title: "Mindhunter", card_image: "https://static.tvgcdn.net/feed/1/2/thumbs/118553002_1197x1596.jpg"},
      {title: "Russian Doll", card_image: "https://m.media-amazon.com/images/M/MV5BYmViMjdhZmQtODIyZi00Mzc4LWFhNTItOTk4NGM1NGU0ZDZjXkEyXkFqcGdeQXVyNjc2NTQzMjU@._V1_.jpg"},
      {title: "Master of None", card_image: "https://ih0.redbubble.net/image.511228335.0654/flat,550x550,075,f.u1.jpg"},
      // {title: "GLOW", card_image: "https://images-na.ssl-images-amazon.com/images/I/71edS3VeIcL._SY679_.jpg"},
      {title: "Big Mouth", card_image: "https://images-na.ssl-images-amazon.com/images/I/81QBTBizRxL._SY679_.jpg"},
      {title: "Dark", card_image: "https://i.pinimg.com/originals/67/5e/bc/675ebc2fd210a8bd5362928a51514960.jpg"},
      // {title:"The Crown", card_image: "https://m.media-amazon.com/images/M/MV5BMjAxOTA2Mjc3MF5BMl5BanBnXkFtZTgwMTMxMzIxNDM@._V1_.jpg"},
      {title:"Orange is the New Black", card_image: "https://m.media-amazon.com/images/M/MV5BYjYyM2FmMmMtZDgyZi00NGU3LWI3NzktODllZDY0YzQyNzgyXkEyXkFqcGdeQXVyMTkxNjUyNQ@@._V1_.jpg"},
      // {title: "Dead to Me", card_image: "https://m.media-amazon.com/images/M/MV5BODkwNmY1MjgtY2ZlNS00MWVmLWEzZTktYmMyNDQzMjlmMGY2XkEyXkFqcGdeQXVyMTkxNjUyNQ@@._V1_.jpg"},
      {title: "Black Mirror", card_image: "https://m.media-amazon.com/images/M/MV5BMjM5MzgzMjM3OF5BMl5BanBnXkFtZTgwMzQ2MzQwNzM@._V1_.jpg"},
      // {title: "The Umbrella Academy", card_image: "https://m.media-amazon.com/images/M/MV5BNTFhOTk1NTgtYWM1ZS00NWI1LTgzYzAtYmE5MjZiMDE0NzlhXkEyXkFqcGdeQXVyMTkxNjUyNQ@@._V1_.jpg"},
      // {title: "Grade & Frankie", card_image: "https://m.media-amazon.com/images/M/MV5BODg0MjIzOTc4MV5BMl5BanBnXkFtZTgwNDE3NTIxNzM@._V1_.jpg"},
      // {title: "Our Planet", card_image: "https://m.media-amazon.com/images/M/MV5BN2I1ZjA5YjQtYmQ0ZS00ZmE1LTk1ZjktNTQ5ODIzY2JiZDdhXkEyXkFqcGdeQXVyNjg2NjQwMDQ@._V1_.jpg"},
      {title: "Sex Education", card_image: "https://m.media-amazon.com/images/M/MV5BOTE0MjQ1NDU3OV5BMl5BanBnXkFtZTgwNTI4MTgwNzM@._V1_.jpg"},
      {title: "Dear White People", card_image: "https://m.media-amazon.com/images/M/MV5BNjQ1OTU3MWUtYTU1Ny00NGFkLTk1MTItMjM4ZWQ4M2IxMTdhXkEyXkFqcGdeQXVyNjg2NjQwMDQ@._V1_.jpg"},
      // {title: "You", card_image: "https://i.pinimg.com/originals/93/bc/eb/93bceb9dc583c4511b9742b182b763aa.jpg"},
      // {title: "Bloodline", card_image: "https://m.media-amazon.com/images/M/MV5BMTU4OTY0MzM1OV5BMl5BanBnXkFtZTgwMjkxMzE0MjI@._V1_.jpg"},
      // {title: "House of Cards", card_image: "https://m.media-amazon.com/images/M/MV5BNmM4ODU1MzItODYyYi00Y2U0LWFjZjItYTRhZWIwOGMyZTRhXkEyXkFqcGdeQXVyNjc2NTQ4Nzk@._V1_.jpg"},
      // {title: "Daredevil", card_image: "https://m.media-amazon.com/images/M/MV5BODcwOTg2MDE3NF5BMl5BanBnXkFtZTgwNTUyNTY1NjM@._V1_.jpg"},
      // {title: "Fuller House", card_image: "https://m.media-amazon.com/images/M/MV5BMjAxMzU5MzA0MF5BMl5BanBnXkFtZTgwODgyOTg1MzI@._V1_.jpg"},
      // {title: "Narcos", card_image: "https://m.media-amazon.com/images/M/MV5BMTcyODAxNzcwNF5BMl5BanBnXkFtZTgwNzM1Mjc1NjM@._V1_.jpg"}
    ];
    this.allDecks.netflixDeck.image =
      "https://cdn.vox-cdn.com/thumbor/AwKSiDyDnwy_qoVdLPyoRPUPo00=/39x0:3111x2048/1400x1400/filters:focal(39x0:3111x2048):format(png)/cdn.vox-cdn.com/uploads/chorus_image/image/49901753/netflixlogo.0.0.png";
    this.allDecks.netflixDeck.title = "Netflix Originals";
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
      "https://nationaltoday.com/wp-content/uploads/2019/07/national-french-fry-day.jpg";
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
      "https://images.britcdn.com/wp-content/uploads/2016/05/raw-vegan-pad-thai-ohsheglows-sq.jpg";
    this.allDecks.foodTypesDeck.title = "Food Types";
    // this.allDecks.businesses = [];
    this.yelpDecks.yelpRestaurants.image =
      "https://portal.restodata.ca/delice/gallery/images/Square/01_delice-_375-2018-03-21.jpg";
    this.yelpDecks.yelpRestaurants.title = "Restaurants";
    this.yelpDecks.yelpShops.image =
      "https://www.bwiairport.com/sites/default/files/styles/square_xsml/public/2017-06/stores.jpg";
    this.yelpDecks.yelpShops.title = "Shops";
    this.yelpDecks.yelpArts.image =
      "https://wearewingard.com/wp-content/uploads/2018/04/cummermuseum-1920x1080-gallery3-768x768.jpg";
    this.yelpDecks.yelpArts.title = "Arts & Entertainment";
    this.yelpDecks.yelpParks.image =
      "https://www.discoverdurham.com/imager/s3_us-east-1_amazonaws_com/durham-2019/images/Nature-Science/DUKE_GARDENS_BRIDGE_aea8419375870281fb13854150585c99.jpg";
    this.yelpDecks.yelpParks.title = "Parks";
  },
  methods: {
    sendKey(key) {
      this.getCardsOnClick(key);
      this.getSearchParam(key);
    },
    getCardsOnClick(key) {
      this.hiddenDeck = true;
      this.hiddenNav = true;
      if (key.includes("netflixDeck")) {
        this.hiddenNetflix = false;
      } else if (key.includes("fastFoodDeck")) {
        this.hiddenFood = false;
      } else if (key.includes("activityDeck")) {
        this.hiddenActivity = false;
      } else if (key.includes("foodTypesDeck")) {
        this.hiddenFoodTypes = false;
      } else {
        this.hiddenSearch = false;
      }
    },
    getSearchParam(key) {
      if (key.includes("yelpRestaurants")) {
        this.searchingFor = "categories=food";
      } else if (key.includes("yelpShops")) {
        this.searchingFor = "categories=shopping,all";
      } else if (key.includes("yelpArts")) {
        this.searchingFor = "categories=arts,aquariums,localflavor";
      } else if (key.includes("yelpParks")) {
        this.searchingFor = "categories=parks,dog_parks,skate_parks";
      }
    },
    buildURL(url, searchingFor, location) {
      return `${yelpBaseURL}${this.searchingFor}&location=${this.cityName}`;
    },
    getBusinesses(key) {
      let apiURL = this.buildURL(yelpBaseURL, this.searchingFor, this.cityName);

      axios
        .get(apiURL, {
          headers: {
            "Access-Control-Allow-Origin": "*",
            Authorization: `Bearer ${apiKey}`
          }
        })
        .then(response => {
          this.yelpDecks.businesses = response.data.businesses;
          this.filterBusinesses(this.yelpDecks.businesses);
        })
        .catch(error => {
          console.log(error);
        });
    },
    filterBusinesses() {
      this.yelpDecks.businesses.map(business => {
        let businessName = business.name;
        let businessImageURL = business.image_url;
        let businessRating = business.rating;
        let businessURL = business.url;

        this.yelpDecks.yelpRestaurants.push({
          name: businessName,
          imageURL: businessImageURL,
          rating: businessRating,
          url: businessURL
        });
        this.yelpDecks.businesses = [];
        this.hiddenSearch = true;
        return this.yelpDecks.yelpRestaurants;
      });
    }
  }
};
</script>