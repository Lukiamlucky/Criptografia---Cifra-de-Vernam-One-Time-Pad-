programa {
  funcao inicio() {
    inteiro qtde=10
    inteiro a[qtde],b[qtde],c[qtde]
    para(inteiro i=0;i<2;i++){
      se(i==0){
        para(inteiro j=0;j<qtde;j++){
        escreva("O "+(i+1)+" º elemento de A: ")
        leia(a[j])
        }
      }senao se(i>0){            
      para(inteiro k=0;k<qtde;k++){
      escreva("O "+(k+1)+" º elemento de B: ")
      leia(b[k])
      }para(inteiro l=0;l<qtde;l++){
        c[l]=a[l]+b[l]
      }
    }
    }  
    para(inteiro k=0;k<qtde;k++){
      escreva(""+c[k]+" = "+a[k]+" + "+b[k]+" .\n")
    }
  }
}
