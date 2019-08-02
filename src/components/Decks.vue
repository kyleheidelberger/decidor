<template>
  <section class='deck'>
    <div class='container'>
        <h2 
        v-if="hiddenCards"
        @click='hiddenCards = false, hiddenDeck = true'
        class='netflixTitle'>Netflix
        </h2>
            <button 
            class='deckButton'
            @click='hiddenCards = false, hiddenDeck = true'
            :class='{ hiddenDick: hiddenDeck }'>
            <img class="netflixLogo" src='https://cdn.vox-cdn.com/thumbor/AwKSiDyDnwy_qoVdLPyoRPUPo00=/39x0:3111x2048/1400x1400/filters:focal(39x0:3111x2048):format(png)/cdn.vox-cdn.com/uploads/chorus_image/image/49901753/netflixlogo.0.0.png'>
            </button>
    </div>
    
    <div v-if='!hiddenCards'>
        <ChoiceLogic />
    </div>

  </section>
</template>

<script>
import ChoiceLogic from './ChoiceLogic'

export default {
  name: 'Decks',
  components: {
    ChoiceLogic
  },
  data: () => {
    return {
      hiddenCards: true,
      hiddenDeck: false
    }
  }
}
</script>