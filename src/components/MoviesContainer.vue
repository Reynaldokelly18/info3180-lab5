<template> 
    <section class="moviecontainer"> 
        <div class="movie" v-for="movie in movies">
         <img v-bind:src="`../uploads/${movie.poster}`" alt="">
         <div class="moviebody">
            <h4>  {{ movie.title }}</h4>
            <p>
               {{ movie.description }}
           </p>
         </div>
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
section.moviecontainer{
    display: grid;
    grid-template-columns: repeat(2,1fr);
    grid-gap: 2em;
    width: 90%;
    margin: 2em auto;
}
div.movie img{
   width: 50%;
   
}
div.movie {
    display: flex;
    flex-flow: row wrap;
}
div.moviebody {
    display: flex;
    flex-flow: column wrap;
}
</style>