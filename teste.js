function verificarAprovacao(nota) {
    if (nota >= 7) {
        return "Aprovado!";
    } else if (nota >= 5) {
        return "Recuperação!";
    } else {
        return "Reprovado!";
    }
}

let notaAluno = 6;
let resultado = verificarAprovacao(notaAluno);
console.log(resultado);