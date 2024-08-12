<script setup>
import { RouterLink, RouterView } from 'vue-router'
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
            <a class="nav-link active" aria-current="page" href="#">Home</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">All Articles</a>
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
              <li><a class="dropdown-item" href="#"><span class="flag-icon flag-icon-cn"></span> 中文(简体)</a></li>
              <li><a class="dropdown-item" href="#"><span class="flag-icon flag-icon-us"></span> English(US)</a></li>
            </ul>
          </li>
          <li v-if="bNotHaveToken" class="nav-item">
            <button type="button" class="btn btn-primary" data-bs-toggle="modal"
              data-bs-target="#loginModel">Login</button>
          </li>
          <li v-else class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown"
              aria-expanded="false"><i class="bi bi-person-circle"></i></a>
            <ul class="dropdown-menu">
              <li><a class="dropdown-item" href="#" @click="enterView('editor')"><i class="bi bi-pen-fill"></i> Write
                  New Article</a></li>
              <li><a class="dropdown-item" href="#" @click="enterView('profile')"><i class="bi bi-person-square"></i> My
                  Profile</a></li>
              <li><a class="dropdown-item dropdown-danger" @click="logout()"><i class="bi bi-x-circle-fill"></i> Log
                  Out</a></li>
            </ul>
          </li>
          </li>
        </ul>
        <form class="d-flex" role="search">
          <input class="form-control me-2" type="search" placeholder="Search Articles" aria-label="Search">
          <button class="btn btn-outline-success" type="submit">Search</button>
        </form>
      </div>
    </div>
  </nav>


  <RouterView />

  <div class="modal fade" id="loginModel" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
    <div class="modal-dialog modal-dialog-centered">
      <div class="modal-content">
        <div class="modal-header">
          <h1 v-show="bLogin" class="modal-title fs-5 text-reset">Login</h1>
          <h1 v-show="!bLogin" class="modal-title fs-5 text-reset">Signup</h1>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <div v-show="!bLogin" class="form-floating mb-3">
            <input v-model="submitForm.usr" type="text" class="form-control" id="floatingUsr" placeholder="Username">
            <label for="floatingUsr">Username</label>
          </div>
          <div class="form-floating mb-3">
            <input v-model="submitForm.email" type="email" class="form-control" id="floatingInput"
              placeholder="Email address">
            <label for="floatingInput">Email address</label>
          </div>
          <div class="form-floating mb-3">
            <input v-model="submitForm.psw" type="password" class="form-control" id="floatingPassword"
              placeholder="Password">
            <label for="floatingPassword">Password</label>
          </div>
          <div v-show="bLogin" class="form-floating">
            <input v-model="submitForm.twofa" type="password" class="form-control" id="floating2FA"
              placeholder="2FA Passcode" disabled>
            <label for="floating2FA">2FA Passcode</label>
          </div>
          <div v-show="bLogin" class="form-text">No account? <span class="clickText"
              @click="switchLogin(false)">Signup</span> now.</div>
          <div v-show="!bLogin" class="form-text">Have an account? <span class="clickText"
              @click="switchLogin(true)">Login</span> now.</div>
        </div>
        <div v-show="bLogin" class="modal-footer">
          <button id="dismissModalBtn" type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
          <button type="button" class="btn btn-primary" @click="handleLog()">Login</button>
        </div>
        <div v-show="!bLogin" class="modal-footer">
          <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
          <button type="button" class="btn btn-primary" @click="handleReg()">Register</button>
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
          {{ lsMsg }}
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

const getPreferredTheme = () => {
  if (storedTheme) {
    return storedTheme
  }

  return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light'
}
storedTheme = getPreferredTheme()

const getSwitchTheme = () => {
  console.log(storedTheme)
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
      },
      lsMsg: 'Welcome! This website uses a small file, called \"LocalStorage\" to store some data. If you continue browsing, you will be deemed to agree to the use of LocalStorage.'
    }
  },
  methods: {
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
    },
    checkedLS() {
      localStorage.setItem('checkedLS', 'true');
    },
    logout() {
      localStorage.clear();
      this.bLogin = true;
      this.bNotHaveToken = true;
      this.showToast({
        text: "Log Out Successfully!",
        title: "Info",
        small: "Just Now"
      })
    },
    async handleReg() {
      try {
        await axios.post(this.$server + '/api/register', this.submitForm);
        this.showToast({
          text: 'Registration Successful.',
          title: 'Info',
          small: 'Just Now'
        })
      }
      catch (error) {
        this.showToast({
          text: error.response ? error.response.data.error : 'Registration failed',
          title: 'Error',
          small: 'Just Now'
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
          text: error.response ? error.response.data.error : 'Token expired, please re-login.',
          title: 'Error',
          small: 'Just Now'
        })
        setTimeout('this.logout()', 2000)
      }
    },
    async handleLog() {
      try {
        const res = await axios.post(this.$server + '/api/login', this.submitForm);
        this.showToast({
          text: 'Login Successful.',
          title: 'Info',
          small: 'Just Now'
        });
        this.submitForm.token = res.data.jwt;
        localStorage.setItem('jwt', res.data.jwt);
        this.bNotHaveToken = false;
        document.getElementById('dismissModalBtn').click();
      }
      catch (error) {
        this.showToast({
          text: error.response ? error.response.data.error : 'Login failed',
          title: 'Error',
          small: 'Just Now'
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
    setInterval(() => {
      this.testToken()
    }, 60000)
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
