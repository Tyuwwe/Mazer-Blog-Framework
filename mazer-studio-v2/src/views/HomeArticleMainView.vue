<script setup>
import HomeArticleMainTop from '../components/HomeArticleMainTop.vue'
import CopyRight from '../components/CopyRight.vue'
import Prism from "prismjs"
</script>

<template>
    <div class="HomeArticleContainer">
        <div class="HomeArticleContainerBox">
            <div class="topImg">
                <HomeArticleMainTop :sourceData="sourceData" />
            </div>       
            <div v-html="articleMain.text" class="main-text"></div>
            <div class="ArticleBottomBox">
                <div class="bottomLeft">
                    <div class="likes">
                        <i @click="likeArt()" class="bi bi-hand-thumbs-up-fill"></i>
                        <div class="likesNum">{{ sourceData.likes }}</div>
                    </div>
                </div>
                <div class="bottomRight">
                    <div class="shares">
                        <i id="qq" class="bi bi-tencent-qq"></i>
                        <i id="wechat" class="bi bi-wechat"></i>
                        <i id="weibo" class="bi bi-sina-weibo"></i>
                        <i id="twitter" class="bi bi-twitter"></i>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <div class="toast-container position-fixed bottom-0 end-0 p-3">
        <div id="liveToast" class="toast" role="alert" aria-live="assertive" aria-atomic="true">
            <div class="d-flex">
                <div class="toast-body">
                    {{ infoText }}
                </div>
                <button type="button" class="btn-close me-2 m-auto" data-bs-dismiss="toast" aria-label="Close"></button>
            </div>
        </div>
    </div>
    <CopyRight />
</template>

<script>
import axios from 'axios';
import katex from 'katex';
import 'katex/dist/katex.min.css';
import Clipboard from 'clipboard';
import { Toast } from 'bootstrap';

let bCanLike = true

export default {
    data() {
        return {
            articleMain: {
                text: '<h3>Loading... Please Wait</h3>'
            },
            auid: this.$route.query.auid,
            sourceData: {
                publish_date: ''
            },
            infoText: ''
        }
    },
    methods: {
        showToast(text) {
            const toastLiveExample = document.getElementById('liveToast')
            const toast = new Toast(toastLiveExample)
            this.infoText = text
            toast.show()
        },
        async likeArt() {
            if (!bCanLike) return;
            bCanLike = false;
            try {
                await axios.put(this.$server + '/api/like', {auid: this.auid});
                this.sourceData.likes += 1;
                setTimeout(() => {
                    bCanLike = true;
                }, 10000)
            } catch (error) {
                console.error('Error like:', error);
            }
        },
        async fetchText() {
            try {
                const response = await axios.get(this.$server + '/api/article/' + this.$route.query.auid);
                this.articleMain.text = response.data.data.art_html;
                this.sourceData = response.data.data.art_meta
                // console.log(response)
                setTimeout(() => {
                    Prism.highlightAll();
                    this.loadMath();
                    this.addCpEvent();
                }, 500)
            } catch (error) {
                console.error('Error fetching text:', error);
            }
        },
        loadMath() {
            let mathFormulas = document.getElementsByClassName("math")
            for (let mathFormula of mathFormulas) {
                katex.render(mathFormula.innerText, mathFormula, {});
            }
        },
        addCpEvent() {
            let cpFormulas = document.getElementsByClassName("cp-formula")
            for (let cpFormula of cpFormulas) {
                cpFormula.innerText = this.$t('art.cp_formula')
                cpFormula.addEventListener('click', (e) => {
                    this.copyFormula(cpFormula.getAttribute("data"), e);
                    cpFormula.style = "background-color: green";
                    cpFormula.innerText = this.$t('art.cpd_formula')
                    setTimeout(() => {
                        cpFormula.style = "";
                        cpFormula.innerText = this.$t('art.cp_formula')
                    }, 2000)
                })
            }
        },
        copyFormula(text, event) {
            const cb = new Clipboard('.t', {
                text: () => text
            })
            cb.on('success', (e) => {
                cb.off('error')
                cb.off('success')
            })
            cb.on('error', (e) => {
                cb.off('error')
                cb.off('success')
            })
            cb.onClick(event)
        },
        initSharelink() {
            const qq = document.getElementById('qq');
            const wechat = document.getElementById('wechat');
            const weibo = document.getElementById('weibo');
            const twitter = document.getElementById('twitter');

            qq.addEventListener('click', () => {
                window.open('http://connect.qq.com/widget/shareqq/index.html?url=' + location.href + '&sharesource=qzone&title=' + this.sourceData.title + '&desc=MazerStudio')
            })

            for (let ele of [wechat, weibo, twitter]) {
                ele.addEventListener('click', (e) => {
                    this.copyFormula(location.href, e)
                    this.showToast(this.$t('art.share_cp'))
                })
            }
        }
    },
    mounted() {
        this.fetchText();
        this.initSharelink();
    }
}
</script>

<style scoped>
@keyframes swing {
    0% {transform: rotate(0deg) scale(1);}
    25% {transform: rotate(-15deg);}
    50% {transform: rotate(15deg) scale(1.1);}
    75% {transform: rotate(-15deg);}
    100% {transform: rotate(15deg) scale(1);}
}

@keyframes swingScale {
    0% {transform: rotate(0deg) scale(1.1);}
    25% {transform: rotate(-15deg) scale(1.1);}
    50% {transform: rotate(15deg) scale(1.1);}
    75% {transform: rotate(-15deg) scale(1.1);}
    100% {transform: rotate(15deg) scale(1.1);}
}

.likes, .shares {
    height: 40px;
    border-radius: 20px;
    padding: 10px;
    background-color: var(--bs-secondary-bg);
    display: flex;
    justify-content: space-around;
    align-items: center;
}

.likes i, .shares i {
    color: var(--primary-text-dark);
    width: 30px;
    height: 30px;
    border-radius: 15px;
    display: flex;
    justify-content: center;
    align-items: center;
    cursor: pointer;
    margin-left: 5px;
    margin-right: 5px;
    transition-duration: 0.1s;
}

.likes i {
    color: var(--primary-text-dark);
    margin-left: 0px;
    margin-right: 5px;
}

.likes i:hover, .shares i:hover {
    animation: swing 1s infinite;
    background-color: var(--bs-dark-bg-subtle);
}

.likes i:active, .shares i:active {
    background-color: var(--bs-secondary-color);
    color: var(--bs-secondary-bg);
    animation: swingScale 1s infinite;
}

.likesNum {
    margin-right: 5px;
}

.ArticleBottomBox {
    width: 100%;
    display: flex;
    justify-content: space-between;
    align-items: center;
    box-sizing: border-box;
    padding: 20px;
}

.HomeArticleContainer {
    width: 100%;
    color: var(--primary-text-dark);
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding: 0;
}

.HomeArticleContainerBox {
    width: 65%;
    max-width: 800px;
    min-width: 350px;
    margin-top: 100px;
    margin-bottom: 100px;
    background-color: var(--bs-tertiary-bg);
}

.main-text {
    padding: 20px;
    box-sizing: border-box;
    width: 100%;
    overflow-x: auto;
}

</style>

<style>
.main-text a {
    color: var(--bs-primary);
    filter: brightness(1.4);
}

.main-text a:hover {
    opacity: 0.5;
}

.main-text table {
    width: 100%;
    box-sizing: border-box;
    margin-top: 10px;
    margin-bottom: 10px;
    background-color: var(--bs-secondary-bg);
}

.main-text tr, 
.main-text td,
.main-text th  {
    border: rgb(170, 170, 170) 1px solid;
    padding: 5px;
}

.main-text img {
    width: 100%;
    object-fit: contain;
}

.math {
    max-width: 100%;
}

.inline-math {
    background-color: var(--bs-secondary-bg);
    padding: 5px;
    border-radius: 5px;
}

.block-math-container {
    width: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}

.block-math {
    text-align: center;
    padding-top: 10px;
}

.block-math-container:hover .cp-formula {
    opacity: 1;
}

.cp-formula {
    opacity: 0;
    transition: opacity 0.4s !important;
    z-index: 200;
    margin-top: 5px;
    margin-bottom: 10px;
}

.cp-formula:active {
    background-color: rgb(64, 68, 76) !important;
}
</style>