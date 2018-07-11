<template>
  <b-col cols="8">
    <template v-for="article in list">
    <b-card :key="article.id">
      <b>{{ article.title }}</b>
      <hr>
      <p class="card-text">{{ article.content }}</p>
      <router-link :to="{name:'detail', params: { id: article.id }}">阅读全文</router-link>
      <hr>
      <timeago :since="article.created_time" locale="zh-CN" class="text-muted"></timeago>
    </b-card>
    <br>
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
      totalrows: null
    }
  },
  created () {
    this.get_list()
  },
  watch: {
    '$route': function () {
      this.currentPage = 1
      this.get_list()
    },
    'currentPage': 'get_list'
  },
  methods: {
    get_list () {
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
