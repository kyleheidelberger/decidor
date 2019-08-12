<template>
  <section class="buttons-container or" id="choice-logic">
    <h1 v-if="!onlyChoice" class="this-or-that">Which do you prefer?</h1>
    <div v-if="onlyChoice" class="this-or-that">
      <h1
        class="great-choice"
        v-for="(option, index) in options"
        :key="`${option}${index}`"
      ><em>{{option.title}}!</em> Great Choice!</h1>
    </div>
    <progress v-if="!onlyChoice" class="progress" id="progress-bar" value="0" max="1"></progress>
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
            <!-- <h2 class="cardTitle">{{option.title}}</h2> -->
          </a>
        </div>
      </transition>
    </button>
    <a v-if="onlyChoice" href="" class="fill another-choice">Make Another Choice</a>
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
      clicks: 0, 
      colors: ["round2", "round3", "round4", "round5", "round6",],
      x: 0,
    };
  },
  mounted() {
    this.shuffle(this.choices);
    this.copyChoiceList = this.choices;
    let progressBar = document.querySelector("#progress-bar");
    progressBar.max = this.choices.length - 1;
    this.setOptions();
  },
  methods: {
    changeColor (progressBar) {
      let newColor = this.colors[this.x++];
      if (this.preferences.length === 0){
        progressBar.classList.add(newColor);
      }
    },
    triggerConfetti() {
      if (this.onlyChoice === true) {
        this.$confetti.start({});
      }
    },
    setOptions() {
      this.endIndex = this.currentIndex + 2;
      this.options = this.copyChoiceList.slice(
        this.currentIndex,
        this.endIndex
      );
      this.clicks++;
    },
    selectOption(index) {
      this.currentIndex = this.currentIndex + 2;
      const toAdd = this.options[index];
      this.preferences.push(toAdd);
      let progressBar = document.querySelector("#progress-bar");
      progressBar.value = this.clicks;

      if (this.endIndex >= this.copyChoiceList.length - 1) {
        if (this.endIndex != this.copyChoiceList.length) {
          this.preferences.push(
            this.copyChoiceList[this.copyChoiceList.length - 1]
          );
        }
        this.currentIndex = 0;
        this.copyChoiceList = this.preferences;
        this.preferences = [];
        this.changeColor(progressBar);
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