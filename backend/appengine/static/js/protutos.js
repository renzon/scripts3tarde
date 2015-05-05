var olaMundo = function olaMundo() {

  console.log('Olá Mundo')
};

olaMundo();

var outroMundo = olaMundo;

outroMundo();

function executarEContatenarString(fcn) {
  return 'Executando função com retorno: ' + fcn();
}

function blah() {
  return 'Blah';
}
function blah2() {
  return 'Blah2';
}

console.log(executarEContatenarString(blah));
console.log(executarEContatenarString(blah2));

function criarFuncaoTransladar(fcn){
  function transladar(x){
    return fcn(x)+ 1;
  }

  return transladar;
}

function reta45(x){
  return x;
}

var retaTransladada=criarFuncaoTransladar(reta45);

console.log(retaTransladada(1));
console.log(retaTransladada(2));

var obj={'a':1, b:2, 1:'utra coisa', t:retaTransladada };


console.log(obj);
console.log(obj.a);
console.log(obj['a']);
console.log(obj[1]);
console.log(obj.t(3))











