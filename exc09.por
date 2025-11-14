programa {
  funcao inicio() {
    real nota1, nota2, media
    limpa()
    escreva("CÁLCULO DA MÉDIA E DEFINIÇÃO DA SITUAÇÃO DO ALUNO\n\n")
    escreva("Digite a nota NP1 : ")
    leia(nota1)
    escreva("Digite a nota NP2 : ")
    leia(nota2)
    media = mediaSemestre(nota1, nota2)
    limpa()
    escreva("RESULTADO\n\n")
    escreva("A média do(a) aluno(a) foi " + media + " e ele(a) foi " + situacao(media) + ".\n")
  }

  funcao inteiro mediaSemestre(real np1, real np2) {
    retorne (np1 + np2)/2
  }

  funcao cadeia situacao(real media) {
    se (media >= 7) {
      retorne "APROVADO(A)"
    } senao {
      retorne "REPROVADO(A)"
    }
  }
}
