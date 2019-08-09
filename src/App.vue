<script>
import Decks from "./components/Decks.vue";
import AOS from 'aos'

export default {
  created () {
  AOS.init()
},
  name: "app",
  components: {
    Decks,
  }
};
</script>

<template>
  <main id="app">
    <Decks />
  </main>

</template>

