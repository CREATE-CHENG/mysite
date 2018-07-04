<template>
  <b-col cols="4">
    <b-card header="分类">
<b-list-group>
  <b-list-group-item v-for="cat in categories" :key="cat.id">
    <router-link :to="'/category/'+cat.id">{{cat.name}}</router-link>
  </b-list-group-item>
</b-list-group>
    </b-card>
    <br>
    <b-card header="Card title"
            sub-title="Card subtitle">
        <p class="card-text">
            Some quick example text to build on the <em>card title</em> and make up the bulk of the card's content.
        </p>
        <a href="#"
           class="card-link">Card link</a>
        <b-link href="#"
                class="card-link">Another link</b-link>
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


