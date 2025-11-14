programa {
  funcao inicio() {
    inteiro numero
    limpa()
    escreva("CÁLCULO DO FATORIAL\n\n")
    escreva("Digite o número: ")
    leia(numero)
    limpa()
    escreva("RESULTADO\n") 
    se (numero < 0) {
      escreva("\nNão existe fatorial para número negativo!\n")
    } senao {
      escreva("\n" + numero + "! = " + fatorial(numero) + "\n")
    }
  }

  funcao inteiro fatorial(inteiro n) {
    inteiro fatorial = 1
    para (inteiro i=n; i>0; i--) {
      fatorial *= i
    }
    retorne fatorial
  }
}