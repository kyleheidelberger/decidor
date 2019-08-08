<template>
  <section class="buttons-container or" id="choice-logic">
    <h1 class='this-or-that'>Which do you prefer?</h1>
       <progress class="progress" id="progress-bar" value="0" max="1"></progress>
          <button
            v-for="(option, index) in options"
            :key="`${option}${index}`"
            @click="selectOption(index), setProgressBar()"
            class="option-buttons"
            :disabled="validated"
            :class="{ finalChoice: onlyChoice }">
            <transition appear
              name='enlorge'>
              <div class="cardContainer">
                  <img class="cardImage" :src="option.card_image" />
                  <h2 class="cardTitle">
                {{option.title}}</h2>
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
      endIndex: 2
    };
  },
  mounted() {
    this.copyChoiceList = this.choices;

    this.setOptions();
    // console.log("currentIndex", this.currentIndex)
    // console.log("endIndex", this.endIndex)
    // console.log(document.querySelector('#progress-bar').value)
  },
  methods: {
    setProgressBar() {
      let progressBar = document.querySelector('#progress-bar');
      progressBar.max = Math.round(((this.copyChoiceList.length / 2) - 1));
      // console.log('preferences length:', this.preferences.length)
      progressBar.value = this.preferences.length
      // console.log('progressBarValue:', progressBar.value)
      // console.log('progressBarMax:', progressBar.max)
      // console.log('copyChoiceList:', this.copyChoiceList.length)
        // for (let preference in this.preferences) {
            // console.log('copyChoiceList:', this.copyChoiceList.length)
            // if (progressBar.max === (progressBar.value + 1)) {
            //     progressBar.value === 0;
            // }
        // }
    },
    setOptions() {
      this.endIndex = this.currentIndex + 2;
      // console.log("end index:", this.endIndex)
      // console.log("pref:", this.preferences);
      this.options = this.copyChoiceList.slice(
        this.currentIndex,
        this.endIndex
      );
      // console.log("before:", this.endIndex);
    },
    selectOption(index) {
      this.currentIndex = this.currentIndex + 2;
      const toAdd = this.options[index];
      this.preferences.push(toAdd);
      console.log("end index:", this.endIndex)
      console.log("copy choice list length:", this.copyChoiceList.length);
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
    }
  }
};
</script>