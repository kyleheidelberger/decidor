<template>
  <section class="deck">
    <h1 v-if="!hiddenNav" class="decks-info">Your decks</h1>

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
          <div class="deck-container deck-grid">
            <h2 class="deckTitle">{{deck.title}}</h2>
            <div class="overlay">
              <img class="deckImage" :src="deck.image" />
            </div>
          </div>
        </button>

        <h2 v-if="!hiddenNav" class="deckInfo2">Local Decks</h2>
        <button
          id="deckButton"
          v-for="(deck, key) in yelpDecks"
          :key="`${deck}${key}`"
          class="deckButton"
          @click="sendKey(key)"
          :class="{ hiddenDick: hiddenDeck }"
        >
          <div class="deck-container deck-grid">
            <h2 class="deckTitle">{{deck.title}}</h2>
            <div class="overlay">
              <img class="deckImage" :src="deck.image" />
            </div>
          </div>
        </button>

        <div v-if="!hiddenSearch" class="searchBar">
          <input type="text" v-model.lazy="cityName" v-on:change="getBusinesses" placeholder="City" />
          <button @click="getBusinesses">Get Businesses</button>
          <p>
            Input your current location.
            You are currently looking in: {{ cityName }}
          </p>
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
          <ChoiceLogic :choices="yelpDecks.yelpRestaurants" />
        </div>

        <div
          v-for="(business, index) in yelpDecks.yelpRestaurants"
          :key="`${business}${index}`"
          class="deck-container"
        >
          <!-- <a :href="business.url" target="_blank"> -->
          <h2 class="deckTitle">{{ business.name }}</h2>
          <div>
            <img :src="business.imageURL" class="deckImage" />
          </div>
          <!-- </a> -->
        </div>
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
        foodTypesDeck: []
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
      hiddenNav: false
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
      {
        title: "Queer Eye",
        card_image: "http://static.tvgcdn.net/feed/1/548/118938548.jpg"
      },
      {
        title: "Stranger Things",
        card_image:
          "https://images-na.ssl-images-amazon.com/images/I/71OB1IywjLL._SY679_.jpg"
      },
      {
        title: "Bojack Horseman",
        card_image:
          "https://i.pinimg.com/originals/91/df/30/91df30f6063a67073293864aba9357a9.jpg"
      },
      {
        title: "Unbreakable Kimmy Schmidt",
        card_image:
          "https://m.media-amazon.com/images/M/MV5BMTgyNTQyNjUwN15BMl5BanBnXkFtZTgwNjMwNjUzNzM@._V1_.jpg"
      },
      {
        title: "American Vandal",
        card_image:
          "https://static2.showtimes.com/poster/540x800/american-vandal-netflix-119343.jpg"
      },
      {
        title: "Mindhunter",
        card_image:
          "https://static.tvgcdn.net/feed/1/2/thumbs/118553002_1197x1596.jpg"
      },
      {
        title: "Russian Doll",
        card_image:
          "https://m.media-amazon.com/images/M/MV5BYmViMjdhZmQtODIyZi00Mzc4LWFhNTItOTk4NGM1NGU0ZDZjXkEyXkFqcGdeQXVyNjc2NTQzMjU@._V1_.jpg"
      },
      {
        title: "Master of None",
        card_image:
          "https://ih0.redbubble.net/image.511228335.0654/flat,550x550,075,f.u1.jpg"
      },
      {
        title: "GLOW",
        card_image:
          "https://images-na.ssl-images-amazon.com/images/I/71edS3VeIcL._SY679_.jpg"
      },
      {
        title: "Big Mouth",
        card_image:
          "https://images-na.ssl-images-amazon.com/images/I/81QBTBizRxL._SY679_.jpg"
      },
      {
        title: "Dark",
        card_image:
          "https://i.pinimg.com/originals/67/5e/bc/675ebc2fd210a8bd5362928a51514960.jpg"
      },
      {
        title: "The Crown",
        card_image:
          "https://m.media-amazon.com/images/M/MV5BMjAxOTA2Mjc3MF5BMl5BanBnXkFtZTgwMTMxMzIxNDM@._V1_.jpg"
      },
      {
        title: "Orange is the New Black",
        card_image:
          "https://m.media-amazon.com/images/M/MV5BYjYyM2FmMmMtZDgyZi00NGU3LWI3NzktODllZDY0YzQyNzgyXkEyXkFqcGdeQXVyMTkxNjUyNQ@@._V1_.jpg"
      },
      {
        title: "Dead to Me",
        card_image:
          "https://m.media-amazon.com/images/M/MV5BODkwNmY1MjgtY2ZlNS00MWVmLWEzZTktYmMyNDQzMjlmMGY2XkEyXkFqcGdeQXVyMTkxNjUyNQ@@._V1_.jpg"
      },
      {
        title: "Black Mirror",
        card_image:
          "https://m.media-amazon.com/images/M/MV5BMjM5MzgzMjM3OF5BMl5BanBnXkFtZTgwMzQ2MzQwNzM@._V1_.jpg"
      },
      {
        title: "The Umbrella Academy",
        card_image:
          "https://m.media-amazon.com/images/M/MV5BNTFhOTk1NTgtYWM1ZS00NWI1LTgzYzAtYmE5MjZiMDE0NzlhXkEyXkFqcGdeQXVyMTkxNjUyNQ@@._V1_.jpg"
      },
      {
        title: "Grade & Frankie",
        card_image:
          "https://m.media-amazon.com/images/M/MV5BODg0MjIzOTc4MV5BMl5BanBnXkFtZTgwNDE3NTIxNzM@._V1_.jpg"
      },
      {
        title: "Our Planet",
        card_image:
          "https://m.media-amazon.com/images/M/MV5BN2I1ZjA5YjQtYmQ0ZS00ZmE1LTk1ZjktNTQ5ODIzY2JiZDdhXkEyXkFqcGdeQXVyNjg2NjQwMDQ@._V1_.jpg"
      },
      {
        title: "Sex Education",
        card_image:
          "https://m.media-amazon.com/images/M/MV5BOTE0MjQ1NDU3OV5BMl5BanBnXkFtZTgwNTI4MTgwNzM@._V1_.jpg"
      },
      {
        title: "Dear White People",
        card_image:
          "https://m.media-amazon.com/images/M/MV5BNjQ1OTU3MWUtYTU1Ny00NGFkLTk1MTItMjM4ZWQ4M2IxMTdhXkEyXkFqcGdeQXVyNjg2NjQwMDQ@._V1_.jpg"
      },
      {
        title: "You",
        card_image:
          "https://i.pinimg.com/originals/93/bc/eb/93bceb9dc583c4511b9742b182b763aa.jpg"
      },
      {
        title: "Bloodline",
        card_image:
          "https://m.media-amazon.com/images/M/MV5BMTU4OTY0MzM1OV5BMl5BanBnXkFtZTgwMjkxMzE0MjI@._V1_.jpg"
      },
      {
        title: "House of Cards",
        card_image:
          "https://m.media-amazon.com/images/M/MV5BNmM4ODU1MzItODYyYi00Y2U0LWFjZjItYTRhZWIwOGMyZTRhXkEyXkFqcGdeQXVyNjc2NTQ4Nzk@._V1_.jpg"
      },
      {
        title: "Daredevil",
        card_image:
          "https://m.media-amazon.com/images/M/MV5BODcwOTg2MDE3NF5BMl5BanBnXkFtZTgwNTUyNTY1NjM@._V1_.jpg"
      },
      {
        title: "Fuller House",
        card_image:
          "https://m.media-amazon.com/images/M/MV5BMjAxMzU5MzA0MF5BMl5BanBnXkFtZTgwODgyOTg1MzI@._V1_.jpg"
      },
      {
        title: "Narcos",
        card_image:
          "https://m.media-amazon.com/images/M/MV5BMTcyODAxNzcwNF5BMl5BanBnXkFtZTgwNzM1Mjc1NjM@._V1_.jpg"
      }
    ];
    this.allDecks.netflixDeck.image =
      "https://cdn.vox-cdn.com/thumbor/AwKSiDyDnwy_qoVdLPyoRPUPo00=/39x0:3111x2048/1400x1400/filters:focal(39x0:3111x2048):format(png)/cdn.vox-cdn.com/uploads/chorus_image/image/49901753/netflixlogo.0.0.png";
    this.allDecks.netflixDeck.title = "Netflix Originals";
    this.allDecks.fastFoodDeck = [
      {
        title: "McDonald's",
        card_image:
          "https://upload.wikimedia.org/wikipedia/commons/3/36/McDonald%27s_Golden_Arches.svg"
      },
      {
        title: "Chick-Fil-A",
        card_image:
          "https://upload.wikimedia.org/wikipedia/en/0/02/Chick-fil-A_Logo.svg"
      },
      {
        title: "Wendy's",
        card_image:
          "https://upload.wikimedia.org/wikipedia/en/6/66/Wendy%27s_logo_2012.svg"
      },
      {
        title: "Burger King",
        card_image:
          "https://upload.wikimedia.org/wikipedia/commons/3/3a/Burger_King_Logo.svg"
      },
      {
        title: "Bojangles",
        card_image:
          "https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fimg1.southernliving.timeinc.net%2Fsites%2Fdefault%2Ffiles%2Fstyles%2F4_3_horizontal_-_1200x900%2Fpublic%2Fimage%2F2018%2F07%2Fmain%2Fddul_zmv4aauhhf.jpg%3Fitok%3DAWbx6bKH%261532464651&w=400&c=sc&poi=face&q=85"
      },
      {
        title: "Subway",
        card_image:
          "https://upload.wikimedia.org/wikipedia/commons/5/5c/Subway_2016_logo.svg"
      },
      {
        title: "Sonic",
        card_image:
          "https://upload.wikimedia.org/wikipedia/en/d/df/Sonic_Drive-In_logo.svg"
      },
      {
        title: "Taco Bell",
        card_image:
          "https://upload.wikimedia.org/wikipedia/en/b/b3/Taco_Bell_2016.svg"
      },
      {
        title: "Arby's",
        card_image:
          "https://upload.wikimedia.org/wikipedia/en/f/f4/Arby%27s_logo.svg"
      },
      {
        title: "Moe's",
        card_image:
          "http://laxteams.net/files_public/1/1097/files/2013_Sponsors/Moes_button_over_green.jpg"
      },
      {
        title: "Pizza Hut",
        card_image:
          "https://upload.wikimedia.org/wikipedia/commons/7/73/Pizza_Hut_1967-1999_logo.svg"
      },
      {
        title: "Domino's",
        card_image:
          "https://upload.wikimedia.org/wikipedia/commons/3/3e/Domino%27s_pizza_logo.svg"
      },
      {
        title: "KFC",
        card_image:
          "https://upload.wikimedia.org/wikipedia/en/b/bf/KFC_logo.svg"
      },
      {
        title: "Papa John's",
        card_image:
          "https://upload.wikimedia.org/wikipedia/commons/f/f0/Papa_John%27s_Logo_2019.svg"
      },
      {
        title: "Chipotle",
        card_image:
          "https://upload.wikimedia.org/wikipedia/en/3/3b/Chipotle_Mexican_Grill_logo.svg"
      },
      {
        title: "Popeye's",
        card_image:
          "https://upload.wikimedia.org/wikipedia/en/b/bc/Popeyes_Louisiana_Kitchen.svg"
      },
      {
        title: "Jersey Mike's",
        card_image:
          "https://upload.wikimedia.org/wikipedia/en/9/91/Jersey_Mike%27s_logo.svg"
      }
    ];
    this.allDecks.fastFoodDeck.image =
      "https://nationaltoday.com/wp-content/uploads/2019/07/national-french-fry-day.jpg";
    this.allDecks.fastFoodDeck.title = "Fast Food Chains";
    this.allDecks.activityDeck = [
      {
        title: "Play a Sport",
        card_image:
          "https://blog.playo.co/wp-content/uploads/2016/12/Ultimate-frisbee.jpg"
      },
      {
        title: "Go to the Movies",
        card_image:
          "https://blindgossip.com/wp-content/uploads/2018/05/couple-popcorn-movies.jpg"
      },
      {
        title: "Go to a Park",
        card_image:
          "https://static8.depositphotos.com/1000857/922/i/950/depositphotos_9226599-stock-photo-central-park-new-york-beautiful.jpg"
      },
      {
        title: "Go out to Eat",
        card_image:
          "https://www.smallbizdaily.com/wp-content/uploads/2016/08/ThinkstockPhotos-466378405.jpg"
      },
      {
        title: "Read a Book",
        card_image:
          "https://static.jeffbullas.com/wp-content/uploads/2016/01/7-Inspiring-books.jpg"
      },
      {
        title: "Go Bowling",
        card_image:
          "http://tenpins-more.com/resources/2017_Material/Glow-in-the-Dark.png?timestamp=1493587484666"
      },
      {
        title: "Go for a Walk/Hike",
        card_image: "https://www.cincynature.org/media/images/trail2_img-52.jpg"
      },
      {
        title: "Try a New Recipe",
        card_image:
          "https://news.flinders.edu.au/wp-content/uploads/2018/06/healthy-cooking-at-home.jpg"
      },
      {
        title: "Go to the Gym",
        card_image:
          "https://www.virginactive.com.au/images/library/Blog/Media/Workoutready_730x411.jpg"
      },
      {
        title: "Ride a Bike",
        card_image:
          "https://static.wixstatic.com/media/cb0988_778b1e8d3cc741178850d634059a5421~mv2.jpg"
      },
      {
        title: "Go Shopping",
        card_image:
          "https://thenypost.files.wordpress.com/2018/06/men-shopping-masculine.jpg?quality=90&strip=all&w=618&h=410&crop=1"
      },
      {
        title: "Start Learning a New Skill",
        card_image:
          "https://www.merries.co.id/uploads/2015/10/Benarkah-Anak-Belajar-Bahasa-Asing-Tidak-Mudah-Frustasi.jpg"
      },
      {
        title: "Go out for a Drink",
        card_image:
          "https://wgme.com/resources/media/4361daf4-9cae-4271-8334-3e95c5efbf13-large16x9_GettyImages1060456922.jpg?1564659754622"
      },
      {
        title: "Plan a Vacation",
        card_image:
          "https://radioimg.s3.amazonaws.com/womcfm/styles/delta__775x515/s3/Vacation.jpg?itok=kYmnrvXA"
      },
      {
        title: "Draw, Color, or Paint",
        card_image:
          "https://img.freepik.com/free-photo/human-hand-holding-origami-bird-craft-product_23-2148188394.jpg?size=626&ext=jpg"
      },
      {
        title: "Do Yoga",
        card_image:
          "https://media3.s-nbcnews.com/j/newscms/2019_29/2940406/190719-yoga-stock-mn-1505_4f11f09072135a3989a050bdd89fdcfb.fit-760w.jpg"
      },
      {
        title: "Play a Board Game",
        card_image:
          "https://www.idaho-jones.com/wp-content/uploads/chesstime-1254x627.jpg"
      }
    ];
    this.allDecks.activityDeck.image =
      "https://blindgossip.com/wp-content/uploads/2018/05/couple-popcorn-movies.jpg";
    this.allDecks.activityDeck.title = "Activities";
    this.allDecks.foodTypesDeck = [
      {
        title: "American",
        card_image:
          "http://pngimg.com/uploads/burger_sandwich/burger_sandwich_PNG4114.png"
      },
      {
        title: "Chinese",
        card_image:
          "https://www.pngkey.com/png/full/48-486539_fantastic-chinese-and-beijing-cuisine-in-grays-from.png"
      },
      {
        title: "Thai",
        card_image:
          "https://www.sccpre.cat/mypng/full/165-1658915_pad-thai-chicken-thai-food-transparent-background.png"
      },
      {
        title: "Italian",
        card_image:
          "http://www.pngmart.com/files/5/Spaghetti-PNG-Transparent-Image.png"
      },
      {
        title: "Mexican",
        card_image: "https://ui-ex.com/images/taco-transparent-background-6.png"
      },
      {
        title: "Japanese",
        card_image:
          "https://www.suviche.com/static/sitefiles/menu_manager/cilantro_roll1.png"
      },
      {
        title: "Seafood",
        card_image: "https://longfordpc.com/images/seafood-clipart-chips-15.png"
      },
      {
        title: "Barbecue",
        card_image:
          "https://webstockreview.net/images/grill-clipart-bbq-chicken-3.png"
      },
      {
        title: "Indian",
        card_image: "http://pluspng.com/img-png/meat-curry-700.png"
      },
      {
        title: "Pizza",
        card_image: "http://www.pngmart.com/files/1/Cheese-Pizza.png"
      },
      {
        title: "Korean",
        card_image: "https://tchol.org/images/kimchi-png-2.png"
      },
      {
        title: "Cuban",
        card_image:
          "https://www.pngkey.com/png/full/206-2062130_nuestras-empanadas-empanadas-salteas-png.png"
      },
      {
        title: "Mediterranean",
        card_image:
          "https://www.chrisanthidis.gr/en/assets/components/phpthumbof/cache/40.b6f57f458e1d7ac994e539f631c2897b.png"
      },
      {
        title: "French",
        card_image:
          "https://peoplepng.com/wp-content/uploads/2019/02/quiche-png-2.png"
      },
      {
        title: "Jamaican",
        card_image: "https://i.dlpng.com/static/png/3950128_thumb.png"
      },
      {
        title: "Middle Eastern",
        card_image: "https://www.pngarts.com/files/4/Falafel-PNG-Pic.png"
      },
      {
        title: "Steakhouse",
        card_image: "http://pluspng.com/img-png/png-steak-steak-png-500.png"
      },
      {
        title: "Spanish",
        card_image:
          "https://pngimage.net/wp-content/uploads/2018/06/tapas-png-5.png"
      },
      {
        title: "Pub",
        card_image:
          "http://pluspng.com/img-png/fish-and-chips-png-hd-fish-png-fish-and-chips-png-500.png"
      }
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