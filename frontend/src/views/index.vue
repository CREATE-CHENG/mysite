<template>
<div>
    <navbar></navbar>
    <jumbotron></jumbotron>
    <b-container>
        <b-row>
            <list></list>
            <b-col></b-col>
        </b-row>
    </b-container>
</div>
</template>

<script>
import navbar from '../components/head/navbar'
import jumbotron from '../components/head/jumbotron'
import list from '../components/section/list'

export default {
  components: {
    'navbar': navbar,
    'jumbotron': jumbotron,
    'list': list
  }
}
</script>
