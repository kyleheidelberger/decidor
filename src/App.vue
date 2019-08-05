<template>
  <main id="app">
    <router-link to="landing">Landing</router-link>
    <router-link to="decks">Decks</router-link>
    <router-link to="choicelogic">Choice Logic</router-link>
    <a href="">Register</a>
    <router-view/>
  </main>
</template>

<script>


export default {
  name: "app",
  
};
</script>