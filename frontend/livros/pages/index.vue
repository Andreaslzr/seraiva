<script setup lang="ts">
import { getLivros } from "~/services/livros";
import { type Livro } from "~/models/livros";
import { type Ref, ref } from "vue";
import { useToast } from "primevue/usetoast";
const toast = useToast();

const show = () => {
    toast.add({ severity: 'success', summary: 'Livro Adicionado', detail: 'Acesse-o em seu carrinho', life: 30000 });
};

const livros: Ref<Array<Livro>> = ref([]);

  

const atualizarLivros = () => {
  getLivros().then((livrosEncontrados) => {
    console.log("livros encontrados: ", livrosEncontrados?.results[0].titulo);
    livros.value = livrosEncontrados?.results ?? [];
  });
};

atualizarLivros();

const painel = ref();

const toggle = (event: any) => {
    painel.value.toggle(event);
}
</script>

<template>
  <main class="home-container flex flex-column align-items-center">
        <div class="chatbot">
            <Button type="button" icon="pi pi-comment" label="Chatbot" @click="toggle" />
            <OverlayPanel ref="painel">
                <iframe allow="microphone;" width="350" height="430"
                    src="https://console.dialogflow.com/api-client/demo/embedded/a423ff1d-1da7-4eae-b5a3-9f59361ec297">
                </iframe>
            </OverlayPanel>
        </div>
    <h1 class="mt-4 mb-4">SERAIVA</h1>
    <Toast />
    <div class="produtos-container grid align-items-center justify-content-center">
        <div v-for="(livro,index) in livros">
            <LivroItem :key="index" class="col-4" :livro="livro" @eventoAdicionado="show" />
        </div>
    </div>
  </main>
</template>

<style scoped lang="scss">
.home-container {
  margin: 0;
  width: 100vw;
  min-height: calc(100vh - 80px);
  background-color: rgb(154, 154, 243);
  background-image: url("background.jpg");
  background-repeat: repeat;
  background-size: cover;
}

.p-toast-summary		{
  padding: 1.5rem !important;
}

.chatbot{
    position: fixed;
    top: 0;
    right: 0;
    margin: 1rem
}

</style>
