<template>
<div>
 <b-card header="评论" header-tag="header">
   <template v-for="comment in comments">
     <b-card>
       <b-media>
         <b-img slot="aside" width="50" alt="avatar" :src="comment.user.social_auth.extra_data.profile_image_url" />
         <h6 class="mt-0">{{comment.user.username}}</h6>
         <vue-markdown class="markdown-body">{{comment.content}}</vue-markdown>
         <p>
           <timeago :since="comment.created_time" locale="zh-CN" class="text-muted"></timeago>
           <b-button variant="link" @click="reply(comment.id, comment.user.username)" class="text-muted">回复</b-button>
         </p>
         <hr>
         <template v-for="child in comment.children">
         <b-media>
         <b-img slot="aside" width="50" alt="placeholder" :src="child.user.social_auth.extra_data.profile_image_url"/>
           <h6 class="mt-0">{{child.user.username}}</h6>
           <vue-markdown class="markdown-body">{{child.content}}</vue-markdown>
           <p>
             <timeago :since="child.created_time" locale="zh-CN" class="text-muted"></timeago>
             <b-button variant="link" @click="reply(comment.id)" class="text-muted">回复</b-button>
           </p>
         </b-media>
         <hr>
         </template>
       </b-media>
     </b-card>
   </template>
     <b-form @submit="onSubmit" @reset="onReset" v-show="this.user.token">
      <mavon-editor @imgAdd="$imgAdd" ref=md v-model="value" :placeholder="placeholder" :editable="editable"></mavon-editor>
      <br>
      <b-button type="submit" variant="default">发表评论</b-button>
      <b-button type="reset" variant="default">重置</b-button>
    </b-form>
  </b-card>
  <br>
  </div>
</template>
<script>
import { imageupload, addcomment } from '@/api/api'
import VueMarkdown from 'vue-markdown'
import { mavonEditor } from 'mavon-editor'
import 'mavon-editor/dist/css/index.css'
import { mapGetters } from 'vuex'

export default {
  data () {
    return {
      value: '',
      placeholder: '请输入评论内容',
      pid: null,
      editable: true
    }
  },
  components: {
    VueMarkdown,
    mavonEditor
  },
  computed: {
    ...mapGetters({
      user: 'user'
    })
  },
  created () {
    this.editable = this.set_editable()
  },
  props: ['comments', 'article_id'],
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
      if (this.user.token) {
        if (this.value) {
          var formdata = new FormData()
          var content = this.markdown(this.value)
          formdata.append('content', content)
          formdata.append('article', this.article_id)
          if (this.pid) {
            formdata.append('parent', this.pid)
          }
          addcomment(formdata)
        } else {
          evt.preventDefault()
          alert('请输入评论内容')
          this.$refs.md.textAreaFocus()
        }
      } else {
        alert('请登录！')
      }
    },
    onReset () {
      this.value = ''
      this.placeholder = '请输入评论内容!'
      this.pid = null
    },
    reply (pid, username) {
      if (this.user.token) {
        this.$refs.md.textAreaFocus()
        this.placeholder = '回复' + username
        this.pid = pid
        console.log(pid)
      } else {
        alert('请登录！')
      }
    },
    markdown (content) {
      return this.$refs.md.markdownIt.render(content)
    },
    set_editable () {
      if (this.user.token) {
        return true
      } else {
        this.placeholder = '看到也没用，登录后才能使用！'
        return false
      }
    }
  }
}
</script>
<style>

</style>

