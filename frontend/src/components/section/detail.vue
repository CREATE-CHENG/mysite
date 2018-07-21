<template>
  <b-col cols="8">
    <b-card :header="article.title">
      <p class="card-text">{{ article.content }}</p>
      <p class="card-text text-muted"><timeago :since="article.created_time" locale="zh-CN" class="text-muted"></timeago></p>
    </b-card>
    <br>
    <comment :comments="article.comments" :article_id='article.id'></comment>
  </b-col>
</template>

<script>
import comment from '@/components/section/comment'
import { getarticle } from '@/api/api'

export default {
  data () {
    return {
      article: [],
      article_id: ''
    }
  },
  created () {
    this.article_id = this.$route.params.id
    this.get_article()
  },
  components: {
    'comment': comment
  },
  methods: {
    get_article () {
      getarticle(this.article_id)
        .then((response) => {
          this.article = response.data
        })
    }
  }
}
</script>
