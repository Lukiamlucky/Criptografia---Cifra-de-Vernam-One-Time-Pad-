programa {
  funcao inicio() {
    real grausC, grausF
    logico i = verdadeiro
    caracter opcao
    cadeia prosseguir

    faca {
      limpa()
      escreva("CONVERSÃO DE TERMPERATURAS")
      escreva("\n\n1 - Fahreinheit para Celsius")
      escreva("\n2 - Celsius para Fahreinheit")
      escreva("\n\nOpte por uma conversão: ")
      leia(opcao)

      escolha(opcao){
        caso "1":
          limpa()
          escreva("Digite a temperatura em ºF: ")
          leia(grausF)
          grausC = converteF2C(grausF)
          escreva("\n" + grausF + " ºF = " + grausC + " ºC\n")
        pare
        caso "2":
          limpa()
          escreva("Digite a temperatura em ºC: ")
          leia(grausC)
          grausF = converteC2F(grausC)
          escreva("\n" + grausC + " ºC = " + grausF + " ºF\n")
        pare
        caso contrario:
          limpa()
          escreva("Opção inválida!\n")
      }
      escreva("\nTecle <ENTER> para prosseguir. ")
      leia(prosseguir)
    } enquanto(i)
  }

  funcao real converteF2C(real tempF) {
    retorne (tempF-32)/1.8
  }

  funcao real converteC2F(real tempC) {
    retorne (tempC*1.8)+32
  }
}
