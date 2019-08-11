<template>
  <section class="deck">
    <!-- <h1 v-if="!hiddenNav" class="decks-info">Your decks</h1> -->

    <div v-if="!hiddenSearch" class="searchBar">
      <p class="searchPrompt">Where would you like to find choices?</p>
      <div>
        <input
          class="input"
          type="text"
          v-model.lazy="cityName"
          v-on:change="getBusinesses"
          placeholder=" Address, City, Zip Code, etc..."
        />
        <button class="searchButton" @click="getBusinesses">Get Choices</button>
      </div>
      <img class="orLogo" src="//decidor.s3.amazonaws.com/OR_solid_white.png" />
      <button class="locationButton" @click="getLocation()">Get My Location For Me</button>
    </div>

    <div v-if="!hiddenCustomSearch" class="searchBar">
      <div>
        <p class="searchPrompt">What are you looking for?</p>
        <input
          class="input"
          type="text"
          v-model.lazy="searchTerm"
          v-on:change="getBusinesses"
          placeholder=" Coffee, bookstores, etc..."
        />
      </div>
      <div>
        <p class="searchPrompt">Where would you like to find choices?</p>
        <input
          class="input"
          type="text"
          v-model.lazy="cityName"
          placeholder="Address, City, Zip Code, etc..."
        />
        <button class="searchButton" @click="getBusinesses">Get Choices</button>
      </div>
      <img class="orLogo" src="//decidor.s3.amazonaws.com/OR_solid_white.png" />
      <button class="locationButton" @click="getLocation()">Get My Location For Me</button>
    </div>

    <div v-if="!hiddenMovieSearch" class="searchBar">
      <p class="searchPrompt">Where would you like to find movies?</p>
      <div>
        <input
          class="input"
          type="text"
          v-model.lazy="cityName"
          v-on:change="getCityID()"
          placeholder=" City Name"
        />
        <button class="searchButton" @click="getCityID">Get Choices</button>
      </div>
      <img class="orLogo" src="//decidor.s3.amazonaws.com/OR_solid_white.png" />
      <button class="locationButton" @click="getMovieLocation()">Get My Location For Me</button>
    </div>

    <div v-if="!hiddenNetflix">
      <ChoiceLogic :choices="allDecks.netflixDeck" />
    </div>

    <div v-if="!hiddenNetflixFilms">
      <ChoiceLogic :choices="allDecks.netflixFilmsDeck" />
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

    <div v-if="!hiddenBusiness">
      <ChoiceLogic :choices="allDecks.yelpRestaurants" />
    </div>

    <div v-if="!hiddenFictionBooks">
      <ChoiceLogic :choices="allDecks.fictionDeck" />
    </div>

    <div v-if="!hiddenNonFictionBooks">
      <ChoiceLogic :choices="allDecks.nonFictionDeck" />
    </div>

    <div v-if="!hiddenMovies">
      <ChoiceLogic :choices="allDecks.inTheaters" />
    </div>

    <div id='deckContainer' :class="{hiddenContainer: hiddenContainer}" class="deck-grid">
      <!-- <h2 v-if="!hiddenNav" class="deckInfo">Starter Decks</h2> -->
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
    </div>
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
const databaseBaseURL = "//decidor.herokuapp.com/starterdecks/";

const bookBaseURL = `https://api.nytimes.com/svc/books/v3/lists/current/`;
const nytApiKey = `4QC7YMXjnIWo1dTtGFpj5itZlVDPvbOk`;

const movieBaseURL =
  "https://api.internationalshowtimes.com/v4/movies/?fields=title,slug,poster_image.flat&countries=US&release_date_to=";
const movieApiKey = "LafOf9zLcvERnGpF3IBU85w8txyALDvH";

const movieCityURL =
  "https://api.internationalshowtimes.com/v4/cities/?countries=US&";

export default {
  name: "Decks",
  components: {
    ChoiceLogic
  },
  data: () => {
    return {
      allDecks: {
        inTheaters: [],
        netflixDeck: [],
        netflixFilmsDeck: [],
        yelpArts: [],
        yelpRestaurants: [],
        foodTypesDeck: [],
        fastFoodDeck: [],
        cookoutMilkshakes: [],
        activityDeck: [],
        yelpShops: [],
        yelpParks: [],
        custom: [],
        fictionDeck: [],
        nonFictionDeck: []
      },
      database: [],
      // hiddenCards: true,
      cityName: "",
      searchingFor: "",
      book_category: "",
      searchTerm: "",
      hiddenDeck: false,
      hiddenContainer: false,
      businesses: [],
      results: [],
      movies: [],
      cities: [],
      cityID: "",
      movieLocation: "",
      hiddenBusiness: true,
      hiddenNetflix: true,
      hiddenFood: true,
      hiddenActivity: true,
      hiddenFoodTypes: true,
      hiddenFictionBooks: true,
      hiddenNonFictionBooks: true,
      hiddenSearch: true,
      hiddenCustomSearch: true,
      hiddenMovieSearch: true,
      hiddenNav: false,
      hiddenMilkshakes: true,
      hiddenMovies: true,
      hiddenNetflixFilms: true,
      formattedSearch: "",
      lat: "",
      lon: ""
    };
  },
  mounted() {
    this.buildLocalApi();
    console.log(this.database);
    this.allDecks.netflixDeck.image =
      "//decidor.s3.amazonaws.com/netflix_logo.jpeg";
    this.allDecks.netflixDeck.title = "Netflix Shows";
    this.allDecks.fastFoodDeck.image =
      "//decidor.s3.amazonaws.com/national-french-fry-day.jpg";
    this.allDecks.fastFoodDeck.title = "Fast Food Chains";
    this.allDecks.activityDeck.image =
      "//decidor.s3.amazonaws.com/couple-popcorn-movies.jpg";
    this.allDecks.activityDeck.title = "Date Night";
    this.allDecks.foodTypesDeck.image =
      "//decidor.s3.amazonaws.com/foodtypes.jpeg";
    this.allDecks.foodTypesDeck.title = "Types of Cuisine";
    this.allDecks.yelpRestaurants.image =
      "//decidor.s3.amazonaws.com/restaurants.jpeg";
    this.allDecks.yelpRestaurants.title = "Restaurants";
    this.allDecks.yelpShops.image = "//decidor.s3.amazonaws.com/shops.jpeg";
    this.allDecks.yelpShops.title = "Shops";
    this.allDecks.yelpArts.image = "//decidor.s3.amazonaws.com/arts.jpeg";
    this.allDecks.yelpArts.title = "Entertainment";
    this.allDecks.yelpParks.image = "//decidor.s3.amazonaws.com/parks.jpeg";
    this.allDecks.yelpParks.title = "Parks";
    this.allDecks.custom.title = "Custom Yelp";
    this.allDecks.custom.image = "//decidor.s3.amazonaws.com/yelp-avatar.png";
    this.allDecks.fictionDeck.image =
      "//decidor.s3.amazonaws.com/NYT_yellow_square.png";
    this.allDecks.fictionDeck.title = "Fiction";
    this.allDecks.nonFictionDeck.image =
      "//decidor.s3.amazonaws.com/NYT_blue_square.png";
    this.allDecks.nonFictionDeck.title = "Non-Fiction";
    this.allDecks.cookoutMilkshakes.title = "Cookout Milkshakes";
    this.allDecks.cookoutMilkshakes.image =
      "//decidor.s3.amazonaws.com/cookoutmilkshake.jpeg";
    this.allDecks.netflixFilmsDeck.title = "Netflix Films";
    this.allDecks.netflixFilmsDeck.image =
      "//decidor.s3.amazonaws.com/netflix_white.png";
    this.allDecks.inTheaters.title = "In Theaters Now";
    this.allDecks.inTheaters.image =
      "//decidor.s3.amazonaws.com/toy_story.jpeg";
  },
  methods: {
    sendKey(key) {
      this.getCardsOnClick(key);
      this.getSearchParam(key);
      this.getBookCategory(key);
    },
    getCardsOnClick(key) {
      this.hiddenDeck = true;
      this.hiddenContainer = true;
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
      } else if (key.includes("custom")) {
        this.hiddenCustomSearch = false;
      } else if (key.includes("inTheaters")) {
        this.hiddenMovieSearch = false;
      }
    },
    getLocation: function() {
      if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(this.showPosition);
      } else {
        this.error = "Geolocation is not supported.";
      }
    },
    showPosition: function(position) {
      this.lat = position.coords.latitude;
      this.lon = position.coords.longitude;
      this.getLatLonBusinesses();
    },
    getSearchParam(key) {
      if (key.includes("yelpRestaurants")) {
        this.searchingFor = "categories=restaurants";
      } else if (key.includes("yelpShops")) {
        this.searchingFor = "categories=shopping,all";
      } else if (key.includes("yelpArts")) {
        this.searchingFor = "categories=arts,aquariums,localflavor";
      } else if (key.includes("yelpParks")) {
        this.searchingFor = "categories=parks,dog_parks,skate_parks";
      }
    },
    buildLatLonURL(url, searchingfor, lat, lon) {
      return `${yelpBaseURL}${this.searchingFor}&latitude=${this.lat}&longitude=${this.lon}`;
    },
    buildYelpURL(url, searchingFor, location) {
      return `${yelpBaseURL}${this.searchingFor}&location=${this.cityName}`;
    },
    getLatLonBusinesses() {
      if (!this.hiddenCustomSearch) {
        console.log("searchTerm:", this.searchTerm);
        this.formattedSearch = this.searchTerm;
        this.formattedSearch = this.formattedSearch.replace(" ", "+");
        this.searchingFor = `term=${this.formattedSearch}`;
      }

      let apiURL = this.buildLatLonURL(
        yelpBaseURL,
        this.searchingFor,
        this.lat,
        this.lon
      );
      console.log(apiURL);

      axios
        .get(apiURL, {
          headers: {
            "Access-Control-Allow-Origin": "*",
            Authorization: `Bearer ${yelpApiKey}`
          }
        })
        .then(response => {
          this.allDecks.businesses = response.data.businesses;
          this.filterBusinesses(this.allDecks.businesses);
          this.hiddenBusiness = false;
        })
        .catch(error => {});
    },
    getBusinesses() {
      if (!this.hiddenCustomSearch) {
        console.log("searchTerm:", this.searchTerm);
        this.formattedSearch = this.searchTerm;
        this.formattedSearch = this.formattedSearch.replace(" ", "+");
        this.searchingFor = `term=${this.formattedSearch}`;
      }

      let apiURL = this.buildYelpURL(
        yelpBaseURL,
        this.searchingFor,
        this.cityName
      );
      console.log(apiURL);

      axios
        .get(apiURL, {
          headers: {
            "Access-Control-Allow-Origin": "*",
            Authorization: `Bearer ${yelpApiKey}`
          }
        })
        .then(response => {
          this.allDecks.businesses = response.data.businesses;
          this.filterBusinesses(this.allDecks.businesses);
          this.hiddenBusiness = false;
        })
        .catch(error => {});
    },
    filterBusinesses() {
      this.allDecks.businesses.map(business => {
        let businessName = business.name;
        let businessImageURL = business.image_url;
        // let businessRating = business.rating;
        let businessURL = business.url;

        this.allDecks.yelpRestaurants.push({
          title: businessName,
          card_image: businessImageURL,
          // rating: businessRating,
          url: businessURL
        });
        this.allDecks.businesses = [];
        this.hiddenSearch = true;
        this.hiddenCustomSearch = true;
        return this.allDecks.yelpRestaurants;
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
        .catch(error => {});
    },
    filterFictionBooks() {
      this.results.books.map(book => {
        let bookTitle = book.title;
        let bookAuthor = book.author;
        let bookDescription = book.description;
        let bookCover = book.book_image;
        let bookURL = book.amazon_product_url;

        this.allDecks.fictionDeck.push({
          title: bookTitle,
          description: bookDescription,
          card_image: bookCover,
          url: bookURL
        });
        this.results = [];
        return this.allDecks.fictionDeck;
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
        .catch(error => {});
    },
    filterNonFictionBooks() {
      this.results.books.map(book => {
        let bookTitle = book.title;
        let bookAuthor = book.author;
        let bookDescription = book.description;
        let bookCover = book.book_image;
        let bookURL = book.amazon_product_url;

        this.allDecks.nonFictionDeck.push({
          title: bookTitle,
          description: bookDescription,
          card_image: bookCover,
          url: bookURL
        });
        this.results = [];
        return this.allDecks.nonFictionDeck;
      });
    },
    getCityID() {
      let completeCityURL = movieCityURL + "query=" + this.cityName;
      console.log("url", completeCityURL);

      axios
        .get(completeCityURL, {
          headers: {
            Authorization: `Token ${movieApiKey}`
          }
        })
        .then(response => {
          this.cities = response.data.cities;
          console.log(response.data.cities);
          this.cityID = this.cities[0].id;
          console.log("cityID=", this.cityID);
          this.makeMovieCityURL();
        })
        .catch(error => {
          console.log(error);
        });
    },
    getMovieLocation: function() {
      if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(this.showPosition);
      } else {
        this.error = "Geolocation is not supported.";
      }
    },
    showPosition: function(position) {
      this.lat = position.coords.latitude;
      this.lon = position.coords.longitude;
      this.makeMovieLatLonURL();
    },
    makeMovieLatLonURL(url) {
      this.movieLocation = `&location=${this.lat},${this.lon}`;
      this.getMovies();
    },
    makeMovieCityURL() {
      this.movieLocation = `&city_ids=${this.cityID}`;
      this.getMovies();
    },
    getMovies() {
      let todaysDate = new Date();
      let month = ("0" + (todaysDate.getMonth() + 1)).slice(-2);
      let date = ("0" + todaysDate.getDate()).slice(-2);
      let year = todaysDate.getFullYear();
      let formattedDate = year + "-" + month + "-" + date;

      let startDate = new Date();
      let sDate = ("0" + startDate.getDate()).slice(-2);
      let sMonth = ("0" + (startDate.getMonth() - 1)).slice(-2);
      let sYear = startDate.getFullYear();
      let twoMonthsAgoDate = sYear + "-" + sMonth + "-" + sDate;

      let movieApiURL = `${movieBaseURL}${formattedDate}&release_date_from=${twoMonthsAgoDate}`;
      movieApiURL = movieApiURL + this.movieLocation;
      console.log("url", movieApiURL);

      axios
        .get(movieApiURL, {
          headers: {
            Authorization: `Token ${movieApiKey}`
          }
        })
        .then(response => {
          this.allDecks.movies = response.data.movies;
          console.log(response.data.movies);
          this.filterMovies(this.allDecks.movies);
          this.hiddenMovies = false;
          this.hiddenMovieSearch = true;
        })
        .catch(error => {
          console.log(error);
        });
    },
    filterMovies() {
      let filteredMovies = this.allDecks.movies.filter(
        movie => movie.poster_image !== null
      );
      filteredMovies.map(movie => {
        let movieTitle = movie.title;
        let movieDescription = movie.slug;
        let movieCover = movie.poster_image;

        this.allDecks.inTheaters.push({
          title: movieTitle,
          description: movieDescription,
          card_image: movieCover
        });
        filteredMovies = [];
        this.allDecks.movies = [];
        return this.allDecks.inTheaters;
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
        this.makeNetflixFilmsDeck(this.database);
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
      this.database[2].card_set.map(card => {
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
      this.database[3].card_set.map(card => {
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
      this.database[5].card_set.map(card => {
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
    }
  }
};
</script>