$(document).ready(function () {
  var $txtInput = $('#txt-input');
  var $listaDiv = $('#lista-div');
  var $inputNome = $("input[name='nome']");

  var $msgUl = $('#msg-ul');

  var $selectCategoria = $("select[name='categoria']");
  var $inputPreco = $("input[name='preco']");

  function obterInputs() {
    return {
      'preco': $inputPreco.val(),
      'nome': $inputNome.val(),
      'categoria': $selectCategoria.val()
    };
  }

  $('#salvar-produto-btn').click(function(){
    console.log(obterInputs());
  });

  $('#jq').click(function fcn(evento) {
    $listaDiv.slideToggle();
  });

  $('#jq2').click(function fcn(evento) {
    $listaDiv.empty();
  });

  $('#enviar-btn').click(function () {
    var msg = $txtInput.val();
    $txtInput.val('');
    var item = '<li>' + msg + '</li>';
    $msgUl.prepend(item);
    $msgUl.fadeOut(400, function () {
      $msgUl.fadeIn(2000);
    });
  });


});