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

      se(opmat == "+") {
        escreva("\n" + n1 + " " + opmat + " " + n2 + " = " + soma(n1, n2) + "\n")
      } senao se (opmat == "-") {
        escreva("\n" + n1 + " " + opmat + " " + n2 + " = " + subtracao(n1, n2) + "\n")
      } senao se (opmat == "*") {
        escreva("\n" + n1 + " " + opmat + " " + n2 + " = " + multiplicacao(n1, n2) + "\n")
      } senao {
        se (n2 != 0) {
          escreva("\n" + n1 + " " + opmat + " " + n2 + " = " + divisao(n1, n2) + "\n")
        } senao {
          escreva("\n" + n1 + " " + opmat + " " + n2 + " = Divisão impossível!\n")
        }
      }

      escreva("\nTecle <ENTER> para prosseguir.")
      leia(prosseguir)
      
    } enquanto (i)
  }

  funcao real soma(real num1, real num2) {
    retorne num1 + num2
  }

  funcao real subtracao(real num1, real num2) {
    retorne num1 - num2
  }

  funcao real multiplicacao(real num1, real num2) {
    retorne num1 * num2
  }

  funcao real divisao(real num1, real num2) {
    retorne num1 / num2
  }
}
