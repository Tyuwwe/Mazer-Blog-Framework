<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>

  <nav class="navbar fixed-top navbar-expand-lg">
    <div class="container-fluid">
      <a class="navbar-brand" href="./">
        <i class="bi bi-gpu-card"></i>
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
            <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#loginModel">Login</button>
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
          <h1 class="modal-title fs-5 text-reset">Login</h1>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <div class="form-floating mb-3">
          <input type="email" class="form-control" id="floatingInput" placeholder="name@example.com">
          <label for="floatingInput">Email address</label>
        </div>
        <div class="form-floating mb-3">
          <input type="password" class="form-control" id="floatingPassword" placeholder="Password">
          <label for="floatingPassword">Password</label>
        </div>
        <div class="form-floating">
          <input type="password" class="form-control" id="floating2FA" placeholder="2FA Passcode">
          <label for="floatingPassword">2FA Passcode</label>
        </div>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
          <button type="button" class="btn btn-primary">Login</button>
        </div>
      </div>
    </div>
  </div>


</template>

<script>
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
</style>
