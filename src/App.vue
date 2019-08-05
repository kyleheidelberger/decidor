<template>
  <main id="app">
    <router-link to="landing">Landing</router-link>
    <router-link to="decks">Decks</router-link>
    <router-link to="choicelogic">Choice Logic</router-link>
    <a href="http://127.0.0.1:8000/accounts/register/">Register</a>
    <router-view/>
  </main>
</template>

<script>


export default {
  name: "app",
  
};
</script>