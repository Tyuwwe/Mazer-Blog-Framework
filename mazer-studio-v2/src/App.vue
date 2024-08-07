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
          <li class="nav-item">
            <a class="nav-link" @click="setTheme(getSwitchTheme())"><i class="bi bi-brightness-high-fill"></i></a>
          </li>
          <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown"
              aria-expanded="false"><i class="bi bi-globe"></i></a>
            <ul class="dropdown-menu">
              <li><a class="dropdown-item" href="#"><span class="flag-icon flag-icon-cn"></span> 中文(简体)</a></li>
              <li><a class="dropdown-item" href="#"><span class="flag-icon flag-icon-us"></span> English(US)</a></li>
            </ul>
          </li>
          <li class="nav-item">
            <button type="button" class="btn btn-primary" data-bs-toggle="modal"
              data-bs-target="#loginModel">Login</button>
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
          <div class="form-floating mb-3">
            <input v-model="submitForm.usr" type="email" class="form-control" id="floatingInput" placeholder="Email address">
            <label for="floatingInput">Email address</label>
          </div>
          <div class="form-floating mb-3">
            <input v-model="submitForm.psw" type="password" class="form-control" id="floatingPassword" placeholder="Password">
            <label for="floatingPassword">Password</label>
          </div>
          <div v-show="bLogin" class="form-floating">
            <input v-model="submitForm.twofa" type="password" class="form-control" id="floating2FA" placeholder="2FA Passcode" disabled>
            <label for="floating2FA">2FA Passcode</label>
          </div>
          <div v-show="bLogin" class="form-text">No account? <span class="clickText"
              @click="switchLogin(false)">Signup</span> now.</div>
          <div v-show="!bLogin" class="form-text">Have an account? <span class="clickText"
              @click="switchLogin(true)">Login</span> now.</div>
        </div>
        <div v-show="bLogin" class="modal-footer">
          <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
          <button type="button" class="btn btn-primary" @click="handleLog()">Login</button>
        </div>
        <div v-show="!bLogin" class="modal-footer">
          <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
          <button type="button" class="btn btn-primary" @click="handleReg()">Register</button>
        </div>
      </div>
    </div>
  </div>
  
  <div class="toast-container position-fixed top-0 start-50 translate-middle-x">
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
  console.log(theme)
}

setTheme(getPreferredTheme())

export default {
  data() {
    return {
      bLogin: true,
      submitForm: {
        usr: "",
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
      }
      catch (error) {
        this.showToast({
          text: error.response ? error.response.data.error : 'Login failed',
          title: 'Error',
          small: 'Just Now'
        })
        // console.log(error)
      }
    }
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
</style>
