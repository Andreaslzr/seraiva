export type Categoria = {
    id: number;
    nome: string;
}
export type Livro = {
    id: number;
    titulo: string;
    avaliacao: number;
    valor: number;
    quantidade: number;
    categoriaFK: Categoria;
    imagem: string;
}
