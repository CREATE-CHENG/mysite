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

export default {
  components: {
    'navbar': navbar,
    'asides': aside
  }
}
</script>
