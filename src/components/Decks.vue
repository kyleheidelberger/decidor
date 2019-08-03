<template>
  <section class='deck'>
    <div class='container'>
        <!-- <h2 
        v-if="hiddenCards"
        @click='hiddenCards = false, hiddenDeck = true'
        class='netflixTitle'>
        </h2> -->
          <button
          id='deckButton'
          v-for='(deck, key) in allDecks'
          :key='`${deck}${key}`'
          class='deckButton'
          @click='getCardsOnClick(key)'
          :class='{ hiddenDick: hiddenDeck }'>
          {{ key }}
            <img class="netflixLogo" src='https://cdn.vox-cdn.com/thumbor/AwKSiDyDnwy_qoVdLPyoRPUPo00=/39x0:3111x2048/1400x1400/filters:focal(39x0:3111x2048):format(png)/cdn.vox-cdn.com/uploads/chorus_image/image/49901753/netflixlogo.0.0.png'>
          </button>
    </div>
    
    <div 
    v-if='!hiddenNetflix'>
        <!-- <ChoiceLogic 
        v-for='(deck, key) in allDecks'
        :key='`${deck}${key}`'
        :choices='deck'/> -->
        <ChoiceLogic :choices='allDecks.netflixDeck'/>
    </div>

     <div v-if='!hiddenFood'>
        <ChoiceLogic :choices='allDecks.fastFoodDeck'/>
        <!-- <ChoiceLogic :choices='fastFoodDeck'/> -->
    </div>

  </section>
</template>

<script>
import ChoiceLogic from './ChoiceLogic';
// import axios from 'axios';

export default {
  name: 'Decks',
  components: {
    ChoiceLogic
  },
  data: () => {
    return {
      allDecks: {
        netflixDeck: [],
        fastFoodDeck: []
      },
      // hiddenCards: true,
      hiddenDeck: false,
      hiddenNetflix: true,
      hiddenFood: true
    }
  },
  mounted() {
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

    this.allDecks.netflixDeck =
      ['Queer Eye', 'Stranger Things', 
        'Bojack Horseman', 'Orange is the New Black', 
        'Unbreakable Kimmy Schmidt', 'American Vandal', 
        'Mindhunter', 'Russian Doll',
        'Master of None', 'GLOW',
        'The Umbrella Academy', 'Big Mouth', 
        'Dark', 'The Crown']
    
    this.allDecks.fastFoodDeck = 
      ["McDonald's", "Wendy's", "Burger King", "Chick-Fil-A"]
  },
  methods: {
    getCardsOnClick(key) {
      this.hiddenDeck = true;
      if (key.includes('netflixDeck')) {
        console.log('hi')
        this.hiddenNetflix = false;
    }
      else {
        console.log("else!")
        this.hiddenFood = false;
      }
    }
  }
}
</script>