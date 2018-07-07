<template>
 <b-card header="评论" header-tag="header">
   <template v-for="comment in comments">
     <b-card :title="comment.id"
              sub-title="Card subtitle" :key="comment.id">
          <p class="card-text">
              Some quick example text to build on the <em>card title</em> and make up the bulk of the card's content.
          </p>
          <a href="#"
             class="card-link">Card link</a>
          <b-link href="#"
                  class="card-link">Another link</b-link>
      </b-card>
    </template>
  </b-card>
</template>
<script>
export default {
  props: ['comments']
}
</script>
