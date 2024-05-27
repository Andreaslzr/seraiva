import type { Livro } from "./livros";
import type { Usuario } from "./usuario";

export type Emprestimo = {
    id?: number,
    usuarioFK: string;
} 

export type EmprestimoLivros = {
    livroFK: Livro;
    quantidade: number;
    emprestimoFK: Emprestimo;
}

export type EmprestimoLivrobody = {
    livroFK: number;
    quantidade: number;
    emprestimoFK: number;
}