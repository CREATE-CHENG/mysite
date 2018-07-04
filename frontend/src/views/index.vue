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
import jumbotron from '../components/head/jumbotron'
import list from '../components/section/list'
import aside from '../components/aside/aside'

export default {
  components: {
    'navbar': navbar,
    'jumbotron': jumbotron,
    'list': list,
    'asides': aside
  },
  data () {
    return {
      items: [{
        text: 'Admin',
        href: '#'
      }, {
        text: 'Manage',
        href: '#'
      }, {
        text: 'Library',
        active: true
      }]
    }
  }
}
</script>
