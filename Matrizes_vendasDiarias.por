programa {
  funcao inicio() {
    inteiro qtdedeVendedores=3,qtdedeDias=5
    real vendasDiarias[qtdedeVendedores][qtdedeDias],faturamentoDiario[qtdedeDias],faturamentoSemanal=0,faturamentoPorVendedor[qtdedeVendedores]
    cadeia nomes[qtdedeVendedores],diasdaSemana[qtdedeDias]
    diasdaSemana[0]="Segunda"
    diasdaSemana[1]="Terça"
    diasdaSemana[2]="Quarta"
    diasdaSemana[3]="Quinta"
    diasdaSemana[4]="Sexta"
    para(inteiro i=0;i<qtdedeVendedores;i++){
      escreva("O "+(i+1)+"º vendedor: ")
      leia(nomes[i])
    } para(inteiro linha=0;linha<qtdedeVendedores;linha++){
      para(inteiro coluna=0;coluna<qtdedeDias;coluna++){
      escreva("A venda de "+(nomes[linha])+" do dia "+(diasdaSemana[coluna])+" : ")
      leia(vendasDiarias[linha][coluna])
      faturamentoDiario[coluna]=0
      }
      faturamentoPorVendedor[linha]=0
    }
    escreva("Resultados: \n")
    para(inteiro linha=0;linha<qtdedeVendedores;linha++){
      para(inteiro coluna=0;coluna<qtdedeDias;coluna++){
        faturamentoDiario[coluna]+=vendasDiarias[linha][coluna]
        faturamentoPorVendedor[linha]+=vendasDiarias[linha][coluna]
        faturamentoSemanal+=vendasDiarias[linha][coluna]
      }
    }
    escreva("Faturamento total "+faturamentoSemanal+"\n")
    para(inteiro linha=0;linha<qtdedeVendedores;linha++){
      escreva("O faturamento de "+(nomes[linha])+" foi de "+faturamentoPorVendedor[linha]+"\n")
    } para(inteiro coluna=0;coluna<qtdedeDias;coluna++){
      escreva("O faturamento do dia "+diasdaSemana[coluna]+" foi de "+faturamentoDiario[coluna]+"\n")
    }
  }
}
