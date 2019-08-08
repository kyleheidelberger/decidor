<template>
  <section class="deck">
    <h1 v-if="!hiddenNav" class="decks-info">Your decks</h1>

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

    <div v-if="!hiddenActivity">
      <ChoiceLogic :choices="allDecks.activityDeck" />
    </div>

    <div v-if="!hiddenFoodTypes">
      <ChoiceLogic :choices="allDecks.foodTypesDeck" />
    </div>

    <div v-if="!hiddenMilkshakes">
      <ChoiceLogic :choices="allDecks.cookoutMilkshakes" />
    </div>

    <div v-if="!hiddenBusiness">
      <ChoiceLogic :choices="yelpDecks.yelpRestaurants" />
    </div>

    <div v-if="!hiddenFictionBooks">
      <ChoiceLogic :choices="apiDecks.fictionDeck" />
    </div>

    <div v-if="!hiddenNonFictionBooks">
      <ChoiceLogic :choices="apiDecks.nonFictionDeck" />
    </div>

    <transition appear name="bounce">
      <div class="container">
        <h2 v-if="!hiddenNav" class="deckInfo">Starter Decks</h2>
        <button
          id="deckButton"
          v-for="(deck, key) in allDecks"
          :key="`${deck}${key}`"
          class="deckButton"
          @click="sendKey(key)"
          :class="{ hiddenDick: hiddenDeck }"
        >
          <div class="deck-container">
            <h2 class="deckTitle">{{deck.title}}</h2>
            <div class="overlay">
              <img class="deckImage" :src="deck.image" />
            </div>
          </div>
        </button>

        <h2 v-if="!hiddenNav" class="deckInfo2">Local Decks</h2>
        <button
          v-for="(deck, key) in yelpDecks"
          :key="`${deck}${key}`"
          class="deckButton"
          @click="sendKey(key)"
          :class="{ hiddenDick: hiddenDeck }"
        >
          <div class="deck-container">
            <h2 class="deckTitle">{{deck.title}}</h2>
            <div class="overlay">
              <img class="deckImage" :src="deck.image" />
            </div>
          </div>
        </button>

        <h2 v-if="!hiddenNav" class="deckInfo3">API Decks</h2>
        <button
          v-for="(deck, key) in apiDecks"
          :key="`${deck}${key}`"
          class="deckButton"
          @click="sendKey(key)"
          :class="{ hiddenDick: hiddenDeck }"
        >
          <div class="deck-container">
            <h2 class="deckTitle">{{deck.title}}</h2>
            <div class="overlay">
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
import { callbackify } from "util";

const yelpBaseURL =
  "https://cors-anywhere.herokuapp.com/https://api.yelp.com/v3/businesses/search?";
const yelpApiKey =
  "SM6pJx7LlCeKgElTpKU3PgsBDvqZud92PBBhqRBOEunqL9az6MmnAN9GUf4_mjjQva10STsyAlOs6RacEdskjV3qx7X_SjhqtpFVY0G0KzKvDoXcb4s-X2eZHOc5XXYx";
const databaseBaseURL = "https://decidor.herokuapp.com/starterdecks/";

const bookBaseURL = `https://api.nytimes.com/svc/books/v3/lists/current/`;
const nytApiKey = `4QC7YMXjnIWo1dTtGFpj5itZlVDPvbOk`;

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
        cookoutMilkshakes:[],
      },
      yelpDecks: {
        yelpRestaurants: [],
        yelpShops: [],
        yelpArts: [],
        yelpParks: []
      },
      apiDecks: {
        fictionDeck: [],
        nonFictionDeck: []
      },
      database: [],
      // hiddenCards: true,
      cityName: "",
      searchingFor: "",
      book_category: "",
      hiddenDeck: false,
      businesses: [],
      results: [],
      hiddenBusiness: true,
      hiddenNetflix: true,
      hiddenFood: true,
      hiddenActivity: true,
      hiddenFoodTypes: true,
      hiddenFictionBooks: true,
      hiddenNonFictionBooks: true,
      hiddenSearch: true,
      hiddenNav: false,
      hiddenMilkshakes: true,
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

    this.buildLocalApi();
    this.allDecks.netflixDeck = [];
    this.allDecks.netflixDeck.image =
      "https://cdn.vox-cdn.com/thumbor/AwKSiDyDnwy_qoVdLPyoRPUPo00=/39x0:3111x2048/1400x1400/filters:focal(39x0:3111x2048):format(png)/cdn.vox-cdn.com/uploads/chorus_image/image/49901753/netflixlogo.0.0.png";
    this.allDecks.netflixDeck.title = "Netflix Originals";
    this.allDecks.fastFoodDeck = [];
    this.allDecks.fastFoodDeck.image =
      "https://nationaltoday.com/wp-content/uploads/2019/07/national-french-fry-day.jpg";
    this.allDecks.fastFoodDeck.title = "Fast Food Chains";
    this.allDecks.activityDeck = [];
    this.allDecks.activityDeck.image =
      "https://blindgossip.com/wp-content/uploads/2018/05/couple-popcorn-movies.jpg";
    this.allDecks.activityDeck.title = "Activities";
    this.allDecks.foodTypesDeck = [];
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
    this.yelpDecks.yelpArts.title = "Entertainment";
    this.yelpDecks.yelpParks.image =
      "https://www.discoverdurham.com/imager/s3_us-east-1_amazonaws_com/durham-2019/images/Nature-Science/DUKE_GARDENS_BRIDGE_aea8419375870281fb13854150585c99.jpg";
    this.yelpDecks.yelpParks.title = "Parks";
    this.apiDecks.fictionDeck.image =
      "https://decidor.s3.amazonaws.com/books.jpeg";
    this.apiDecks.fictionDeck.title = "NYT Fiction";
    this.apiDecks.nonFictionDeck.image =
      "https://decidor.s3.amazonaws.com/books.jpeg";
    this.apiDecks.nonFictionDeck.title = "NYT Non-Fiction";
    this.allDecks.cookoutMilkshakes.title = "Cookout Milkshakes";
    this.allDecks.cookoutMilkshakes.image = "https://s3.amazonaws.com/secretsaucefiles/photos/images/000/106/478/large/530-350x350.jpg?1485364962";
  },
  methods: {
    sendKey(key) {
      this.getCardsOnClick(key);
      this.getSearchParam(key);
      this.getBookCategory(key);
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
      } else if (key.includes("cookoutMilkshakes")) {
        this.hiddenMilkshakes = false;
      } else if (key.includes("yelp")) {
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
    buildYelpURL(url, searchingFor, location) {
      return `${yelpBaseURL}${this.searchingFor}&location=${this.cityName}`;
    },
    getBusinesses(key) {
      let apiURL = this.buildYelpURL(
        yelpBaseURL,
        this.searchingFor,
        this.cityName
      );

      axios
        .get(apiURL, {
          headers: {
            "Access-Control-Allow-Origin": "*",
            Authorization: `Bearer ${yelpApiKey}`
          }
        })
        .then(response => {
          this.yelpDecks.businesses = response.data.businesses;
          console.log("yelpresults:", this.yelpDecks.businesses);
          this.filterBusinesses(this.yelpDecks.businesses);
          this.hiddenBusiness = false;
        })
        .catch(error => {
          console.log(error);
        });
    },
    filterBusinesses() {
      this.yelpDecks.businesses.map(business => {
        let businessName = business.name;
        let businessImageURL = business.image_url;
        // let businessRating = business.rating;
        let businessURL = business.url;

        this.yelpDecks.yelpRestaurants.push({
          title: businessName,
          card_image: businessImageURL,
          // rating: businessRating,
          url: businessURL
        });
        this.yelpDecks.businesses = [];
        this.hiddenSearch = true;
        return this.yelpDecks.yelpRestaurants;
      });
    },
    getBookCategory(key) {
      if (key.includes("fictionDeck")) {
        this.book_category = "hardcover-fiction";
        this.getFictionBookList(key);
      }
      if (key.includes("nonFictionDeck")) {
        this.book_category = "hardcover-nonfiction";
        this.getNonFictionBookList(key);
      }
    },
    buildBookURL(bookBaseURL, book_category, nytApiKey) {
      return `${bookBaseURL}${this.book_category}.json?api-key=${nytApiKey}`;
    },
    getFictionBookList(key) {
      let bookApiURL = this.buildBookURL(
        bookBaseURL,
        this.book_category,
        nytApiKey
      );

      axios
        .get(bookApiURL)
        .then(response => {
          this.results = response.data.results;
          this.hiddenFictionBooks = false;
          this.filterFictionBooks(this.results);
        })
        .catch(error => {
          console.log(error);
        });
    },
    filterFictionBooks() {
      this.results.books.map(book => {
        let bookTitle = book.title;
        let bookAuthor = book.author;
        let bookDescription = book.description;
        let bookCover = book.book_image;
        let bookURL = book.amazon_product_url;

        this.apiDecks.fictionDeck.push({
          title: bookTitle,
          description: bookDescription,
          card_image: bookCover,
          url: bookURL
        });
        this.results = [];
        return this.apiDecks.fictionDeck;
      });
    },
    getNonFictionBookList(key) {
      let bookApiURL = this.buildBookURL(
        bookBaseURL,
        this.book_category,
        nytApiKey
      );

      axios
        .get(bookApiURL)
        .then(response => {
          this.results = response.data.results;
          this.hiddenNonFictionBooks = false;
          this.filterNonFictionBooks(this.results);
        })
        .catch(error => {
          console.log(error);
        });
    },
    filterNonFictionBooks() {
      this.results.books.map(book => {
        let bookTitle = book.title;
        let bookAuthor = book.author;
        let bookDescription = book.description;
        let bookCover = book.book_image;
        let bookURL = book.amazon_product_url;

        this.apiDecks.nonFictionDeck.push({
          title: bookTitle,
          description: bookDescription,
          card_image: bookCover,
          url: bookURL
        });
        this.results = [];
        return this.apiDecks.nonFictionDeck;
      });
    },
    buildLocalApi() {
      axios.get(databaseBaseURL).then(response => {
        this.database = response.data.results;
        this.makeNetflixDeck(this.database);
        this.makeFastFoodDeck(this.database);
        this.makeActivityDeck(this.database);
        this.makeFoodTypesDeck(this.database);
        this.makeCookoutMilkshakesDeck(this.database);
      });
    },
    makeNetflixDeck() {
      this.database[1].card_set.map(card => {
        let cardTitle = card.title;
        let cardImage = card.card_image;
        let cardDeck = card.deck;
        let cardDescription = card.description;

        this.allDecks.netflixDeck.push({
          title: cardTitle,
          card_image: cardImage,
          description: card.description
        });
        return this.allDecks.netflixDeck;
      });
    },
    makeFastFoodDeck() {
      this.database[0].card_set.map(card => {
        let cardTitle = card.title;
        let cardImage = card.card_image;
        let cardDeck = card.deck;
        let cardDescription = card.description;

        this.allDecks.fastFoodDeck.push({
          title: cardTitle,
          card_image: cardImage,
          description: card.description
        });
        return this.allDecks.fastFoodDeck;
      });
    },
    makeActivityDeck() {
      this.database[3].card_set.map(card => {
        let cardTitle = card.title;
        let cardImage = card.card_image;
        let cardDeck = card.deck;
        let cardDescription = card.description;

        this.allDecks.activityDeck.push({
          title: cardTitle,
          card_image: cardImage,
          description: card.description
        });
        return this.allDecks.activityDeck;
      });
    },
    makeFoodTypesDeck() {
      this.database[4].card_set.map(card => {
        let cardTitle = card.title;
        let cardImage = card.card_image;
        let cardDeck = card.deck;
        let cardDescription = card.description;

        this.allDecks.foodTypesDeck.push({
          title: cardTitle,
          card_image: cardImage,
          description: card.description
        });
        return this.allDecks.foodTypesDeck;
      });
    },
    makeCookoutMilkshakesDeck() {
      this.database[5].card_set.map(card => {
        let cardTitle = card.title;
        let cardImage = card.card_image;
        let cardDeck = card.deck;
        let cardDescription = card.description;

        this.allDecks.cookoutMilkshakes.push({
          title: cardTitle,
          card_image: cardImage,
          description: card.description
        });
        return this.allDecks.cookoutMilkshakes;
      });
    },
  }
};
</script>