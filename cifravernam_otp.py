import random # Função aleatória importada para gerar a chave aleatória segura
import string # Função string importada para compor o alfabeto

# --- Configuração do Alfabeto incluindo acentos gráficos e caracteres especiais ---
alfabeto = string.ascii_letters + string.digits + " ,.:;!?-()ÁÉÍÓÚÀÈÌÒÙÃÕÂÊÎÔÛÇáéíóúàèìòùãõâêîôûç" 
# o comando string.ascii_letters + string.digits compõe a variável alfabeto de letras e caracteres especiais
alfabeto_tamanho = len(alfabeto)

"""
    Converte um caractere para seu valor numérico (0 até alfabeto_tamanho - 1).
    Aplica-se a qualquer caractere no alfabeto estendido.
    """

def letra_num(caracter):
    
    return alfabeto.find(caracter)
#Retorna o índice,isto é o número correspondente à letra

def numero_letra(num):
    """
    Converte um valor numérico para o caractere correspondente, usando o módulo N.
    """
   
    num = num % alfabeto_tamanho
    #Garante que o número esteja dentro do intervalo permitido(alfabeto_tamanho)
    return alfabeto[num]
#Corresponde um número a sua letra dentro do intervalo permitido

def gerar_chave(tamanho):
    """
    Gera uma chave OTP aleatória e segura usando caracteres do alfabeto.
    """
    try:
        chave_segura = random.SystemRandom()
    except AttributeError:
        chave_segura = random
    
    # Gera a chave com caracteres presentes no alfabeto
    return ''.join(chave_segura.choice(alfabeto) for _ in range(tamanho))

# --- Função processamento ---

def processamento(texto, chave, mode='cripto'):
    """
    Função unificada tanto para cifrar quanto decifrar usando a Cifra de Vernam.
    """
    # Filtra apenas caracteres que estão no alfabeto
    caracteres_texto = [caracter for caracter in texto if caracter in alfabeto]
    #Atribui um vetor para cada elemento no texto que se encontra na variável alfabeto. Iterando o parâmetro texto e verificando se está contida em alfabeto
    caracteres_chave = [caracter for caracter in chave if caracter in alfabeto]
    #Atribui um vetor para cada elemento na chave que se encontra na variável alfabeto. Iterando o parâmetro chave e verificando se está contida em alfabeto
    
    # Assegura a condição do Vernam (OTP) : Texto e chave de mesmo tamanho.
    if len(caracteres_texto) != len(caracteres_chave):
        raise ValueError(f"ERRO: A chave deve ter o mesmo número de caracteres válidos ({alfabeto_tamanho}) que o texto.")

    resultado = list(texto) #Atribui variável resultado que armazena em uma lista 
    indice_chave = 0 #Atribui o índice da chave 0
    
    for i, caracter_texto in enumerate(texto):
        
        if caracter_texto in alfabeto: # Se caracter estiver no alfabeto . Então
            caracter_chave = caracteres_chave[indice_chave] #Atribui um vetor que recebe a posição dos caracteres da chave
            
            # 2. Mapeamento
            C_P = letra_num(caracter_texto) # Valor numérico do texto
            K = letra_num(caracter_chave)   # Valor numérico da chave
            
            # 3. Aplica a fórmula modular (agora mod N)
            if mode == 'cripto': #Testa a condição para criptografia
                # C = (P + K) mod N
                M_C = (C_P + K) % alfabeto_tamanho
            else:
                # M = (C - K) mod N (Descriptografia)
                M_C = (C_P - K + alfabeto_tamanho) % alfabeto_tamanho
            
            # Converte o resultado para a letra
            resultado[i] = numero_letra(M_C)
            
            indice_chave += 1
            
    return "".join(resultado)

# --- Função de Interação do Usuário (Menu) ---

def vernam_interface():
    print("\n--- Cifra de Vernam (OTP) - Simétrica Modular  ---")
    
    # Escolha de Modo
    while True:
        modo = input("Você quer [C]ifrar ou [D]ecifrar? (C/D): ").upper()
        if modo in ['C', 'D']:
            break
        print("Opção inválida. Digite C para Cifrar ou D para Decifrar.")
        
    try:
        if modo == "C" or modo == "c":
            # --- MODO CIFRAR ---
            texto_original = input("\nDigite a MENSAGEM a ser criptografada: ").strip()
            # O tamanho da chave é baseado em todos os caracteres válidos no alfabeto
            caracteres_validos = "".join(c for c in texto_original if c in alfabeto)
            chave_tamanho = len(caracteres_validos) #Tamanho da chave corresponde ao comprimento de caracteres válidos presentes
            
            if chave_tamanho == 0: #Verifica a condição caso mensagem não contenha caracteres válidos
                print("Mensagem não contém caracteres válidos para cifrar.")
                return

            # Chama a função geradora da chave aleatória segura
            chave = gerar_chave(chave_tamanho)
            #Chama a função de criptografia
            texto_cifrado = processamento(texto_original, chave, mode='cripto')
            
            print("-" * 50)
            print(f"[CHAVE GERADA] Use esta chave para decifrar: {chave}")
            print(f"[CRIPTOGRAFIA] Texto Cifrado: {texto_cifrado}")
            print("-" * 50)

        elif modo == 'D' or modo =="d":
            # --- MODO DECIFRAR ---
            texto_cifrado = input("\nDigite o TEXTO CIFRADO: ").strip()
            chave = input("Digite a CHAVE OTP correspondente: ").strip()

            caracteres_cifrados = "".join(c for c in texto_cifrado if c in alfabeto) #Junta todos elemento na cifra . Iterando o parâmetro texto_cifrado e verificando se está contida em alfabeto 
            caracteres_chave = "".join(c for c in chave if c in alfabeto) #Junta todos elemento na cifra . Iterando o parâmetro texto_cifrado e verificando se está contida em alfabeto
            
            if len(caracteres_cifrados) != len(caracteres_chave): #Testa a condição que garante mesmo comprimento tanto para cifra quanto para a chave
                 raise ValueError("ERRO: O número de caracteres válidos no texto e na chave não coincide. O OTP é inválido.")
            
            texto_decriptografado = processamento(texto_cifrado, chave, mode='decifrar') #Chama a função responsável pela descriptografia 

            print("-" * 50)
            print(f"[DESCRIPTOGRAFIA] Texto Original Decifrado: {texto_decriptografado}")
            print("-" * 50)
            
    except ValueError as e:
        print(f"\nERRO: {e}")

if __name__ == "__main__":
    vernam_interface()