

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
      <a :href="business.url">{{ business.name }}</a>
      <img :src="business.image_url" class="yelp-business-image" />"
    </div>
  </section>
</template>


<script>
import axios from "axios";

const yelpBaseURL =
  "https://cors-anywhere.herokuapp.com/https://api.yelp.com/v3/businesses/search?categories=food,all&location=";
const apiKey =
  "SM6pJx7LlCeKgElTpKU3PgsBDvqZud92PBBhqRBOEunqL9az6MmnAN9GUf4_mjjQva10STsyAlOs6RacEdskjV3qx7X_SjhqtpFVY0G0KzKvDoXcb4s-X2eZHOc5XXYx";
// const LOCATIONS = "Durham, Greensboro, Raleigh";

function buildURL(url) {
  return yelpBaseURL + url;
}

export default {
  name: "YelpDeck",
  props: {
    choices: {
      type: Array,
      default() {
        return [
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
      }
    }
  },
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
      //   cityName: "Durham",
      businesses: [],
      //   locations: LOCATIONS.split(","), // create an array of locations
      cityName: "" // set default location to Durham
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
  //     searchYelp(cityName) {
  //       axios
  //         .get(
  //           `https://cors-anywhere.herokuapp.com/https://api.yelp.com/v3/businesses/search?categories=food,all&location=${cityName}`,
  //           {
  //             headers: {
  //               "Access-Control-Allow-Origin": "*",
  //               Authorization: `Bearer SM6pJx7LlCeKgElTpKU3PgsBDvqZud92PBBhqRBOEunqL9az6MmnAN9GUf4_mjjQva10STsyAlOs6RacEdskjV3qx7X_SjhqtpFVY0G0KzKvDoXcb4s-X2eZHOc5XXYx`
  //             }
  //           }
  //         )
  //         .then(response => (this.info = response));
  //     },

  //     showResults(cityName) {
  //       // call searchYelp to get API data
  //       this.searchYelp(this.cityName).then(function(data) {
  //         console.log(data);

  //         // grabs result list div and sets it to empty
  //         const resultList = document.querySelector("#result-list");
  //         resultList.innerHTML = "";

  //         // loops through data.businesses array
  //         for (index = 0; index < data.businesses.length; index++) {
  //           // create a div for each result
  //           const result = document.createElement("div");
  //           //then creates separate div elements inside result div for info and cover img
  //           const resultInfo = document.createElement("div");
  //           const resultImage = document.createElement("div");

  //           // add classes to divs
  //           result.classList.add("result");
  //           resultInfo.classList.add("result-details", "container");
  //           resultImage.classList.add("result-image-div", "container");

  //           // assigns data from fetch businesses to variables:
  //           let resultName = data.businesses[index].name;
  //           let resultImageURL = data.businesses[index].image_url;

  //           // puts data into divs
  //           resultInfo.innerHTML = `<ul class="unstyled"><li><strong>${resultName}</strong></li></ul>`;
  //           resultImage.innerHTML = `<img class="resultArt" src="${resultImageURL}">`;

  //           // update the new result
  //           result.append(resultImage, resultInfo);
  //           // update result list with new result
  //           resultList.append(result);
  //         }
  //       });
  //     },

  //     buttonListener() {
  //       // assigns search bar to variable userSearch
  //       let button = document.querySelector(".button");
  //       // adds 'change' event to userSearch so that event occurs when input is changed
  //       // event.preventDefault prevents page from refreshing
  //       button.addEventListener("click", function(event) {
  //         event.preventDefault();
  //         // adds user term= to user input and encodes for url
  //         let cityName = encodeURIComponent(button.value);
  //         console.log(cityName);
  //         // clears the search
  //         button.value = "";
  //       });
  //     }
  //   }
  computed: {
    processedBusinesses() {
      let businesses = this.businesses;

      businesses.map(post => {
        let imgObj = post.multimedia.find(
          media => media.format === "superJumbo"
        );
        business.image_url = imgObj
          ? imgObj.url
          : "http://placehold.it/300x200?text=N/A";
      });

      let i,
        j,
        chunkedArray = [],
        chunk = 4;
      for (i = 0, j = 0; i < business.length; i += chunk, j++) {
        chunkedArray[j] = businesses.slice(i, i + chunk);
      }
      return chunkedArray;
    }
  }
};
</script>