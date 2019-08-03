

<template>
  <section class="buttons-container" id="choice-logic">
    <button
      v-for="(option, index) in options"
      :key="`${option}${index}`"
      @click="selectOption(index)"
      class="option-buttons button-style"
      :disabled="validated === true"
      :class="{ finalChoice: onlyChoice }"
    >{{option}}</button>

    <div id="YelpDeck">{{ info }}</div>
  </section>
</template>


<script>
import axios from "axios";

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
      info: null
    };
  },
  mounted() {
    axios.get(
      `https://cors-anywhere.herokuapp.com/https://api.yelp.com/v3/businesses/search?categories=food,all&location=Durham`,
    {headers: {
          "Access-Control-Allow-Origin": "*",
          Authorization: `Bearer SM6pJx7LlCeKgElTpKU3PgsBDvqZud92PBBhqRBOEunqL9az6MmnAN9GUf4_mjjQva10STsyAlOs6RacEdskjV3qx7X_SjhqtpFVY0G0KzKvDoXcb4s-X2eZHOc5XXYx`
        }}).then(response => (this.info = response));
    this.copyChoiceList = this.choices;
    this.setOptions();
  },
  methods: {
    setOptions() {
      this.endIndex = this.currentIndex + 2;
      console.log("pref:", this.preferences);
      this.options = this.copyChoiceList.slice(
        this.currentIndex,
        this.endIndex
      );
      console.log("before:", this.endIndex);
    },
    selectOption(index) {
      this.currentIndex = this.currentIndex + 2;
      const toAdd = this.options[index];
      this.preferences.push(toAdd);
      console.log("copychoicelist:", this.copyChoiceList);
      if (this.endIndex >= this.copyChoiceList.length - 1) {
        if (this.endIndex != this.copyChoiceList.length) {
          this.preferences.push(
            this.copyChoiceList[this.copyChoiceList.length - 1]
          );
        }
        this.currentIndex = 0;
        this.copyChoiceList = this.preferences;
        this.preferences = [];
        console.log("after:", this.endIndex);
      }
      if (this.copyChoiceList.length === 1) {
        this.onlyChoice = true;
        this.validated = true;
      }
      this.setOptions();
    }
  }
};
</script>