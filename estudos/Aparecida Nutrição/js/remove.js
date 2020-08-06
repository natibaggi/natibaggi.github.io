// var pacientes = document.querySelectorAll(".paciente")

// pacientes.forEach(function(paciente){
//     paciente.addEventListener("dblclick", function(){
//         this.remove();
//     });
// });


var dadosTabela = document.querySelector("#tabela-pacientes");

dadosTabela.addEventListener("dblclick", function(event){
    var alvoEvento = event.target;
    var paiDoAlvo = alvoEvento.parentNode;
    var classePai = paiDoAlvo.classList.add("efeitoRemover");

    setTimeout(function(){
        paiDoAlvo.remove();
    },500);
});