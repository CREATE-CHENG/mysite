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

      <b-card>
  <b-media>
    <b-img slot="aside" blank blank-color="#ccc" width="64" alt="placeholder" />
    <h5 class="mt-0">Media Title</h5>
    <p>
      Cras sit amet nibh libero, in gravida nulla. Nulla vel metus scelerisque ante
      sollicitudin. Cras purus odio, vestibulum in vulputate at, tempus viverra turpis.
      Fusce condimentum nunc ac nisi vulputate fringilla. Donec lacinia congue felis
      in faucibus.
    </p>
    <p>
      Donec sed odio dui. Nullam quis risus eget urna mollis ornare vel eu leo. Cum
      sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.
    </p>
    <b-media>
    <b-img slot="aside" blank blank-color="#ccc" width="64" alt="placeholder" />
      <h5 class="mt-0">Nested Media</h5>
      <p class="mb-0">
        Fusce condimentum nunc ac nisi vulputate fringilla. Donec lacinia
        congue felis in faucibus.
      </p>
    </b-media>
  </b-media>
</b-card>


    </template>
  </b-card>
</template>
<script>
export default {
  props: ['comments']
}
</script>
