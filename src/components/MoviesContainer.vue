<template> 
    <section class="moviecontainer"> 
        <div class="movie" v-for="movie in movies">
         <img v-bind:src="`../uploads/${movie.poster}`" alt="">
         <h4>  {{ movie.title }}</h4>
         <p>
            {{ movie.description }}
         </p>
        </div>

    </section>
</template>
<script> 
//import { ref, onMounted } from "vue"; 
//let csrf_token = ref(""); 
export default{
    data(){
        return{
            movies:[],
           
        }
    },
    
    created(){
        fetch('/api/v1/movies',{
                method: 'GET',
            })
            .then((response) => response.json())
            .then((data) => {
              this.movies=data;
              console.log(data);
            })
    },
}

</script>
<style>
</style>