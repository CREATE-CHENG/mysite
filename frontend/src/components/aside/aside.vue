<template>
  <b-col cols="4">
    <b-card header="分类">
<b-list-group>
  <b-list-group-item v-for="cat in categories" :key="cat.id" class="d-flex justify-content-between align-items-center">
    <router-link :to="'/category/'+cat.id">{{cat.name}}</router-link>
    <b-badge variant="dark" pill>{{cat.articles.length}}</b-badge>
  </b-list-group-item>
</b-list-group>
    </b-card>
    <br>
    <b-card header="吾"
            sub-title="何人也">
        <p class="card-text">
            Some quick example text to build on the <em>card title</em> and make up the bulk of the card's content.
        </p>
    </b-card>
  </b-col>
</template>

<script>
import {getcategories} from '@/api/api'
export default {
  data () {
    return {
      categories: []
    }
  },
  created () {
    getcategories(
    ).then((response) => {
      this.categories = response.data
    })
  }
}
</script>


