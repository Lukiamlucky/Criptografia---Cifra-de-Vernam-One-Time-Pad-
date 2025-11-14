programa {
  funcao inicio() {
    real grausF, grausC
    
    limpa()
    escreva("Digite a temperatura em ºF: ")
    leia(grausF)

    grausC = converteFC(grausF)

    escreva("\n" + grausF + " ºF = " + grausC + " ºC")
  }

  funcao real converteFC(real tempF) {
    retorne (tempF-32)/1.8
  }
}
