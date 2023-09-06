function copiarTexto() {
    // Seleciona o elemento de input
    var inputElement = document.getElementById("meuInput");

    // Seleciona o texto no elemento de input
    inputElement.select();

    // Copia o texto para a área de transferência
    document.execCommand("copy");

    // Deseleciona o texto
    inputElement.setSelectionRange(0, 0);
}