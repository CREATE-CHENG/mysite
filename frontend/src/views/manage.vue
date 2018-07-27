<template>
  <div>
    <navbar></navbar>
    <b-container id="container">
        <b-card header="文章管理" header-tag="header">
          <b-list-group>
          <b-card>
            <span class="text-muted pull-left">
              <b-button variant="link" @click="" class="text-muted">添加文章</b-button>
              <b-button variant="link" @click="" class="text-muted">添加分类</b-button>
            </span>
          </b-card>
          <b-card :header="cat.name" v-for="cat in categories" :key="cat.id" class="my-card">
            <b-list-group-item v-for="article in cat.articles" :key="article.id">{{article.title}}
              <span class="text-muted pull-right">
                <b-button variant="link" @click="" class="text-muted">修改</b-button>
                <b-button variant="link" @click="" class="text-muted">删除</b-button>
              </span>
            </b-list-group-item>
            <b-list-group-item>
              <span class="text-muted">
                <b-button variant="link" @click="" class="text-muted">修改分类名</b-button>
              </span>
            </b-list-group-item>
          </b-card>
          </b-list-group>
        </b-card>
    </b-container>
    <foot></foot>
  </div>
</template>

<script>
import navbar from '../components/head/navbar'
import foot from '../components/foot/foot'
import {getcategories} from '@/api/api'

export default {
  data () {
    return {
      categories: []
    }
  },
  components: {
    'navbar': navbar,
    'foot': foot
  },
  created () {
    getcategories(
    ).then((response) => {
      this.categories = response.data
    })
  }
}
</script>

<style>
#container{
    padding-bottom: 60px;
    padding-top: 40px;
}
.bs-footer {
    padding-top: 20px;
    padding-bottom: 10px;
    margin-top: 20px;
    color: #99979c;
    text-align: left;
    background-color: #ffffff;
}
.my-card {
    padding-bottom: 10px;
    margin-top: 20px;
}
</style>

