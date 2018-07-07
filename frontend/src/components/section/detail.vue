<template>
  <b-col cols="8">
<b-card :header="article.title" :header-tag="header">
            <p class="card-text">{{ article.content }}</p>
            <p class="card-text">{{ article.created_time }}</p>
        </b-card>
        <br>
        <comment :comments="article.comments"></comment>
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
