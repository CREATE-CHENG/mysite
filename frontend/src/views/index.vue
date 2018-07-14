<template>
<div>
    <navbar></navbar>
    <br>
    <b-container>
        <b-row>
            <router-view name="section"></router-view>
            <asides></asides>
        </b-row>
    </b-container>
</div>
</template>

<script>
import navbar from '../components/head/navbar'
import aside from '../components/aside/aside'
import { getjwt } from '../api/api'
import { mapGetters } from 'vuex'

export default {
  components: {
    'navbar': navbar,
    'asides': aside
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
      if (!this.user.token) {
        getjwt(
          ).then((response) => {
            sessionStorage.setItem('token', response.data.token)
            sessionStorage.setItem('user', response.data.user.username)
            sessionStorage.setItem('avatar', response.data.user.social_auth.extra_data.profile_image_url)
            this.$store.dispatch('setuser')
          }).catch((error) => {
            return error
          })
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
