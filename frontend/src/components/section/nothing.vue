<template>
  <b-col cols="8">
    <b-card header="404">
      <b-jumbotron header="404" lead="" >
        <hr class="my-4">
        <b-btn variant="secondary" href="/">回到首页</b-btn>
      </b-jumbotron>
     </b-card>
  </b-col>
</template>

<script>
export default {
  created () {
    document.title = '无何有之乡'
  }
}
</script>
