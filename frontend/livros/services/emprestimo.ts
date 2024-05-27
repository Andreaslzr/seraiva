import { BACKEND_URL } from "~/models/app";
import type { Emprestimo, EmprestimoLivros, EmprestimoLivrobody } from "~/models/emprestimo";

export const salvarEmprestimo = (emprestimo: Emprestimo): Promise<Emprestimo | null> => {
  return useFetch<Emprestimo>(`${BACKEND_URL}/emprestimo/`, {
    method: 'POST',
    body: emprestimo
  })
    .then(resposta => {
      return Promise.resolve(resposta.data.value);
    })
    .catch(error => {
      console.log("error", error);
      return Promise.resolve(null);
    })
};


/*export const salvarEmprestimoLivro = (emprestimo: Array<EmprestimoLivrobody>): Promise<EmprestimoLivros | null> => {
  return useFetch<EmprestimoLivros>(`${BACKEND_URL}/emprestimo-livros/`, {
    method: 'POST',
    body: emprestimo
  })
    .then(resposta => {
      return Promise.resolve(resposta.data.value);
    })
    .catch(error => {
      console.log("error", error);
      return Promise.resolve(null);
    })
};*/



