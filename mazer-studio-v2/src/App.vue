<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>

  <nav class="navbar fixed-top navbar-expand-lg" data-bs-theme="dark">
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
          <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown"
              aria-expanded="false"><i class="bi bi-globe"></i></a>
            <ul class="dropdown-menu">
              <li><a class="dropdown-item" href="#"><span class="flag-icon flag-icon-cn"></span> 中文(简体)</a></li>
              <li><a class="dropdown-item" href="#"><span class="flag-icon flag-icon-us"></span> English(US)</a></li>
            </ul>
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

</template>

<style scoped>
nav {
  width: 100%;
  padding: 20px 50px 20px 50px;
}

.navbar {
  background-color: #252a2fc4;
  backdrop-filter: saturate(20%) blur(12px);
}
</style>
