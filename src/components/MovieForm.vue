<template> 
    <form @submit.prevent="saveMovie" method="POST" id="movieForm" enctype = "multipart/form-data">
        <div class="form-group">
            <label for="title">Title</label>
            <input class="form-control" id="title" rows="3" name="title" >
        </div>
        <div class="form-group">
            <label for="description">Description</label>
            <textarea class="form-control" id="description" rows="3" name="description" ></textarea>
        </div>

        <div class="form-group">
            <label for="poster">Poster Upload</label><br>
            <input type="file" class="form-control-file" id="poster"  name="poster" >
        </div>

         <input type="submit" class="btn btn-primary"/>
         <!--<input id="csrf_token" name="csrf_token" type="hidden" value={{csrf_token}}>-->
         
    </form>
</template>
<script> 
import { ref, onMounted } from "vue"; 
//let csrf_token = ref(""); 
export default{
    data(){
        return{
            message:'',
            csrf_token:'',
        }
    },
    methods:{
        saveMovie(){

            const movieForm = document.getElementById('movieForm');
            const form_data = new FormData(movieForm);
            console.log(this.csrf_token);
            fetch("/api/v1/movies", {
                method: 'POST',
                body: form_data,
                headers: {
                    'X-CSRFToken': this.csrf_token
                }
            })
            .then(function (response) {
                return response.json();
            })
            .then(function (data) {
            // display a success message
                console.log(data);
            })
            .catch(function (error) {
                console.log(error);
            });
        },
        getCsrfToken() {
            fetch('/api/v1/csrf-token',{
                method: 'GET',
            })
            .then((response) => response.json())
            .then((data) => {
                console.log(data);
                this.csrf_token = data.csrf_token;
            })

        },
    },
    created(){
        this.getCsrfToken();
        console.log(this.csrf_token);
    },
}

</script>
<style>
</style>