<template>
  <b-col cols="8">
    <template v-for="article in list">
    <b-card :key="article.id">
      <b>{{ article.title }}</b>
      <hr>
      <p class="card-text">{{ article.desc }}</p>
      <router-link :to="{name:'article', params: { id: article.id }}" class="url">阅读全文</router-link>
      <hr>
      <timeago :since="article.created_time" locale="zh-CN" class="text-muted"></timeago>
      <span class="text-muted pull-right">
        <i class="fa fa-eye"> {{article.view}}</i>
        <i class="fa fa-comments"> {{article.comments.length}}</i>
      </span>
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
  mounted () {
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
      if (this.$route.params.name) {
        getlist({
          page: this.currentPage,
          category__name: this.$route.params.name
        }).then((response) => {
          var count = response.data.count
          if (count !== 0) {
            this.list = response.data.results
            this.totalrows = response.data.count
          } else {
            this.$router.push({ name: '404' })
          }
        })
        document.title = this.$route.params.name + ' - 何人也的博客'
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

