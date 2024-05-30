<script setup lang="ts">

definePageMeta({
    middleware:'auth'
})

</script>

<template>
    <main class="carrinho-container flex flex-column align-items-center">
        <h1>Tela Autor</h1>
    </main>
</template>

<style scoped lang="scss">

.carrinho-container {
  margin: 0;
  width: 100vw;
  min-height: calc(100vh - 80px);
  background-color: rgb(154, 154, 243);
  background-image: url("background.jpg");
  background-repeat: repeat;
  background-size: cover;
}
</style>