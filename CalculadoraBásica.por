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

      se (opmat == "+") {
        soma(n1,n2)
      } senao se (opmat == "-") {
        subtracao(n1,n2)
      } senao se (opmat == "*") {
        multiplicacao(n1,n2)
      } senao se (opmat == "/") {
        divisao(n1,n2)
      }
      
      escreva("\nTecle <ENTER> para prosseguir.")
      leia(prosseguir)
    } enquanto (i)
  }

  funcao soma(real num1, real num2) {
    escreva ("\n" + num1 + " + " + num2 + " = " + (num1+num2) + "\n")
  }

  funcao subtracao(real num1, real num2) {
    escreva ("\n" + num1 + " - " + num2 + " = " + (num1-num2) + "\n")
  }

  funcao multiplicacao(real num1, real num2) {
    escreva ("\n" + num1 + " x " + num2 + " = " + (num1*num2) + "\n")
  }

  funcao divisao(real num1, real num2) {
    se (num2 != 0) {
      escreva ("\n" + num1 + " / " + num2 + " = " + (num1/num2) + "\n")
    } senao {
      escreva ("\n" + num1 + " / " + num2 + " = Divisão impossível!!\n")
    }
  }

}
