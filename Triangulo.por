programa {
  inclua biblioteca Matematica --> mat

  funcao inicio() {
    real lado1, lado2, lado3
    escreva("Digite o primeiro lado: ")
    leia(lado1)
    escreva("Digite o segundo lado: ")
    leia(lado2)
    escreva("Digite o terceiro lado: ")
    leia(lado3)

    limpa()
    escreva("RESULTADO\n\n")

    se(ehTriangulo(lado1, lado2, lado3)) {
      escreva("O triângulo de lados '" + lado1 + "', '" + lado2 + "' e '" + lado3 + "' é do tipo " + tipoTriangulo(lado1, lado2, lado3) + ".\n")
      escreva("A área do triângulo é de " + formulaHeron(lado1, lado2, lado3) + " ua.\n")
    } senao {
      escreva("As dimensões '" + lado1 + "', '" + lado2 + "' e '" + lado3 + "' NÃO formam um triângulo.\n")
    }

  }

  funcao logico ehTriangulo(real l1, real l2, real l3) {
    se ((l1 + l2) > l3 e (l1 + l3) > l2 e (l2 + l3) > l1) {
      retorne verdadeiro
    } senao {
      retorne falso
    }
  }

  funcao inteiro semiPerimetro(real l1, real l2, real l3) {
    retorne (l1 + l2 + l3)/2
  }

  funcao cadeia tipoTriangulo(real l1, real l2, real l3) {
    cadeia resposta = ""
    se (l1*l1 == l2*l2 + l3*l3 ou l2*l2 == l1*l1 + l3*l3 ou l3*l3 == l1*l1 + l2*l2) {
      resposta = "RETÂNGULO e "
    }
    se(l1 == l2 e l2 == l3) {
      resposta += "EQUILÁTERO"
    } senao se (l1 == l2 ou l1 == l3 ou l2 == l3) {
      resposta += "ISÓSCELES"
    } senao {
      resposta += "ESCALENO"
    }
    retorne resposta
  }

  funcao real formulaHeron(real l1, real l2, real l3) {
    real p = semiPerimetro(l1, l2, l3)
    retorne mat.raiz((p*(p-l1)*(p-l2)*(p-l3)),2)
  }
}
