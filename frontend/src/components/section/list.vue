<template>
  <b-col cols="8">
    <b-card v-for="article in list" :header="article.title" :sub-title="article.context" :key="article.id">
        <p class="card-text">
            Some quick example text to build on the <em>card title</em> and make up the bulk of the card's content.
        </p>
        <a href="#"
           class="card-link">Card link</a>
        <b-link href="#"
                class="card-link">Another link</b-link>
    </b-card>
    <br>
    <b-pagination size="md" align="right" :total-rows="100" v-model="currentPage" :per-page="10">
    </b-pagination>
</b-col>
</template>

<script>
import { getlist } from '@/api/api'

export default {
  data () {
    return {
      list: [],
      cat_id: ''
    }
  },
  created () {
    this.getList()
  },
  methods: {
    getList () {
      if (this.$route.params.id) {
        this.cat_id = this.$route.params.id
        getlist(
        ).then((response) => {
          console.log(this.$route.params.id)
          this.list = response.data
        })
      } else {
        getlist(
        ).then((response) => {
          console.log(response.data)
          this.list = response.data
        })
      }
    }
  }
}
</script>
