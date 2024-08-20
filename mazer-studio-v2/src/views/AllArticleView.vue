<script setup>
import CopyRight from '../components/CopyRight.vue'
</script>

<template>
    <div class="AllContainer">
        <div class="AllFilter mb-4 btn-group">
            <div class="dropdown-container">
                <div class="dropdown filter-dropdown">
                    <select @change="fetchArticle()" v-model="sortForm.lang" class="form-select" aria-label="LangSelect">
                        <option value="">{{ $t('all.all_lang') }}</option>
                        <option value="zh">中文（简体）</option>
                        <option value="en">English (US)</option>
                    </select>
                </div>
                <div class="dropdown filter-dropdown">
                    <select @change="sortArticle($event.target.value)" class="form-select" aria-label="SortSelect">
                        <option value="1" selected>{{ $t('all.newest') }}</option>
                        <option value="2">{{ $t('all.highestlikes') }}</option>
                        <option value="3">{{ $t('all.lastupdate') }}</option>
                    </select>
                </div>
            </div>
            <div class="input-group" style="display: flex; justify-content: end;">
                <input type="password" hidden>
                <input v-model="sortForm.keyword" class="form-control rounded-start filter-input" type="search" :placeholder="$t('all.filter_text')" autocomplete="new-password">
                <button @click="fetchArticle()" style="width: 80px;" class="btn btn-secondary" type="submit">{{ $t('all.filter') }}</button>
            </div>
        </div>
        <div v-for="art in arts" :key="art.auid"class="card mb-3 art-card" @click="enterArticle(art.auid)" style="width: 100%;">
            <div class="row g-0">
                <div class="col-md-4">
                    <img :src="serverUrl + art.cover_url" class="img-fluid rounded-start card-cover-img" alt="art_cover">
                </div>
                <div class="col-md-8">
                    <div class="card-body">
                        <h5 class="card-title">{{ art.title }}</h5>
                        <div class="card-tag-box mt-2 mb-2">
                            <div class="card-tags" v-for="tag in art.tags.split(', ')">{{ tag }}</div>
                        </div>
                        <p class="card-text mb-0"><small class="text-muted"><i class="bi bi-clock-fill"></i> {{ $t('all.published') }} {{ art.publish_date.split('T')[0] + ' ' + art.publish_date.split('T')[1].split('.')[0] }}</small></p>
                        <p class="card-text mb-0"><small class="text-muted"><i class="bi bi-clock-fill"></i> {{ $t('all.lastupdated') }} {{ art.update_date.split('T')[0] + ' ' + art.update_date.split('T')[1].split('.')[0] }}</small></p>
                        <p class="card-text mb-0"><small class="text-muted"><i class="bi bi-hand-thumbs-up-fill"></i> {{ $t('all.likes') }} {{ art.likes }}</small></p>
                        <p class="card-text"><small class="text-muted"><i class="bi bi-person-circle"></i> {{ $t('all.author') }} {{ art.author_email }}</small></p>
                    </div>
                </div>
            </div>
        </div>
        <div v-show="!arts.length > 0" class="nofilter">{{ $t('all.no_filter') }}</div>
        <CopyRight class="mt-5" />
    </div>
</template>

<script>
import axios from 'axios';

export default {
    data() {
        return {
            sortForm: {
                keyword: '',
                lang: ''
            },
            arts: {},
            serverUrl: this.$server
        }
    },
    methods: {
        async fetchArticle() {
            let res = await axios.post(this.$server + '/api/articles', this.sortForm);
            console.log(res)
            this.arts = res.data.arts
        },
        enterArticle(auid) {
            window.scroll(0, 0);
            this.$router.push({name: "article", query: {'auid': auid}})
        },
        sortArticle(sortType) {
            if (sortType == '1') {
                this.arts.sort((x, y) => {
                    const yTimeText = y.publish_date.split('.')[0].split('T')
                    const xTimeText = x.publish_date.split('.')[0].split('T')
                    const xTime = xTimeText[0] + ' ' + xTimeText[1]
                    const yTime = yTimeText[0] + ' ' + yTimeText[1]
                    return Date.parse(yTime) - Date.parse(xTime);
                })
            }
            else if (sortType == '2') {
                this.arts.sort((x, y) => {
                    return y.likes - x.likes;
                })
            }
            else if (sortType == '3') {
                this.arts.sort((x, y) => {
                    const yTimeText = y.update_date.split('.')[0].split('T')
                    const xTimeText = x.update_date.split('.')[0].split('T')
                    const xTime = xTimeText[0] + ' ' + xTimeText[1]
                    const yTime = yTimeText[0] + ' ' + yTimeText[1]
                    return Date.parse(yTime) - Date.parse(xTime);
                })
            }
        }

    },
    mounted() {
        this.fetchArticle()
    }
}
</script>

<style scoped>
.AllContainer {
    max-width: 1200px;
    min-width: 400px;
    width: 75%;
    margin: auto;
    margin-top: 100px;
    display: flex;
    flex-direction: column;
    align-items: center;
}

.AllFilter {
    width: 100%;
    display: flex;
    justify-content: space-between;
}

.dropdown-container {
    display: flex;
}

.card-title {
    font-weight: bolder;
    font-size: 1.5rem
}

.card-tag-box {
    display: flex;
    justify-content: start;
    align-items: center;
}

.card-tags {
    border-radius: 100px;
    margin-right: 5px;
    padding-left: 10px;
    padding-right: 10px;
    background-color: var(--bs-secondary-bg);
}

.art-card {
    cursor: pointer;
    transition-duration: 0.2s;
}

.art-card:hover {
    transform: scale(1.02);
}

.art-card:active {
    background-color: var(--bs-secondary-bg);
}

.nofilter {
    text-align: center;
    font-size: 1.2rem;
    font-weight: bolder;
}

.filter-dropdown {
    margin-right: 12px;
    min-width: 150px;
}

.card-cover-img {
    height: 100%;
    object-fit: cover;
}

@media only screen and (max-width: 767px) {
    .AllFilter { 
        flex-direction: column;
    }
    .filter-dropdown {
        flex: 1;
        margin-right: 0px;
        margin-bottom: 12px;
    } 
}
</style>