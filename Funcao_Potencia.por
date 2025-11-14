programa {
  funcao inicio() {
    inteiro a, b
    real potencia

    limpa()
    escreva("Digite a base: ")
    leia(a)
    limpa()
    escreva("Digite o expoente: ")
    leia(b)
    
    potencia = potenciacao(a, b)

    escreva("\n" + a + " ^ " + b + " = " + potencia + "\n")
  }

  funcao real potenciacao(inteiro base, inteiro expoente) {
    real pot = 1
    se (expoente > 0) {
      para (inteiro i=0; i<expoente; i++) {
        pot *= base
      }
    } senao se (expoente < 0) {
      para (inteiro i=0; i<(-expoente); i++) {
        pot *= base
      }
      pot = 1/pot
    }
    retorne pot  
  }
}
