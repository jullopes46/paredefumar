function calcular() {
    const valor = document.getElementById("valor").value;
    const quantia = document.getElementById("quantia").value;
    const tempo = document.getElementById("tempo").value;
    const custo = (valor/20*(quantia*20)*(tempo*365))
    const cigarro = valor / 20
    const mes = 30
    const ano = mes*12

    document.getElementById("cada").textContent = `O valor de cada cigarro é R$ ${(valor/20).toFixed(2)}`;
    document.getElementById("custo").textContent = `Se você fumou ${quantia} cigarro por dia você fumou ${(quantia/20)*100}% de um maço, e gastou em um mes R$ ${((cigarro*20)*mes).toFixed(2)}`;
    document.getElementById("ano").textContent = `Em se um ano tem ${ano} dias e cada cigarro tem o valor de R$ ${(cigarro).toFixed(2)}, no fim das contas em um anos você fumou ${quantia*ano}`;
    document.getElementById("total").textContent = `Ao total você acabpou de gastar aproximadamente R$ ${custo}`;
}
