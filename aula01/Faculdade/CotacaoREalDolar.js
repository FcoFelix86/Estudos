async function converter() {
    const valor = parseFloat(document.getElementById("valor").value);
    const moeda = document.getElementById("moeda").value;
    const resultado = document.getElementById("resultado");

    if (isNaN(valor) || valor <= 0) {
        resultado.textContent = "Por favor, insira um valor válido.";
        return;
    }

    try {
        const response = await fetch("https://economia.awesomeapi.com.br/last/USD-BRL");
        const data = await response.json();
        const cotacao = parseFloat(data.USDBRL.bid);

        let valorConvertido;
        if (moeda === "USD") {
            valorConvertido = valor * cotacao;
            resultado.textContent = `R$ ${valorConvertido.toFixed(2)}`;
        } else {
            valorConvertido = valor / cotacao;
            resultado.textContent = `$ ${valorConvertido.toFixed(2)}`;
        }
    } catch (error) {
        resultado.textContent = "Erro ao buscar a cotação.";
        console.error("Erro:", error);
    }
}