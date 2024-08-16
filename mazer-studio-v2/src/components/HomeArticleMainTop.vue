<script setup>
</script>

<template>
    <div class="article-container">
        <div class="article-text-container">
            <div class="article-title-text">
                {{ sourceData.title }}
                <div class="article-author-text"><i class="bi bi-person-circle"></i> {{ sourceData.author_email }} / {{ sourceData.publish_date.split('T')[0] }}</div>
            </div>
        </div>
        <div class="article-background-image">
            <img :src="serverUrl + sourceData.cover_url" alt="bkgimg" class="article-bkg-img">
        </div>
    </div>
</template>

<script>
export default {
    props: {
        sourceData: {
            auid: String,
            title: String,
            author_email: String,
            publish_date: String,
            cover_url: String,
            tags: {
                type: Object,
                default: []
            }
        }
    },
    data() {
        return {
            serverUrl: this.$server
        }
    }
}

</script>

<style scoped>
.article-container {
    cursor: pointer;
    width: 100%;
    min-height: 200px;
    position: relative;
    overflow: hidden;
    margin: 10px 0 10px 0px;
}

.article-container:hover .article-bkg-img{
    transform: scale(1.0);
}

.article-title-text {
    color: white;
    font-size: 30px;
    position: absolute;
    z-index: 999;
    bottom: 0;
    width: 100%;
    box-sizing: border-box;
    padding: 20px;
    font-weight: bolder;
    backdrop-filter: saturate(80%) blur(20px);
    transition-duration: 0.4s;
}

.article-title-text:hover {
    backdrop-filter: saturate(100%) blur(20px) brightness(150%);
}

.article-bkg-img {
    width: 100%;
    object-fit: cover;
    transform: scale(1.1);
    transition-duration: 0.8s;
}

.article-author-text {
    color: rgb(233, 233, 233);
    font-size: 20px;
    font-weight: lighter;
}
</style>