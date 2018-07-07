<template>
<b-navbar toggleable="md" type="dark" variant="dark">
  <b-container>
  <b-navbar-toggle target="nav_collapse"></b-navbar-toggle>

  <b-navbar-brand href="#">#</b-navbar-brand>

  <b-collapse is-nav id="nav_collapse">

    <b-navbar-nav>
      <b-nav-item href="/">首页</b-nav-item>
      <b-nav-item href='/archive'>归档</b-nav-item>
    </b-navbar-nav>
    <!-- Right aligned nav items -->
    <b-navbar-nav class="ml-auto">

      <b-nav-form>
        <b-form-input size="sm" class="mr-sm-2" type="text" placeholder="Search"/>
        <b-button size="sm" class="my-2 my-sm-0" type="submit">Search</b-button>
      </b-nav-form>

    </b-navbar-nav>

  </b-collapse>
  </b-container>
</b-navbar>
</template>
