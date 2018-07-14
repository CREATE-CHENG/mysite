<template>
<b-navbar toggleable="md" type="dark" variant="dark">
  <b-container>
  <b-navbar-toggle target="nav_collapse"></b-navbar-toggle>

  <b-navbar-brand href="#">#</b-navbar-brand>

  <b-collapse is-nav id="nav_collapse">

    <b-navbar-nav>
      <b-nav-item href="/">首页</b-nav-item>
      <b-nav-item href="/archive">归档</b-nav-item>
      <b-nav-form>
        <b-form-input size="sm" class="mr-sm-2" type="text" placeholder="Search"/>
        <b-button size="sm" class="my-2 my-sm-0" type="submit">Search</b-button>
      </b-nav-form>
    </b-navbar-nav>
    <!-- Right aligned nav items -->
    <b-navbar-nav class="ml-auto">
      <b-nav-item-dropdown :text="this.$store.state.user.username" right v-if="this.$store.state.user.username">
        <b-dropdown-item @click="logout">登出</b-dropdown-item>
      </b-nav-item-dropdown>
      <b-nav-item href="http://127.0.0.1:8000/login/weibo/" v-else @click="set_redirect_url">登录</b-nav-item>
    </b-navbar-nav>

  </b-collapse>
  </b-container>
</b-navbar>
</template>

<script>
import { logout } from '../../api/api'

export default {
  methods: {
    set_redirect_url () {
      sessionStorage.setItem('redirect_url', this.$route.path)
    },
    logout () {
      sessionStorage.clear()
      this.set_redirect_url()
      this.$cookies.remove('csrftoken')
      logout()
      this.$router.push('/')
    }
  }
}
</script>
