#-*- coding: utf-8 -*-#c

import random
import string

# Mapeamento e Configuração
ALFABETO_MAIUSCULAS = string.ascii_uppercase  # 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ALFABETO_MINUSCULAS = string.ascii_lowercase  # 'abcdefghijklmnopqrstuvwxyz'
TAMANHO_ALFABETO = 26

def gerar_chave_otp(tamanho):
    """
    Gera uma chave OTP aleatória de letras (maiúsculas e/ou minúsculas)
    do tamanho especificado. 
    """
    alfabeto_completo = string.ascii_letters
    # Utilizamos 'random.SystemRandom()' para uma aleatoriedade mais forte
    secure_random = random.SystemRandom()
    return ''.join(secure_random.choice(alfabeto_completo) for _ in range(tamanho))

def char_to_num(char):
    """
    Converte uma letra para seu valor numérico (0-25) baseado no seu caso.
    Retorna -1 se não for uma letra alfabética.
    """
    if char.isupper():
        return ALFABETO_MAIUSCULAS.find(char)
    elif char.islower():
        return ALFABETO_MINUSCULAS.find(char)
    return -1 # Não é letra

def num_to_char(num, is_upper):
    """
    Converte um valor numérico (0-25) para a letra correspondente,
    mantendo o caso (maiúsculo ou minúsculo).
    """
    num = num % TAMANHO_ALFABETO # Garante que o número está dentro do intervalo 0-25
    if is_upper:
        return ALFABETO_MAIUSCULAS[num]
    else:
        return ALFABETO_MINUSCULAS[num]

def vernam_cipher(texto, chave, modo='cifrar'):
    """
    Criptografa ou Descriptografa o texto usando a Cifra de Vernam modular.
    (O mesmo código da implementação anterior, garantindo a simetria).
    """
    # 1. Filtra apenas as letras para garantir que a chave combine 1:1 com as letras
    letras_texto = [char for char in texto if char.isalpha()]
    letras_chave = [char for char in chave if char.isalpha()]

    if len(letras_texto) != len(letras_chave):
        raise ValueError("ERRO: O número de letras no texto e na chave deve ser idêntico.")

    resultado = list(texto)
    indice_chave = 0

    for i in range(len(texto)):
        char_texto = texto[i]
        
        if char_texto.isalpha():
            char_chave = letras_chave[indice_chave]
            
            valor_texto = char_to_num(char_texto)
            
            # A chave é mapeada no mesmo caso da letra do texto para o cálculo ser consistente
            is_upper = char_texto.isupper()
            chave_para_calculo = char_chave.upper() if is_upper else char_chave.lower()
            valor_chave = char_to_num(chave_para_calculo)

            if modo == 'cifrar':
                # CRIPTOGRAFIA: (Plano + Chave) mod 26
                valor_resultante = valor_texto + valor_chave
            elif modo == 'decifrar':
                # DESCRIPTOGRAFIA: (Cifrado - Chave) mod 26
                valor_resultante = valor_texto - valor_chave
            else:
                raise ValueError("Modo inválido. Use 'cifrar' ou 'decifrar'.")

            # Converte o resultado numérico de volta para letra
            resultado[i] = num_to_char(valor_resultante, is_upper)
            
            indice_chave += 1
    
    return "".join(resultado)

# --- Função de Interação do Usuário (Main) ---

def vernam_interface_decifrar():
    print("\n--- Cifra de Vernam (OTP) - MODO DECIFRAR ---")
    print("Para decifrar, você deve possuir a chave OTP correta e o texto cifrado.")
    
    # Seleção de Modo
    while True:
        modo = input("Você quer [C]ifrar ou [D]ecifrar? (C/D): ").upper()
        if modo in ['C', 'D']:
            break
        print("Opção inválida. Digite C para Cifrar ou D para Decifrar.")

    try:
        if modo == 'C':
            # MODO CIFRAR (Opcional, para gerar um exemplo de decifrar)
            plaintext = input("\nDigite a MENSAGEM (Texto Plano): ")
            letras_plaintext = ''.join(filter(str.isalpha, plaintext))
            key_len = len(letras_plaintext)
            
            if key_len == 0:
                print("Mensagem sem letras para cifrar.")
                return

            key = gerar_chave_otp(key_len)
            ciphertext = vernam_cipher(plaintext, key, modo='cifrar')
            
            print("-" * 50)
            print(f"[CHAVE GERADA] Use esta chave para decifrar: {key}")
            print(f"[TEXTO CIFRADO] Use este texto para decifrar: {ciphertext}")
            print("-" * 50)

        elif modo == 'D':
            # MODO DECIFRAR (Foco da sua requisição)
            ciphertext = input("\nDigite o TEXTO CIFRADO: ")
            key = input("Digite a CHAVE OTP (Deve ser a chave original!): ")

            # Valida a regra fundamental do OTP
            letras_ciphertext = ''.join(filter(str.isalpha, ciphertext))
            letras_key = ''.join(filter(str.isalpha, key))
            
            if len(letras_ciphertext) != len(letras_key):
                 raise ValueError("O número de letras no texto cifrado e na chave não coincide. O OTP falhou.")
            
            # Decifrar a mensagem
            decrypted_text = vernam_cipher(ciphertext, key, modo='decifrar')
            
            print("-" * 50)
            print(f"[DESCRIPTOGRAFIA] Texto Original Decifrado: {decrypted_text}")
            print("-" * 50)
            
    except ValueError as e:
        print(f"\nERRO de OTP: {e}")

if __name__ == "__main__":
    vernam_interface_decifrar()