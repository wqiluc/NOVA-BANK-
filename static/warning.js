let saldo = 0;

function avisoSaldoZero() {
    if (saldo === 0) {
        alert("⚠️ Atenção: sua conta está com saldo R$ 0,00.");}}

function avisoSaqueInvalido(valorSaque) {
    if (valorSaque > saldo) {
        alert(
            "❌ Saque não permitido!\n\n" +
            "Seu saldo atual é R$ " + saldo.toFixed(2) + 
            ", e o valor solicitado excede o limite.");
        return false;}
        return true;}

function avisoSairMenu() {
    return confirm(
        "🏦 Deseja realmente sair do menu do banco?\n\n" +
        "Clique em OK para sair ou Cancelar para continuar.");}

        
function atualizarSaldo(novoSaldo) {
    saldo = Number(novoSaldo);}