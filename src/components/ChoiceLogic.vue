<template>
  <section class="buttons-container or" id="choice-logic">
    <h1 class="this-or-that">Which do you prefer?</h1>
    <progress class="progress" id="progress-bar" value="0" max="1"></progress>
    <button
      v-for="(option, index) in options"
      :key="`${option}${index}`"
      @click="selectOption(index)"
      class="option-buttons"
      :disabled="validated"
      :class="{ finalChoice: onlyChoice }"
    >
      <transition appear name="enlorge">
        <div class="cardContainer">
          <img class="cardImage" :src="option.card_image" />
          <h2 class="cardTitle">{{option.title}}</h2>
        </div>
      </transition>
    </button>
  </section>
</template>


<script>
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
      totalNumChoices: 0,
      clicks: 0
    };
  },
  mounted() {
    this.shuffle(this.choices);
    this.copyChoiceList = this.choices;

    this.setOptions();

    let progressBar = document.querySelector('#progress-bar');
    console.log('progress bar', progressBar)
    progressBar.max = this.calculateTotalChoices();
    // console.log("currentIndex", this.currentIndex)
    // console.log("endIndex", this.endIndex)
    // console.log(document.querySelector('#progress-bar').value)
  },
  methods: {
    calculateTotalChoices() {
      let round = 0;
      let choicesPerRound = this.copyChoiceList.length;
      // console.log(round)
      while (round != 1) {
        choicesPerRound = choicesPerRound - round;
        round = Math.floor(choicesPerRound / 2);
        this.totalNumChoices += round
        // console.log(round)
      }
      return this.totalNumChoices
    },
    setOptions() {
      this.endIndex = this.currentIndex + 2;
      // console.log("end index:", this.endIndex)
      // console.log("pref:", this.preferences);
      this.options = this.copyChoiceList.slice(
        this.currentIndex,
        this.endIndex
      );
      this.clicks ++
      console.log(this.clicks)
    },
    selectOption(index) {
      this.currentIndex = this.currentIndex + 2;
      const toAdd = this.options[index];
      this.preferences.push(toAdd);
      let progressBar = document.querySelector('#progress-bar');
      progressBar.value = this.clicks
      console.log('progress bar', progressBar)
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