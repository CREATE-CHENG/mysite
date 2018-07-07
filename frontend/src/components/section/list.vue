<template>
  <b-col cols="8">
    <template v-for="article in list">
    <b-card :header="article.title" :sub-title="article.context" :key="article.id">
        <p class="card-text">
            Some quick example text to build on the <em>card title</em> and make up the bulk of the card's content.
        </p>
        <a href="#"
           class="card-link">Card link</a>
    </b-card>
    <br :key="article.id">
    </template>
    <b-pagination size="md" align="right" :total-rows="totalrows" v-model="currentPage" :per-page="5">
    </b-pagination>
</b-col>
</template>

<script>
import { getlist } from '@/api/api'

export default {
  data () {
    return {
      list: [],
      currentPage: 1,
      totalrows: ''
    }
  },
  created () {
    this.getList()
  },
  watch: {
    '$route': function () {
      this.currentPage = 1
      this.getList()
    },
    'currentPage': 'getList'
  },
  methods: {
    getList () {
      if (this.$route.params.id) {
        getlist({
          page: this.currentPage,
          category__id: this.$route.params.id
        }).then((response) => {
          this.list = response.data.results
          this.totalrows = response.data.count
        })
      } else {
        getlist({
          page: this.currentPage
        }
        ).then((response) => {
          this.list = response.data.results
          this.totalrows = response.data.count
        })
      }
    }
  }
}
</script>
