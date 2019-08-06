<template>
  <div class='center-title'>
    <!-- <transition appear
    name='roll'> -->
      <h1 class='title'>What are we going to do today?</h1>
    <!-- </transition> -->
  <div class='top-rect'></div>
                    <!-- <img class='header-image' :src='mainImageSrc'/> -->
    </div>
</template>

<script>
export default {
  name: 'Landing',
    props: {
    images: {
        type: Array,
            default() {
            return ['https://i.imgur.com/giQkHcC.jpg', 
            'https://i.imgur.com/pOfXLjw.jpg', 
            'https://i.imgur.com/kJ3G1tZ.jpg']
        }
      }
    },
    data: () => {
      return {
        mainImageSrc: null
    }
  },
    created () {
        setInterval(() => this.mainImageSrc = this.images[Math.floor(Math.random()*this.images.length)], 5000);
  }
}
</script>