<template>
  <div>
    <navbar></navbar>
    <b-container id="container">
      <b-card header="文章管理" header-tag="header">
        <b-list-group>
        <b-card>
          <span class="text-muted pull-left">
            <b-button variant="link" @click="toadd" class="text-muted">添加文章</b-button>
            <b-button variant="link" v-b-modal.modal1 class="text-muted">添加分类</b-button>
          </span>
        </b-card>
        <b-card :header="cat.name" v-for="cat in categories" :key="cat.id" class="my-card">
          <b-list-group-item v-for="article in cat.articles" :key="article.id">{{article.title}}
            <span class="text-muted pull-right">
              <b-button variant="link" @click="goedit(article.id)" class="text-muted">修改</b-button>
              <b-button variant="link" @click="setdelinfo(article.title, article.id)" class="text-muted" v-b-modal.modal2>删除</b-button>
            </span>
          </b-list-group-item>
          <b-list-group-item>
            <span class="text-muted">
              <b-button v-b-modal.modal3 variant="link" @click="setcat(cat.id)" @shown="clearName" class="text-muted">修改分类名</b-button>
            </span>
          </b-list-group-item>
        </b-card>
        </b-list-group>
      </b-card>
      <b-modal id="modal1" ref="modal1" centered title="添加分类" @ok="handleOk" @shown="clearName">
        <form>
          <b-form-input type="text" placeholder="输入分类名"  v-model="name"></b-form-input>
        </form>
      </b-modal>
      <b-modal id="modal2" centered @ok="handleDel" ref="modal2">
        确认删除文章： {{article}} ?
      </b-modal>
      <b-modal id="modal3" centered title="修改分类名" @ok="handleUpdate" ref="modal3">
        <form>
          <b-form-input type="text" v-model="name"></b-form-input>
        </form>
      </b-modal>
    </b-container>
    <foot></foot>
  </div>
</template>

<script>
import navbar from '../components/head/navbar'
import foot from '../components/foot/foot'
import { getcategories, addcat, checkpermission, delarticle, updatecat } from '@/api/api'
import { mapGetters } from 'vuex'

export default {
  data () {
    return {
      categories: [],
      name: '',
      article: '',
      id: null,
      catid: null
    }
  },
  computed: {
    ...mapGetters({
      user: 'user'
    })
  },
  components: {
    'navbar': navbar,
    'foot': foot
  },
  beforeCreate () {
    this.$nextTick(function () {
      this.check_permission()
    })
  },
  created () {
    getcategories(
    ).then(response => {
      this.categories = response.data
    })
  },
  mounted () {
    document.title = '管理 - 何人也的博客'
  },
  methods: {
    check_permission () {
      if (this.user.permission) {
        checkpermission()
          .then(response => {
          }).catch(error => {
            console.log(error)
            this.$router.push({ name: '404' })
          }
        )
      } else {
        this.$router.push({ name: '404' })
      }
    },
    toadd () {
      this.$router.push({name: 'new'})
    },
    handleOk (evt) {
      evt.preventDefault()
      if (!this.name) {
        alert('请输入分类名！')
      } else {
        addcat({name: this.name})
        this.$refs.modal1.hide()
        alert('添加成功！')
        this.$router.go(0)
      }
    },
    clearName () {
      this.name = ''
    },
    setdelinfo (article, id) {
      this.article = article
      this.id = id
    },
    handleDel () {
      delarticle(this.id)
      this.id = null
      this.article = ''
      this.$router.go(0)
    },
    setcat (id) {
      this.catid = id
    },
    goedit (id) {
      this.$router.push({name: 'update', params: { id: id }})
    },
    handleUpdate (evt) {
      evt.preventDefault()
      if (!this.name) {
        alert('请输入分类名！')
      } else {
        updatecat(this.catid, {name: this.name})
          .then(response => {
            alert('修改成功！')
            this.$router.go(0)
          })
          .catch(err => {
            alert(err.response.data.name[0])
            this.name = ''
          })
      }
    }
  }
}
// todo 文章管理，分类修改功能
</script>

<style>
#container{
    padding-bottom: 60px;
    padding-top: 40px;
}
.my-card {
    padding-bottom: 10px;
    margin-top: 20px;
}
</style>
