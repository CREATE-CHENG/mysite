<template>
<div>
 <b-card header="评论" header-tag="header">
   <template v-for="comment in comments">
     <b-card>
       <b-media>
         <b-img slot="aside" width="50" alt="avatar" :src="comment.user.social_auth.extra_data.profile_image_url" />
         <h6 class="mt-0">{{comment.user.username}}</h6>
         <p>{{comment.content}}</p>
         <p><timeago :since="comment.created_time" locale="zh-CN" class="text-muted"></timeago></p>
         <hr>
         <template v-for="child in comment.children">
         <b-media>
         <b-img slot="aside" width="50" alt="placeholder" :src="child.user.social_auth.extra_data.profile_image_url"/>
           <h6 class="mt-0">{{child.user.username}}</h6>
           <p>{{comment.content}}</p>
           <p><timeago :since="child.created_time" locale="zh-CN" class="text-muted"></timeago></p>
         </b-media>
         <hr>
         </template>
       </b-media>
     </b-card>
     <br>
   </template>
   <editor></editor>
  </b-card>
  </div>
</template>
<script>
import editor from '@/components/section/editor'

export default {
  props: ['comments'],
  components: {
    'editor': editor
  }
}
</script>
