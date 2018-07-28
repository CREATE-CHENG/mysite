<template>
<div>
  <navbar></navbar>
  <b-container id="container">
    <b-form @submit="onSubmit">
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
      <b-button type="submit" variant="default">发布新文章</b-button>
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
import { imageupload, addarticle, getcategories } from '@/api/api'
import { mapGetters } from 'vuex'

export default {
  data () {
    return {
      title: '',
      value: '',
      desc: '',
      selected: null,
      categories: []
    }
  },
  computed: {
    ...mapGetters({
      permission: 'permission'
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
  },
  methods: {
    // 绑定@imgAdd event
    $imgAdd (pos, $file) {
        // 第一步.将图片上传到服务器.
      var formdata = new FormData()
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
        var formdata = new FormData()
        var content = this.markdown(this.value)
        formdata.append('title', this.title)
        formdata.append('desc', this.desc)
        formdata.append('markdown_content', content)
        formdata.append('content', this.value)
        formdata.append('category', this.selected)
        addarticle(formdata)
        .then((response) => {
        })
        .catch((error) => {
          console.log(error.response.status)
        })
      } else {
        evt.preventDefault()
        alert('请输入文章内容。')
        this.$refs.md.textAreaFocus()
      }
      evt.preventDefault()
    },
    markdown (content) {
      return this.$refs.md.markdownIt.render(content)
    },
    check_permission () {
      if (this.permission === 0) {
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
.bs-footer {
    padding-top: 20px;
    padding-bottom: 10px;
    margin-top: 20px;
    color: #99979c;
    text-align: left;
    background-color: #ffffff;
}
</style>

