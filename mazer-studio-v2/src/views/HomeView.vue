<script setup>
import HomeArticleBox from '../components/HomeArticleBox.vue'
import CopyRight from '../components/CopyRight.vue'

</script>

<template>
  <main>
    <ul class="HomeBody-ul">
      <li class="HomeBody" v-for="sData in sourceDataList" :key="sData.id">
        <HomeArticleBox :sourceData="sData" @click="enterArticle(sData)" />
      </li>
    </ul>
    <CopyRight />
  </main>
</template>

<script>
export default {
  data() {
    return {
      sourceDataList: [
        {
          id: "1",
          title: "How to Install Windows 11",
          author: "Tyuwwe",
          date: "2024-7-26",
          imgUrl: "/static/example-img.jpg"
        },
        {
          id: "2",
          title: "Markdown Support Test Page",
          author: "Tyuwwe",
          date: "2024-7-26",
          imgUrl: "/static/wallhaven-x6yxpz.png"
        }
      ]

    }
  },
  methods: {
    enterArticle(sData) {
      this.$router.push({name: "article", query: sData})
    }
  }
}
</script>

<style>
.HomeBody {
  width: 65%;
  max-width: 800px;
  min-width: 350px;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  margin: 0;
  padding: 0;
}

.HomeBody-ul {
  padding: 0;
  padding-top: 100px;
  width: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
</style>
