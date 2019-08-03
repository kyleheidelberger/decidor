<template>
  <section class="deck">
    <div class="container">
      <h2
        v-if="hiddenCards2"
        @click="hiddenCards2 = false, hiddenDeck = true"
        class="netflixTitle"
      >Netflix</h2>
      <button
        class="deckButton"
        @click="hiddenCards = false, hiddenDeck = true"
        :class="{ hiddenDick: hiddenDeck }"
      >
        <img
          class="netflixLogo"
          src="https://cdn.vox-cdn.com/thumbor/AwKSiDyDnwy_qoVdLPyoRPUPo00=/39x0:3111x2048/1400x1400/filters:focal(39x0:3111x2048):format(png)/cdn.vox-cdn.com/uploads/chorus_image/image/49901753/netflixlogo.0.0.png"
        />
      </button>
    </div>

    <div class="container">
      <h2
        v-if="hiddenCards2"
        @click="hiddenCards2 = false, hiddenDeck = true"
        class="yelpDeckTitle"
      >Yelp</h2>
      <button
        class="yelpDeckButton"
        @click="hiddenCards2 = false, hiddenDeck = true"
        :class="{ hiddenDick: hiddenDeck }"
      >
        <img
          class="yelpLogo"
          src="https://blog.yelp.com/wp-content/themes/yelpblog-updated/images/yelp-avatar.png"
        />
      </button>
    </div>

    <div v-if="!hiddenCards">
      <ChoiceLogic />
    </div>

    <div v-if="!hiddenCards2">
      <YelpDeck />
    </div>
  </section>
</template>

<script>
import ChoiceLogic from "./ChoiceLogic";
import YelpDeck from "./YelpDeck";

export default {
  name: "Decks",
  components: {
    ChoiceLogic,
    YelpDeck
  },
  data: () => {
    return {
      hiddenCards: true,
      hiddenCards2: true,
      hiddenDeck: false
    };
  }
};
</script>