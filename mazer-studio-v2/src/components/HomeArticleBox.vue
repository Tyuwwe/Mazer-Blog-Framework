<script setup>
</script>

<template>
    <div class="article-container">
        <div class="article-background-image">
            <img :src="serverUrl + sourceData.cover_url" alt="bkgimg" class="article-bkg-img">
        </div>
        <div class="article-text-container">
            <div class="article-title-text">
                {{ sourceData.title }}
                <div class="article-author-text"><i class="bi bi-person-circle"></i> {{ sourceData.author_email }} / {{ sourceData.publish_date.split('T')[0] }}</div>
            </div>
        </div>
        <div class="article-background-color"></div>
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
    position: relative;
    margin: 10px 0 10px 0px;
    transition-duration: 0.4s;
}

.article-background-image {
    overflow: hidden;
    border-radius: 20px;
    min-height: 200px;
    max-height: 300px;
    transition-duration: 0.4s;
}

.article-background-color {
    background-color: var(--bs-secondary-bg);
    width: 100%;
    height: 100%;
    position: absolute;
    z-index: -1;
    top: 0;
    left: 0;
    transform: scaleY(0);
    border-radius: 20px;
    transition-duration: 0.4s;
}

.article-container:hover .article-background-color {
    transform: scaleY(1);
}

.article-container:hover .article-bkg-img {
    transform: scale(1.0);
}

.article-title-text {
    font-size: 25px;
    color: var(--primary-text-dark);
    bottom: 0%;
    width: 100%;
    box-sizing: border-box;
    padding: 10px;
    font-weight: bolder;
    transition-duration: 0.4s;
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