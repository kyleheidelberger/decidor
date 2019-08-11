<template>
  <section class="buttons-container or" id="choice-logic">
    <h1 v-if="!onlyChoice" class="this-or-that">Which do you prefer?</h1>
    <div v-if="onlyChoice" class="this-or-that">
      <h1
        v-for="(option, index) in options"
        :key="`${option}${index}`"
      >{{option.title}}! Great Choice!</h1>
    </div>
    <progress class="progress" id="progress-bar" value="0" max="1"></progress>
    <button
      v-for="(option, index) in options"
      :key="`${option}${index}`"
      @click="selectOption(index), triggerConfetti()"
      class="option-buttons"
      :disabled="validated"
      :class="{ finalChoice: onlyChoice }"
    >
      <transition appear name="enlorge">
        <div class="cardContainer">
          <div v-if="!onlyChoice">
            <img class="cardImage" :src="option.card_image" :alt="option.description" />
            <h2 class="cardTitle">{{option.title}}</h2>
          </div>
          <a v-if="onlyChoice" :href="option.url" target="_blank">
            <img class="cardImage" :src="option.card_image" :alt="option.description" />
            <h2 class="cardTitle">{{option.title}}</h2>
          </a>
        </div>
      </transition>
    </button>
  </section>
</template>


<script>
import Vue from "vue";
import VueConfetti from "vue-confetti";

Vue.use(VueConfetti);

export default {
  name: "ChoiceLogic",
  props: {
    choices: {
      type: Object,
      default() {
        return [{ title: String, card_image: String }];
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
      clicks: 0
    };
  },
  mounted() {
    this.shuffle(this.choices);
    this.copyChoiceList = this.choices;
    let progressBar = document.querySelector("#progress-bar");
    console.log("progress bar", progressBar);
    progressBar.max = this.choices.length - 1;
    // console.log("currentIndex", this.currentIndex)
    // console.log("endIndex", this.endIndex)
    console.log(document.querySelector("#progress-bar").value);
    console.log(document.querySelector("#progress-bar").max);
    this.setOptions();
  },
  methods: {
    triggerConfetti() {
      if (this.onlyChoice === true) {
        this.$confetti.start({});
      }
    },
    setOptions() {
      this.endIndex = this.currentIndex + 2;
      // console.log("end index:", this.endIndex)
      // console.log("pref:", this.preferences);
      this.options = this.copyChoiceList.slice(
        this.currentIndex,
        this.endIndex
      );
      this.clicks++;
      console.log(this.clicks);
    },
    selectOption(index) {
      this.currentIndex = this.currentIndex + 2;
      const toAdd = this.options[index];
      this.preferences.push(toAdd);
      let progressBar = document.querySelector("#progress-bar");
      progressBar.value = this.clicks;
      console.log("progress bar", progressBar);
      // console.log("end index:", this.endIndex)
      // console.log("copy choice list length:", this.copyChoiceList.length);
      if (this.endIndex >= this.copyChoiceList.length - 1) {
        if (this.endIndex != this.copyChoiceList.length) {
          this.preferences.push(
            this.copyChoiceList[this.copyChoiceList.length - 1]
          );
        }
        this.currentIndex = 0;
        this.copyChoiceList = this.preferences;
        this.preferences = [];
        // console.log("end index after preferences cleared:", this.endIndex)
        // console.log("after:", this.endIndex);
      }
      if (this.copyChoiceList.length === 1) {
        this.onlyChoice = true;
        this.validated = true;
      }
      this.setOptions();
    },
    shuffle(choices) {
      var m = choices.length,
        t,
        i;
      while (m) {
        i = Math.floor(Math.random() * m--);
        t = choices[m];
        choices[m] = choices[i];
        choices[i] = t;
      }
      return choices;
    }
  }
};
</script>