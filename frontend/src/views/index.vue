<template>
  <div>
    <navbar></navbar>
    <b-container id="container">
      <b-row>
        <router-view name="section"></router-view>
        <asides></asides>
      </b-row>
    </b-container>
    <foot></foot>
  </div>
</template>

<script>
import navbar from '../components/head/navbar'
import foot from '../components/foot/foot'
import aside from '../components/aside/aside'
import { getjwt } from '../api/api'
import { mapGetters } from 'vuex'

export default {
  components: {
    'navbar': navbar,
    'asides': aside,
    'foot': foot
  },
  computed: {
    ...mapGetters({
      user: 'user'
    })
  },
  created () {
    this.get_token()
    this.redirect()
  },
  methods: {
    get_token () {
      if (this.$cookies.get('csrftoken')) {
        if (!this.user.token) {
          getjwt(
            ).then((response) => {
              sessionStorage.setItem('token', response.data.token)
              sessionStorage.setItem('user', response.data.user.first_name)
              sessionStorage.setItem('avatar', response.data.user.social_auth.extra_data.profile_image_url)
              sessionStorage.setItem('permission', response.data.permission)
              this.$store.dispatch('setuser')
            })
        }
      }
    },
    redirect () {
      if (sessionStorage.getItem('redirect_url')) {
        var redirect = sessionStorage.getItem('redirect_url')
        sessionStorage.removeItem('redirect_url')
        this.$router.push(redirect)
      }
    }
  }
}
</script>
<style>
#container{
    padding-bottom: 60px;
    padding-top: 40px;
}
</style>
