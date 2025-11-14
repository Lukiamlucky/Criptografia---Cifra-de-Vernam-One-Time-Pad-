programa {
 	funcao inicio() {
 		inteiro vet[100]
    limpa()
 		para (inteiro i=0; i<100; i++) {
      se(i % 2 == 1) {
        vet[i] = 1
      } senao {
        vet[i] = 0
      }
 		}
    escreva(vet)
 	}
}
