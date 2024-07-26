<script setup>
</script>

<template>
    <div class="article-container">
        <div class="article-text-container">
            <div class="article-title-text">
                {{ sourceData.title }}
                <div class="article-author-text"><i class="bi bi-person-circle"></i> {{ sourceData.author }} / {{ sourceData.date }}</div>
            </div>
        </div>
        <div class="article-background-image">
            <img :src="sourceData.imgUrl" alt="bkgimg" class="article-bkg-img">
        </div>
    </div>
</template>

<script>
export default {
    props: {
        sourceData: {
            id: Number,
            title: String,
            author: String,
            date: String,
            imgUrl: String,
            tags: {
                type: Object,
                default: []
            }
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

.article-container:hover .article-title-text{
    color: white;
    bottom: 0%;
}

.article-container:hover .article-bkg-img{
    transform: scale(1.0);
}

.article-title-text {
    font-size: 25px;
    color: rgba(0, 0, 0, 255);
    position: absolute;
    z-index: 999;
    bottom: -100%;
    width: 100%;
    box-sizing: border-box;
    padding: 10px;
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
    font-size: 15px;
    font-weight: lighter;
}
</style>