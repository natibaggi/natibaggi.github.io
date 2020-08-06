var botaoAdicionar = document.querySelector(".botao-adicionar");

// function cliqueiNoBotao() {
//     console.log("Oi, cliquei no botão.")
// }

botaoAdicionar.addEventListener("click", function(event){ // A posição do () e do {} é por causa da function
    event.preventDefault();

    var form = document.querySelector(".form-adiciona"); //"pega" a elemento classe: form-adiciona do html

    var paciente = extraiConteudoForm(form); // função

    var pacienteTr = criaTr(paciente); // função

    var tabela = document.querySelector("#tabela-pacientes"); // guardei a elemento id: tabela-pacientes dentro da variavel tabela

    tabela.appendChild(pacienteTr); // está criando apenas 1, verificar porque

    form.reset();
})


function extraiConteudoForm(form) {
    var paciente = {
        nome: form.nome.value, // "pega" o conteudo da elemento form - nome
        peso: form.peso.value,
        altura: form.altura.value,
        gordura: form.gordura.value,
        imc: calculaImc(form.peso, form.altura)
    }
    return paciente
}


function criaTr(paciente) {
    var pacienteTr = document.createElement("tr"); //cria uma tr
    pacienteTr.classList.add("paciente");

    var nomeTd = criaTd(paciente.nome, "info-nome");
    var pesoTd = criaTd(paciente.peso, "info-peso");
    var alturaTd = criaTd(paciente.altura, "info-altura");
    var gorduraTd = criaTd(paciente.gordura, "info-gordura");
    var imcTd = criaTd(paciente.imc, "info-imc");

    pacienteTr.appendChild(nomeTd); // coloca a variavel nomeTd como "Filho" da variavel pacienteTr
    pacienteTr.appendChild(pesoTd);
    pacienteTr.appendChild(alturaTd);
    pacienteTr.appendChild(gorduraTd);
    pacienteTr.appendChild(imcTd);

    return pacienteTr
}

function criaTd(dado, classe) {
    var dadoTd = document.createElement("td");
    dadoTd.textContent = dado;
    dadoTd.classList.add(classe);
    return dadoTd
}