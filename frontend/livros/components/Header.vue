<script setup lang="ts">


</script>

<template>
  <header>
    <div class="flex align-items-center justify-content-center">
        <div class="menu-item flex align-items-center justify-content-center mr-4">
          <i class="pi pi-home mr-1"></i>
          <NuxtLink to="/">Livros</NuxtLink>
        </div>
        <div class="menu-item flex align-items-center justify-content-center mr-4">
          <i class="pi pi-shopping-cart mr-1"></i>
          <NuxtLink to="/carrinho">Carrinho</NuxtLink>
        </div>
        <div class="menu-item flex align-items-center justify-content-center mr-4">
          <i class="pi pi-book mr-1"></i>
          <NuxtLink to="/bibliotecaria">bibliotecaria</NuxtLink>
        </div>
        <div class="menu-item flex align-items-center justify-content-center mr-4">
          <i class="pi pi-address-book mr-1"></i>
          <NuxtLink to="/autor">autor</NuxtLink>
        </div>
    </div>
  </header>
</template>

<style scoped lang="scss">
header {
  width: 100vw;
  height: var(--altura-header);

  .menu-item{
    height: var(--altura-header);
    
    a{
      text-decoration: none;
      color: black;
    }
    &:hover{
      transform: scale(1.1);
    }
  }
}
</style>
