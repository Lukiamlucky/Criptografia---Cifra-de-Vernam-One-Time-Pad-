programa {
  funcao inicio() {
    cadeia prosseguir
    caracter opmat
    real n1, n2
    logico i = verdadeiro
    faca {
      faca {
        limpa()
        escreva("Qual operação deseja executar (+, -, * ou /)? ")
        leia(opmat)
      } enquanto (opmat != "+" e opmat != "-" e opmat != "*" e opmat != "/")

      limpa()
      escreva("Digite o primeiro número da operação: ")
      leia(n1)
      escreva("Digite o segundo número da operação: ")
      leia(n2)

      calculadora(opmat, n1, n2)

      escreva("\nTecle <ENTER> para prosseguir.")
      leia(prosseguir)
    } enquanto (i)
  }

  funcao calculadora(caracter operacao, real num1, real num2) {
    se (operacao == "+") {
      escreva ("\n" + num1 + " + " + num2 + " = " + (num1+num2) + "\n")
    } senao se (operacao == "-") {
      escreva ("\n" + num1 + " - " + num2 + " = " + (num1-num2) + "\n")
    } senao se (operacao == "*") {
      escreva ("\n" + num1 + " x " + num2 + " = " + (num1*num2) + "\n")
    } senao se (operacao == "/") {
      se (num2 != 0) {
        escreva ("\n" + num1 + " / " + num2 + " = " + (num1/num2) + "\n")
      } senao {
        escreva ("\n" + num1 + " / " + num2 + " = Divisão impossível!!\n")
      }
    }
  }
}
