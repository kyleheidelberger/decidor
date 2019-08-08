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

    <div v-if="!hiddenFoodTypes">
      <ChoiceLogic :choices="allDecks.foodTypesDeck" />
    </div>

    <div v-if="!hiddenMilkshakes">
      <ChoiceLogic :choices="allDecks.cookoutMilkshakes" />
    </div>

    <div v-if="!hiddenNetflixFilms">
      <ChoiceLogic :choices="allDecks.netflixFilmsDeck" />
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
        netflixFilmsDeck: [],
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
      hiddenNetflixFilms: true,
    };
  },
  mounted() {
    this.buildLocalApi();
    console.log(this.database)
    this.allDecks.netflixDeck.image = "https://decidor.s3.amazonaws.com/netflix_logo.jpeg";
    this.allDecks.netflixDeck.title = "Netflix Shows";
    this.allDecks.fastFoodDeck.image = "https://decidor.s3.amazonaws.com/national-french-fry-day.jpg";
    this.allDecks.fastFoodDeck.title = "Fast Food Chains";
    this.allDecks.activityDeck.image = "https://decidor.s3.amazonaws.com/couple-popcorn-movies.jpg";
    this.allDecks.activityDeck.title = "Activities";
    this.allDecks.foodTypesDeck.image = "https://decidor.s3.amazonaws.com/foodtypes.jpeg";
    this.allDecks.foodTypesDeck.title = "Food Types";
    this.yelpDecks.yelpRestaurants.image = "https://decidor.s3.amazonaws.com/restaurants.jpeg";
    this.yelpDecks.yelpRestaurants.title = "Restaurants";
    this.yelpDecks.yelpShops.image = "https://decidor.s3.amazonaws.com/shops.jpeg";
    this.yelpDecks.yelpShops.title = "Shops";
    this.yelpDecks.yelpArts.image = "https://decidor.s3.amazonaws.com/arts.jpeg";
    this.yelpDecks.yelpArts.title = "Entertainment";
    this.yelpDecks.yelpParks.image = "https://decidor.s3.amazonaws.com/parks.jpeg";
    this.yelpDecks.yelpParks.title = "Parks";
    this.apiDecks.fictionDeck.image = "https://decidor.s3.amazonaws.com/NYT_yellow_square.png";
    this.apiDecks.fictionDeck.title = "Fiction";
    this.apiDecks.nonFictionDeck.image = "https://decidor.s3.amazonaws.com/NYT_blue_square.png";
    this.apiDecks.nonFictionDeck.title = "Non-Fiction";
    this.allDecks.cookoutMilkshakes.title = "Cookout Milkshakes";
    this.allDecks.cookoutMilkshakes.image = "https://decidor.s3.amazonaws.com/cookoutmilkshake.jpeg";
    this.allDecks.netflixFilmsDeck.title = "Netflix Films";
    this.allDecks.netflixFilmsDeck.image = "https://decidor.s3.amazonaws.com/netflix_logo.jpeg"

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
      } else if (key.includes("netflixFilmsDeck")) {
        this.hiddenNetflixFilms = false;
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
          this.filterBusinesses(this.yelpDecks.businesses);
          this.hiddenBusiness = false;
        })
        .catch(error => {
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
        console.log(this.database);
        this.makeNetflixDeck(this.database);
        this.makeFastFoodDeck(this.database);
        this.makeActivityDeck(this.database);
        this.makeFoodTypesDeck(this.database);
        this.makeCookoutMilkshakesDeck(this.database);
        this.makeNetflixFilmsDeck(this.database)
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
      this.database[5].card_set.map(card => {
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
      this.database[4].card_set.map(card => {
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
    makeNetflixFilmsDeck() {
      this.database[2].card_set.map(card => {
        let cardTitle = card.title;
        let cardImage = card.card_image;
        let cardDeck = card.deck;
        let cardDescription = card.description;

        this.allDecks.netflixFilmsDeck.push({
          title: cardTitle,
          card_image: cardImage,
          description: card.description
        });
        return this.allDecks.netflixFilmsDeck;
      });
    },
  }
};
</script>