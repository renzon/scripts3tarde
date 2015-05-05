$(document).ready(function () {
  var $txtInput = $('#txt-input');
  var $listaDiv = $('#lista-div');
  var $msgUl = $('#msg-ul');

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
    $msgUl.fadeOut(400,function(){
      $msgUl.fadeIn(2000);
    });
  });
});