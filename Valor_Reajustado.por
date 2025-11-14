programa {
  funcao inicio() {
    real valor, valorReajustado

    limpa()
    escreva("Digite o valor da mercadoria: ")
    leia(valor)
    
    valorReajustado = reajuste(valor)

    escreva("\nO valor original era de R$ " + valor + " e, depois do reajuste, passou a ser de R$ " + valorReajustado + ".\n")
  }

  funcao real reajuste(real v) {
    retorne v * 1.2
  }
}
