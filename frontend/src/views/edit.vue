<template>
<div>
  <navbar></navbar>
  <b-container id="container">
    <b-form @submit="onSubmit" @reset="onReset">
      <b-form-group label="标题：">
        <b-form-input type="text" v-model="title" required placeholder="输入标题">
        </b-form-input>
      </b-form-group>
      <b-form-group label="文章描述：">
        <b-form-input type="text" v-model="desc" required placeholder="输入描述">
        </b-form-input>
      </b-form-group>
      <b-form-group label="类别：">
      <b-form-select v-model="selected" class="mb-3">
        <option :value="null">请选择类别</option>
        <option :value="category.id" v-for="category in categories">{{category.name}}</option>
      </b-form-select>
      </b-form-group>
      <mavon-editor @imgAdd="$imgAdd" v-model="value" ref=md></mavon-editor>
      <br>
      <b-button type="submit" variant="default">发布文章</b-button>
      <b-button type="reset" variant="default">返回</b-button>
    </b-form>
  </b-container>
  <foot></foot>
</div>
</template>

<script>
import navbar from '../components/head/navbar'
import foot from '../components/foot/foot'
import { mavonEditor } from 'mavon-editor'
import 'mavon-editor/dist/css/index.css'
import { imageupload, addarticle, getcategories, checkpermission, getarticle, updatearticle } from '@/api/api'
import { mapGetters } from 'vuex'

export default {
  data () {
    return {
      title: '',
      value: '',
      desc: '',
      selected: null,
      categories: [],
      id: this.$route.params.id
    }
  },
  computed: {
    ...mapGetters({
      user: 'user'
    })
  },
  components: {
    mavonEditor,
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
    ).then((response) => {
      this.categories = response.data
    })
    if (this.id) {
      document.title = '文章编辑 - 何人也的博客'
      getarticle(this.id)
        .then(response => {
          const article = response.data
          this.title = article.title
          this.desc = article.desc
          this.value = article.content
          this.selected = article.category
        }).catch(err => {
          console.log(err)
          this.$router.push({ name: '404' })
        })
    } else {
      document.title = '添加文章 - 何人也的博客'
    }
  },
  methods: {
    // 绑定@imgAdd event
    $imgAdd (pos, $file) {
        // 第一步.将图片上传到服务器.
      const formdata = new FormData()
      formdata.append('image', $file)
      imageupload(formdata)
      .then((response) => {
        // 第二步.将返回的url替换到文本原位置![...](0) -> ![...](url)
        // $vm.$img2Url 详情见本页末尾
        this.$refs.md.$img2Url(pos, response.data.image)
      })
    },
    onSubmit (evt) {
      if (this.value) {
        const formData = new FormData()
        const markContent = this.markdown(this.value)
        formData.append('title', this.title)
        formData.append('desc', this.desc)
        formData.append('markdown_content', markContent)
        formData.append('content', this.value)
        if (this.selected) {
          formData.append('category', this.selected)
        } else {
          evt.preventDefault()
          alert('请选择分类！')
          return
        }
        if (this.id) {
          updatearticle(this.id, formData)
          .then((response) => {
            this.$router.push({name: 'article', params: { id: response.data.id }})
          })
          .catch((error) => {
            console.log(error.response.status)
          })
        } else {
          addarticle(formData)
          .then((response) => {
            this.$router.push({name: 'article', params: { id: response.data.id }})
          })
          .catch((error) => {
            console.log(error.response.status)
          })
        }
      } else {
        evt.preventDefault()
        alert('请输入文章内容。')
        this.$refs.md.textAreaFocus()
      }
      evt.preventDefault()
    },
    onReset () {
      this.$router.go(-1)
    },
    markdown (content) {
      return this.$refs.md.markdownIt.render(content)
    },
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
    }
  }
}
</script>
<style>
#container{
    padding-bottom: 60px;
    padding-top: 40px;
}
</style>

