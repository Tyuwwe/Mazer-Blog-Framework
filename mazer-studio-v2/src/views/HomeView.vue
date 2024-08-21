<script setup>
import HomeArticleBox from '../components/HomeArticleBox.vue'
import CopyRight from '../components/CopyRight.vue'

</script>

<template>
  <main>
    <ul class="HomeBody-ul">
      <li class="HomeBody" v-for="sData in sourceDataList" :key="sData.auid">
        <HomeArticleBox :sourceData="sData" @click="enterArticle(sData)" />
      </li>
      <li class="HomeBody" v-if="!sourceDataList.length">
        <div class="Info">{{ $t('home.noart') }}</div>
      </li>
    </ul>
    <CopyRight />
  </main>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      sourceDataList: {}
    }
  },
  methods: {
    enterArticle(sData) {
      window.scroll(0, 0);
      this.$router.push({ name: "article", query: { 'auid': sData.auid } })
    },
    async fetchArticle() {
      const res = axios.get(this.$server + '/api/articles/' + localStorage.getItem('lang'))
      res.then((value) => {
        // console.log(value)
        this.sourceDataList = value.data.arts
        // console.log(this.sourceDataList)
      })
    }
  },
  mounted() {
    this.fetchArticle()
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
