<template>
    <header class='main-image'>
        <div class='banner-container'>
            <button class='ghost button'>Log in</button>
            <button class='fill button'>Register</button>
                <h1 class='title'>What are we going to do today?</h1>
                    <img class='header-image' :src='mainImageSrc'/>
        </div>
    </header>
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