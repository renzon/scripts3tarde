$(document).ready(function () {
  var $txtInput = $('#txt-input');
  var $listaDiv = $('#lista-div');
  var $inputNome = $("input[name='nome']");
  var $ajaxImg = $('#ajax-img');
  $ajaxImg.hide();
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

  var $salvarBotao = $('#salvar-produto-btn');
  $salvarBotao.click(function(){
    $('div.has-error').removeClass('has-error');
    $('span.help-block').text('');
    $ajaxImg.fadeIn();
    $salvarBotao.attr('disabled','disabled');
    $.post('/rest/produtos/salvar',obterInputs(), function(produto){
      console.log(produto);
      $('input.form-control').val('');
    }).error(function(erro){
      var errosJson = erro.responseJSON;
      for (propriedade in  errosJson){
        $('#'+propriedade+'-div').addClass('has-error');
        $('#'+propriedade+'-span').text(errosJson[propriedade]);
      }
    }).always(function(){
      $ajaxImg.fadeOut();
      $salvarBotao.removeAttr('disabled');
    });

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