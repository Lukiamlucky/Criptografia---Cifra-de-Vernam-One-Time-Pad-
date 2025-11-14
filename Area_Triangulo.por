programa {
  funcao inicio() {
    real base, altura, area

    limpa()
    escreva("Digite a base do retângulo: ")
    leia(base)
    limpa()
    escreva("Digite a altura do retângulo: ")
    leia(altura)


    area = areaRetangulo(base, altura)

    escreva("\nO retângulo de base '" + base + "' e de altura '" + altura + "' tem área de " + area + " ua.\n")
  }

  funcao real areaRetangulo(real b, real a) {
    retorne b * a
  }
}
