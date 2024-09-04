class ContaBancaria {
  // Atributos da conta bancária
  String titular;
  int numeroConta;
  double saldo;

  // Construtor da classe
  ContaBancaria({
    required this.titular,
    required this.numeroConta,
    this.saldo = 0.0,
  });

  // Método para exibir as informações da conta
  void exibirInformacoes() {
    print('Titular: $titular');
    print('Número da Conta: $numeroConta');
    print('Saldo: R\$ ${saldo.toStringAsFixed(2)}');
  }

  // Método para realizar saque
  void sacar(double valor) {
    if (valor > saldo) {
      print('Saldo insuficiente para saque.');
    } else {
      saldo -= valor;
      print('Saque de R\$ ${valor.toStringAsFixed(2)} realizado com sucesso.');
      print('Novo saldo: R\$ ${saldo.toStringAsFixed(2)}');
    }
  }
}

void main() {
  // Criando uma conta bancária
  ContaBancaria conta = ContaBancaria(
    titular: 'João Silva',
    numeroConta: 123456,
    saldo: 100.0,
  );

  // Exibindo informações da conta
  conta.exibirInformacoes();

  // Tentando sacar um valor maior que o saldo
  conta.sacar(150.0);

  // Realizando um saque válido
  conta.sacar(50.0);

  // Tentando sacar mais do que o saldo atual
  conta.sacar(60.0);

  // Exibindo informações após saques
  conta.exibirInformacoes();
}
