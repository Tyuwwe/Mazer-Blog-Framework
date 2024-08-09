<script setup>
import CopyRight from '../components/CopyRight.vue'
</script>

<template>
    <div class="myProfile-container">
        <div class="myProfile-top">
            <div class="myAvatar">
                <img class="myAvatar-img" :src="userData.avt" alt="Avatar">
            </div>
            <div class="myProfile">
                <div class="myProfile-name">{{ userData.usr }}</div>
                <div class="myProfile-desc">{{ userData.usr_desc }}</div>
            </div>
            <div class="myProfileBtns">
                <button type="button" class="btn btn-primary"><i class="bi bi-pencil-square"></i> Edit</button>
            </div>
        </div>
        <div class="myProfile-bottom">
            <div class="myArticles">
                <div class="myArticles-title">My Articles</div>
                <div v-if="!articles.length" class="myArticles-content">No Available Record</div>
                <div v-for="article in articles" :key="article.id" class="myArticles-content">
                    <div class="article-left">
                        <div class="article-title">{{ article.title }}</div>
                        <div class="article-info">
                            <div class="article-likes"><i class="bi bi-suit-heart-fill"></i> {{ article.likes }}</div>
                            <div class="article-date"><i class="bi bi-calendar-date-fill"></i> {{ article.date }}</div>
                        </div>
                    </div>
                    <div class="article-btns">
                        <button type="button" class="btn btn-primary"
                                data-bs-toggle="tooltip" data-bs-placement="top"
                                data-bs-title="View Article">
                                <i class="bi bi-eye-fill"></i>
                        </button>
                        <button type="button" class="btn btn-secondary"
                                data-bs-toggle="tooltip" data-bs-placement="top"
                                data-bs-title="Edit Article">
                                <i class="bi bi-nut-fill"></i>
                        </button>
                        <button type="button" class="btn btn-danger"
                                data-bs-toggle="tooltip" data-bs-placement="top"
                                data-bs-title="Delete Article">
                                <i class="bi bi-trash3-fill"></i>
                        </button>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <CopyRight />
</template>

<script>
import axios from 'axios';
import { Tooltip } from 'bootstrap';

export default {
    data() {
        return {
            jwt: '',
            userData: {
                usr: "",
                usr_desc: "",
                email: "",
                avt: "/static/image/default.jpg",
            },
            articles: [
                {
                    id: 1,
                    title: "How to get Nobel Prize 2025?",
                    likes: 123,
                    date: "2025/1/1",
                    stat: 1
                },
                {
                    id: 2,
                    title: "How to write a Linux Kernel?",
                    likes: 124133,
                    date: "2025/12/31",
                    stat: 1
                },
                {
                    id: 3,
                    title: "How to go to Mars with 1 dollar?",
                    likes: 114514,
                    date: "2022/12/31",
                    stat: 0
                }
            ]
        }
    },
    methods: {
        async fetchUserData() {
            const response = await axios.get('http://localhost:5000/api/users', {
                headers: {
                    'Authorization': 'Bearer ' + this.jwt,
                },
            });
            this.userData = response.data;
        },
        enterView(vName) {
            this.$router.push({ name: vName })
        },
    },
    mounted() {
        this.jwt = localStorage.getItem('jwt')
        const tooltipTriggers = document.getElementsByClassName('article-btns');
        let tooltipTriggerList = []
        for (let tooltip_element of tooltipTriggers) {
            tooltipTriggerList.push(...(tooltip_element.childNodes))
        }
        [...tooltipTriggerList].map(tooltipTriggerEl => new Tooltip(tooltipTriggerEl))
        this.fetchUserData();
    }
}
</script>

<style scoped>
.myAvatar {
    width: 200px;
    height: 200px;
    overflow: hidden;
    border-radius: 1000px;
    flex-shrink: 0;
}

.myAvatar:hover {
    filter: brightness(0.9);
}

.myAvatar-img {
    width: 100%;
    object-fit: cover;
}

.myProfile-container {
    max-width: 1200px;
    min-width: 400px;
    width: 75%;
    margin: auto;
    margin-top: 100px;
    margin-bottom: 100px;
    display: flex;
    flex-direction: column;
}

.myProfile-top, .myProfile-bottom {
    box-sizing: border-box;
    padding: 20px;
    width: 100%;
    box-shadow: rgba(99, 99, 99, 0.2) 0px 2px 8px 0px;
    display: flex;
    justify-content: center;
    align-items: center;
}

.myProfile-bottom {
    margin-top: 20px;
    justify-content: space-between;
}

.myProfile-name {
    font-size: 2rem;
    font-weight: bolder;
}

.myProfile-desc {
    font-size: .85rem;
    font-weight: normal;
}

.myProfile {
    padding-left: 20px;
    flex: 1;
}

.myArticles {
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
}

.myArticles-title {
    font-size: 1.2rem;
    font-weight: bold;
    margin-bottom: 10px;
}

.myArticles-content {
    font-size: .75rem;
    display: flex;
    width: 100%;
    padding: 20px;
    border-radius: 10px;
    transition-duration: 0.1s;
    margin-top: 10px;
    box-shadow: var(--bs-tertiary-color) 0px 0px 5px 0px inset;
    border: 1px solid transparent;
}

.myArticles-content:hover {
    background-color: var(--bs-tertiary-bg);
    box-shadow: transparent 0px 0px 0px 0px;
    border: 1px solid transparent;
}

.myProfileBtns {
    padding: 10px;
}

.myArticles-content {
    display: flex;
    justify-content: center;
    align-items: center;
    box-sizing: border-box;
}

.article-title {
    font-size: 1.0rem;
    font-weight: normal;
}

.article-info {
    font-size: .75rem;
    color: var(--bs-secondary-color);
    display: flex;
}

.article-date, .article-likes {
    width: 80px;
    text-wrap: nowrap;
}


.article-date {
    margin-left: 5px;
}

.article-left {
    flex: 1;
}

.article-btns {
    flex-shrink: 0;
}

.article-btns button {
    margin-left: 10px;
}

@media only screen and (max-width: 750px) {
    .myProfile-top {
        flex-direction: column;
    }
}
</style>