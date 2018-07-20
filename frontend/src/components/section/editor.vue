<template>
  <b-form @submit="onSubmit">
    <mavon-editor @imgAdd="$imgAdd" ref=md v-model="value"></mavon-editor>
    <br>
    <b-button type="submit" variant="default">发表评论</b-button>
  </b-form>
</template>

<script>
import { imageupload } from '@/api/api'

export default {
  data () {
    return {
      value: ''
    }
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
      evt.preventDefault()
      console.log(this.value)
    }
  }
}
</script>
