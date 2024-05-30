<script setup>
    import { BACKEND_URL } from "~/models/app";
    const route = useRoute();
    const {data:livro} = await useFetch(`${BACKEND_URL}/livros/${route.params.id}`);

</script>

<template>
    <main class="container flex flex-column align-items-center">
        <h1>Tela detalhes livros</h1>
        <img :src=" livro.imagem "  width="500" height="500" >
        <h3>Titulo: {{ livro.titulo }}</h3>
        <h3>Descrição: {{ livro.descricao }}</h3>
        <h3>Formato: {{ livro.formato }}</h3>
        <h3>Número de paginas: {{ livro.paginas }}</h3>
        <h3>Categoria: {{ livro.categoriaFK.nome }}</h3>
        <h1>Autor</h1>
        <h3>Nome: {{ livro.autorFK.nome }}</h3>
        <img :src=" livro.autorFK.foto "  width="500" height="500" >
        <h3>Biografia: {{ livro.autorFK.biografia }}</h3>
    </main>
</template>

<style scoped lang="scss">

.container {
  margin: 0;
  width: 100vw;
  min-height: calc(100vh - 80px);
  background-color: rgb(154, 154, 243);
  background-image: url("background.jpg");
  background-repeat: repeat;
  background-size: cover;

}
</style>