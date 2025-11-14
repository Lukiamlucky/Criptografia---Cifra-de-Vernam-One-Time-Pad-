programa {
  funcao inicio() {
    inteiro termo
    limpa()
    escreva("TERMO DA SEQUÊNCIA DE FIBONACCI\n\n")
    escreva("Digite o número: ")
    leia(termo)
    limpa()
    escreva("RESULTADO\n")   
    escreva("O " + termo + "º termo da sequência de Fibonacci é " + fibonacci(termo) + ".\n")
  }

  funcao inteiro fibonacci(inteiro t) {
    inteiro fibo_antes1,fibo_antes2, fibo, aux
    escreva("\n")
    para (inteiro i=1; i<=t; i++) {
      se (i == 1) {
        fibo = 0
      } senao se (i == 2) {
        fibo = 1
        fibo_antes1 = 0
        fibo_antes2 = 1
      } senao {
        fibo = fibo_antes1 + fibo_antes2
        aux = fibo_antes2
        fibo_antes2 = fibo
        fibo_antes1 = aux
      }
    }
    retorne fibo
  }
}
