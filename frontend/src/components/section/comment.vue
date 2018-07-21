<template>
<div>
 <b-card header="评论" header-tag="header">
   <template v-for="comment in comments">
     <b-card>
       <b-media>
         <b-img slot="aside" width="50" alt="avatar" :src="comment.user.social_auth.extra_data.profile_image_url" />
         <h6 class="mt-0">{{comment.user.username}}</h6>
         <div v-html="markdown(comment.content)"></div>
         <p>
           <timeago :since="comment.created_time" locale="zh-CN" class="text-muted"></timeago>
           <b-button variant="link" @click="reply(comment.id)">回复</b-button>
         </p>
         <hr>
         <template v-for="child in comment.children">
         <b-media>
         <b-img slot="aside" width="50" alt="placeholder" :src="child.user.social_auth.extra_data.profile_image_url"/>
           <h6 class="mt-0">{{child.user.username}}</h6>
           <p>{{child.content}}</p>
           <p>
             <timeago :since="child.created_time" locale="zh-CN" class="text-muted"></timeago>
             <b-button variant="link" @click="reply(comment.id)">回复</b-button>
           </p>
         </b-media>
         <hr>
         </template>
       </b-media>
     </b-card>
   </template>
     <b-form @submit="onSubmit">
      <mavon-editor @imgAdd="$imgAdd" ref=md v-model="value" id="editor"></mavon-editor>
      <br>
      <b-button type="submit" variant="default">发表评论</b-button>
    </b-form>
  </b-card>
  </div>
</template>
<script>
import { imageupload, addcomment } from '@/api/api'

export default {
  data () {
    return { value: '' }
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
    onSubmit () {
      var formdata = new FormData()
      formdata.append('content', this.value)
      formdata.append('article', this.article_id)
      addcomment(formdata)
    },
    markdown (content) {
      return this.$refs.md.markdownIt.render(content)
    },
    reply (pid) {
      this.$refs.md.textAreaFocus()
      console.log(pid)
    }
  }
}
</script>
