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
            <div v-katex:display="'f(G(\\cdot)) = \\frac{1}{2}\\sum_{i=0}^{n}(y_i - \\omega_i)^2 = ||y_i||^2 + ||\\omega_i||^2 - 2y_i^T\\omega_i'"></div>     
            <div v-html="articleMain.text" class="main-text"></div>
        </div>
    </div>
    <CopyRight />
</template>

<script>
import axios from 'axios';
import katex from 'katex';
import 'katex/dist/katex.min.css';
import Clipboard from 'clipboard';

export default {
    data() {
        return {
            articleMain: {
                text: '<h3>Loading... Please Wait</h3>'
            },
            sourceData: this.$route.query
        }
    },
    methods: {
        async fetchText() {
            try {
                const response = await axios.get('http://localhost:5000/test/' + this.sourceData.id);
                this.articleMain.text = response.data.html;
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
                cpFormula.addEventListener('click', (e) => {
                    this.copyFormula(cpFormula.getAttribute("data"), e);
                    cpFormula.style = "background-color: green";
                    cpFormula.innerText = "Copied!"
                    setTimeout(() => {
                        cpFormula.style = "";
                        cpFormula.innerText = "Copy Formula"
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
        }
    },
    mounted() {
        this.fetchText();
    }
}
</script>

<style scoped>
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
}

.main-text {
    background-color: var(--bs-tertiary-bg);
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