function frase(custo) {
    if (custo >= 7) {
        return "texto 01"
    } else if (custo >= 5) {
        return "texto 02"
    } else {
        return "texto 03"
    }
}


var resultado = frase(custoreal);
console.log(resultado);