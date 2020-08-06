var titulo = document.querySelector(".titulo"); // pega o elemento do HTML
titulo.textContent = "Aparecida Nutricionista"; // alterar conteudo de alguma variável do HTML

// var paciente = document.querySelector("#primeiro-paciente"); retorna apenas uma coisa

var pacientes = document.querySelectorAll(".paciente") // pegar todo elemento de uma classe ou id do HTML 

for (let indice = 0; indice < pacientes.length; indice++) {
    const paciente = pacientes[indice];
   
    var tdPeso = paciente.querySelector(".info-peso"); // guardei o elemento classe: info-peso dentro da variavel tdPeso
    var tdAltura = paciente.querySelector(".info-altura");

    var peso = tdPeso.textContent; // peguei o conteudo da variavel tdPeso e coloquei na variavel peso
    var altura = tdAltura.textContent; // peguei o conteudo da variavel tdAltura e coloquei na variavel altura

    var tdImc = paciente.querySelector(".info-imc"); // peguei o elemento classe: info-imc e guardei na variavel tdImc

    if (peso <= 0 || peso >= 1000 ) {
        tdImc.textContent = "Peso inválido."; // alterei o conteúdo da variavel Imc que foi criada
        paciente.classList.add("error");
    }else if (altura <= 0 || altura >= 3) {
        tdImc.textContent = "Altura inválida.";
        paciente.classList.add("error");
    }else {
        paciente.classList.remove("error");
        var imc = calculaImc(peso, altura);
        tdImc.textContent = imc; // alterei o conteudo da variavel Imc
    }
}


function calculaImc(peso, altura) {
    var imc = peso / (altura * altura); // criei uma variavel "imc"

    return imc.toFixed(2);
}





