<script setup>
import { RouterLink, RouterView } from 'vue-router'
import { useI18n, createI18n } from 'vue-i18n';
const { t, locale } = useI18n({ inheritLocale: true, useScope: 'local' });

</script>

<template>

  <nav class="navbar fixed-top navbar-expand-lg">
    <div class="container-fluid">
      <a class="navbar-brand" href="./">
        <i class="bi bi-opencollective"></i>
        Mazer Studio
      </a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarTogglerDemo02"
        aria-controls="navbarTogglerDemo02" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarTogglerDemo02">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <li class="nav-item">
            <a class="nav-link active" aria-current="page" @click="this.$router.push({ name: 'home' })" href="#">{{ $t('topbar.home') }}</a>
          </li>
          <li class="nav-item">
            <a class="nav-link active" @click="this.$router.push({ name: 'all' })" href="#">{{ $t('topbar.all') }}</a>
          </li>
          <li class="nav-item nav-flex">
          <li class="nav-item">
            <a class="nav-link" @click="setTheme(getSwitchTheme())"><i id="themeIco"
                class="bi bi-brightness-high-fill"></i></a>
          </li>
          <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown"
              aria-expanded="false"><i class="bi bi-translate"></i></a>
            <ul class="dropdown-menu">
              <li><a class="dropdown-item" @click="setLang('zh')" href="#"><span class="flag-icon flag-icon-cn"></span> 中文(简体)</a></li>
              <li><a class="dropdown-item" @click="setLang('en')" href="#"><span class="flag-icon flag-icon-us"></span> English(US)</a></li>
            </ul>
          </li>
          <li v-if="bNotHaveToken" class="nav-item">
            <button type="button" class="btn btn-primary" data-bs-toggle="modal"
              data-bs-target="#loginModel">{{ $t('topbar.login') }}</button>
          </li>
          <li v-else class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown"
              aria-expanded="false"><i class="bi bi-person-circle"></i></a>
            <ul class="dropdown-menu">
              <li><a class="dropdown-item" href="#" @click="enterView('editor')"><i class="bi bi-pen-fill"></i>
                  {{ $t('topbar.write') }}</a></li>
              <li><a class="dropdown-item" href="#" @click="enterView('profile')"><i class="bi bi-person-square"></i>
                  {{ $t('topbar.my') }}</a></li>
              <li><a class="dropdown-item dropdown-danger" @click="logout()"><i class="bi bi-x-circle-fill"></i>
                  {{ $t('topbar.logout') }}</a></li>
            </ul>
          </li>
          </li>
        </ul>
        <form class="d-flex" role="search">
          <input class="form-control me-2" type="search" :placeholder="$t('topbar.search_text')" aria-label="Search">
          <button style="width: 80px;" class="btn btn-outline-success" type="submit">{{ $t('topbar.search') }}</button>
        </form>
      </div>
    </div>
  </nav>

  <RouterView />

  <div class="modal fade" id="loginModel" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
    <div class="modal-dialog modal-dialog-centered">
      <div class="modal-content">
        <div class="modal-header">
          <h1 v-show="bLogin" class="modal-title fs-5 text-reset">{{ $t('topbar.login') }}</h1>
          <h1 v-show="!bLogin" class="modal-title fs-5 text-reset">{{ $t('topbar.signup') }}</h1>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <div v-show="!bLogin" class="form-floating mb-3">
            <input v-model="submitForm.usr" type="text" class="form-control" id="floatingUsr" placeholder="Username">
            <label for="floatingUsr">{{ $t('topbar.username') }}</label>
          </div>
          <div class="form-floating mb-3">
            <input v-model="submitForm.email" type="email" class="form-control" id="floatingInput"
              placeholder="">
            <label for="floatingInput">{{ $t('topbar.email') }}</label>
          </div>
          <div class="form-floating mb-3">
            <input v-model="submitForm.psw" type="password" class="form-control" id="floatingPassword"
              placeholder="">
            <label for="floatingPassword">{{ $t('topbar.password') }}</label>
          </div>
          <div v-show="bLogin" class="form-floating mb-3">
            <input v-model="submitForm.twofa" type="password" class="form-control" id="floating2FA"
              placeholder="" disabled>
            <label for="floating2FA">{{ $t('topbar.twofa') }}</label>
          </div>
          <div v-show="bLogin">
            <i18n-t keypath="topbar.noaccount" tag="div" class="form-text">
              <template v-slot:reg>
                <span class="clickText" @click="switchLogin(false)">{{ $t('topbar.signup') }}</span>
              </template>
            </i18n-t>
          </div>
          <div v-show="!bLogin">
            <i18n-t keypath="topbar.havaccount" tag="div" class="form-text">
              <template v-slot:log>
                <span class="clickText" @click="switchLogin(true)">{{ $t('topbar.login') }}</span>
              </template>
            </i18n-t>
          </div>
        </div>
        <div v-show="bLogin" class="modal-footer">
          <button type="button" class="btn btn-primary" @click="handleLog()">{{ $t('topbar.login') }}</button>
          <button id="dismissModalBtn" type="button" class="btn btn-secondary" data-bs-dismiss="modal">{{ $t('topbar.close') }}</button>
        </div>
        <div v-show="!bLogin" class="modal-footer">
          <button type="button" class="btn btn-primary" @click="handleReg()">{{ $t('topbar.signup') }}</button>
          <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">{{ $t('topbar.close') }}</button>
        </div>
      </div>
    </div>
  </div>

  <div class="toast-container position-fixed mt-3 top-0 start-50 translate-middle-x">
    <div id="liveToast" class="toast" role="alert" aria-live="assertive" aria-atomic="true">
      <div class="toast-header">
        <i class="bi bi-info-circle me-2"></i>
        <strong class="me-auto">{{ toastMsg.title }}</strong>
        <small>{{ toastMsg.small }}</small>
        <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Close"></button>
      </div>
      <div class="toast-body">
        {{ toastMsg.text }}
      </div>
    </div>
  </div>

  <div class="toast-container position-fixed mb-3 bottom-0 start-50 translate-middle-x">
    <div id="liveToastLocalStorage" class="toast align-items-center text-bg-primary border-0" role="alert"
      aria-live="assertive" aria-atomic="true" data-bs-autohide="false" style="width: 100%;">
      <div class="d-flex">
        <div class="toast-body">
          {{ $t('topbar.ls_msg') }}
        </div>
        <button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast" aria-label="Close"
          @click="checkedLS()"></button>
      </div>
    </div>
  </div>


</template>

<script>
import axios from 'axios';
import { Toast } from 'bootstrap';

let storedTheme = localStorage.getItem('theme')

const i18n = createI18n({})

const getPreferredTheme = () => {
  if (storedTheme) {
    return storedTheme
  }

  return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light'
}
storedTheme = getPreferredTheme()

const getSwitchTheme = () => {
  // console.log(storedTheme)
  return storedTheme == 'light' ? 'dark' : 'light'
}

const setTheme = function (theme) {
  document.documentElement.setAttribute('data-bs-theme', theme)
  storedTheme = theme
  localStorage.setItem('theme', storedTheme)
  if (theme == 'dark') {
    document.getElementById('themeIco').setAttribute('class', 'bi bi-brightness-high-fill')
  }
  else {
    document.getElementById('themeIco').setAttribute('class', 'bi bi-moon-fill')
  }
}

export default {
  data() {
    return {
      lang: "",
      bLogin: true,
      bNotHaveToken: true,
      submitForm: {
        usr: "",
        email: "",
        psw: "",
        twofa: "",
        token: ""
      },
      toastMsg: {
        text: 'message',
        title: 'title',
        small: 'small'
      }
    }
  },
  methods: {
    setLang(lang) {
      localStorage.setItem('lang', lang)
      // console.log(location.pathname)
      if (location.pathname == '/article') {
        this.$router.push({ path: '/' })
        setTimeout(() => {
          location.reload()
        }, 0)
      }
      else {
        location.reload()
      }
    },
    initPage() {
      this.submitForm.token = localStorage.getItem('jwt');
    },
    switchLogin(loginType) {
      this.bLogin = loginType
    },
    showToast(toastMessage) {
      this.toastMsg = toastMessage;
      const toastLive = document.getElementById('liveToast');
      const toastBootstrap = Toast.getOrCreateInstance(toastLive);
      toastBootstrap.show();
    },
    showToastLS() {
      const toastLive = document.getElementById('liveToastLocalStorage');
      const toastBootstrap = Toast.getOrCreateInstance(toastLive);
      toastBootstrap.show();
    },
    enterView(vName) {
      this.$router.push({ name: vName })
      if (vName = 'editor') {
        localStorage.setItem('editingArt', 'none')
      }
    },
    checkedLS() {
      localStorage.setItem('checkedLS', 'true');
    },
    logout() {
      localStorage.clear();
      this.bLogin = true;
      this.bNotHaveToken = true;
      this.showToast({
        text: this.$t('msg.logout_text'),
        title: this.$t('msg.msg_info'),
        small: this.$t('msg.msg_justnow')
      })
    },
    async handleReg() {
      try {
        await axios.post(this.$server + '/api/register', this.submitForm);
        this.showToast({
          text: this.$t('msg.reg_text'),
          title: this.$t('msg.msg_info'),
          small: this.$t('msg.msg_justnow')
        })
      }
      catch (error) {
        this.showToast({
          text: error.response ? error.response.data.error : this.$t('msg.reg_text_err'),
          title: this.$t('msg.msg_error'),
          small: this.$t('msg.msg_justnow')
        })
        // console.log(error)
      }
    },
    async testToken() {
      try {
        const res = await axios.get(this.$server + '/api/tokentest', {
          headers: {
            'Authorization': 'Bearer ' + localStorage.getItem('jwt'),
          },
        })
      }
      catch (error) {
        this.showToast({
          text: error.response ? error.response.data.error : this.$t('msg.tok_text_err'),
          title: this.$t('msg.msg_error'),
          small: this.$t('msg.msg_justnow')
        })
        setTimeout(() => {
          this.logout()
        }, 2000)
      }
    },
    async handleLog() {
      try {
        const res = await axios.post(this.$server + '/api/login', this.submitForm);
        this.showToast({
          text: this.$t('msg.log_text'),
          title: this.$t('msg.msg_info'),
          small: this.$t('msg.msg_justnow')
        });
        this.submitForm.token = res.data.jwt;
        localStorage.setItem('jwt', res.data.jwt);
        localStorage.setItem('email', res.data.email);
        this.bNotHaveToken = false;
        document.getElementById('dismissModalBtn').click();
      }
      catch (error) {
        this.showToast({
          text: error.response ? error.response.data.error : this.$t('msg.log_text_err'),
          title: this.$t('msg.msg_error'),
          small: this.$t('msg.msg_justnow')
        })
        // console.log(error)
      }
    },
    firstLaunch() {
      localStorage.setItem('lang', 'zh');
      this.lang = 'zh';
    }
  },
  mounted() {
    if (localStorage.getItem('jwt')) {
      this.bNotHaveToken = false;
      this.testToken()
      setInterval(() => {
        this.testToken()
      }, 60000)
    }
    else {
      this.bNotHaveToken = true;
    }
    if (localStorage.getItem('lang')) {
      this.lang = localStorage.getItem('lang');
    }
    else {
      this.firstLaunch();
    }
    if (!localStorage.getItem('checkedLS')) {
      this.showToastLS()
    }
    setTheme(getPreferredTheme())
  }
}



</script>

<style scoped>
nav {
  width: 100%;
  padding: 20px 50px 20px 50px;
}

.navbar {
  transition: background-color 0.2s;
  background-color: var(--bs-body-bg);
  box-shadow: var(--bs-tertiary-color) 0px 1px 1px;
}

.nav-link {
  cursor: pointer;
}

.clickText {
  color: var(--bs-primary);
  cursor: pointer;
}

.clickText:hover {
  opacity: 0.5;
}

.dropdown-danger {
  background-color: var(--bs-danger);
  color: white;
  transition-duration: 0.2s;
  cursor: pointer;
}

.dropdown-danger:hover {
  background-color: #a82733;
  color: white;
}

.nav-flex {
  display: flex;
}

@media only screen and (max-width: 991px) {
  .nav-flex .nav-item {
    margin-right: 20px;
  }
}
</style>
