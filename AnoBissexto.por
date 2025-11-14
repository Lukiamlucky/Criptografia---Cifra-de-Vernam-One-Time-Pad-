programa {
  funcao inicio() {
    inteiro ano

    limpa()
    escreva("Digite o ano: ")
    leia(ano)
    limpa()
    escreva("RESULTADO\n\n")   

    se (vrfAnoBissexto(ano)) {
      escreva("O ano de " + ano + " é um ano bissexto.\n")
    } senao {
      escreva("O ano de " + ano + " NÃO é um ano bissexto.\n")
    }
  }

  funcao logico vrfAnoBissexto(inteiro a) {
    se (( a % 4 == 0 e a % 100 != 0 ) ou (a % 400 == 0)) {
      retorne verdadeiro
    } senao {
      retorne falso
    }
  }
}
