<template>
  <b-col cols="8">
    <b-card no-body>
      <b-tabs card>
        <b-tab title="归档">
        <template v-for="(articles, date) in list">
          <b-card :header="date" no-body>
            <b-list-group flush>
              <b-list-group-item :href="/article/ + article.id" :key="article.id" v-for="article in articles">{{ article.title }}</b-list-group-item>
            </b-list-group>
          </b-card>
          <br>
          </template>
        </b-tab>
      </b-tabs>
    </b-card>
  </b-col>
</template>

<script>
import { getarchive } from '@/api/api'

export default {
  data () {
    return {
      list: []
    }
  },
  created () {
    this.get_archive()
    document.title = '归档 - 何人也的博客'
  },
  methods: {
    get_archive () {
      getarchive()
        .then((response) => {
          this.list = response.data
        })
    }
  }
}
</script>

