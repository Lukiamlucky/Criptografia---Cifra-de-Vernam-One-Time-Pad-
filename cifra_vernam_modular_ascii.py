import random
import string

# Define os alfabetos para mapeamento
ALFABETO_MAIUSCULAS = string.ascii_uppercase  # 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ALFABETO_MINUSCULAS = string.ascii_lowercase  # 'abcdefghijklmnopqrstuvwxyz'
TAMANHO_ALFABETO = 26

def gerar_chave_otp_alfabetica(tamanho):
    """
    Gera uma chave OTP aleatória contendo letras (maiúsculas e minúsculas)
    do tamanho especificado. 
    """
    alfabeto_completo = string.ascii_letters
    return ''.join(random.choice(alfabeto_completo) for cada in range(tamanho))
def vernam_modular_completo(texto, chave, modo='criptografia'):
    """
    Implementa a Cifra de Vernam usando aritmética modular (mod 26) 
    para maiúsculas e minúsculas, preservando o caso.

    :param texto: Texto plano (ou cifrado)
    :param chave: Chave OTP de mesmo comprimento das letras no texto.
    :param modo: 'criptografar' ou 'descriptografar'.
    :return: Texto cifrado (ou plano) resultante.
    """
    
    # Remove caracteres não alfabéticos do texto e da chave para garantir 
    # que a chave só combine com letras. Isso simplifica o controle de tamanho.
    letras_texto = [caracter for caracter in texto if caracter.isalpha()]
    letras_chave = [caracter for caracter in chave if caracter.isalpha()]

    if len(letras_texto) != len(letras_chave):
        raise ValueError("A chave deve ter o mesmo número de letras que o texto para o OTP idealizado.")

    resultado = list(texto)
    indice_chave = 0

    # Iteramos sobre a posição original do texto para preservar espaços e pontuação
    for caracter in range(len(texto)):
        caracter_texto = texto[caracter]
        
        if caracter_texto.isalpha():
            caracter_chave = letras_chave[indice_chave]

            if caracter_texto.isupper():
                # Processamento para MAIÚSCULAS
                alfabeto = ALFABETO_MAIUSCULAS
            else:
                # Processamento para MINÚSCULAS
                alfabeto = ALFABETO_MINUSCULAS
            
            # Garante que a chave correspondente também seja tratada no mesmo caso para o cálculo de índice
            valor_chave = alfabeto.index(caracter_chave.upper() if caracter_texto.isupper() else caracter_chave.lower())

            # 1. Converte letra para valor numérico (A/a=0, Z/z=25)
            valor_texto = alfabeto.index(caracter_texto)
            
            if modo == 'criptografia':
                # 2. CRIPTOGRAFIA: (Plano + Chave) mod 26
                valor_resultante = (valor_texto + valor_chave) % TAMANHO_ALFABETO
            else:
                # 2. DESCRIPTOGRAFIA: (Cifrado - Chave) mod 26
                valor_resultante = (valor_texto - valor_chave) % TAMANHO_ALFABETO

            # 3. Converte o valor numérico de volta para letra
            resultado[caracter] = alfabeto[valor_resultante]
            
            # Avança para o próximo caractere da chave apenas se foi uma letra processada
            indice_chave += 1
    
    return "".join(resultado)

# --- Exemplo de Uso ---

# 1. Defina a mensagem (com maiúsculas, minúsculas e outros caracteres)
texto_plano = input("Mensagem Secreta OTP, 100% Simetrica.: " )
print(f"Texto Plano Original: {texto_plano}")

# 2. Gere a chave OTP: O tamanho da chave deve ser igual ao NÚMERO DE LETRAS no texto.
tamanho_para_chave = sum(1 for char in texto_plano if char.isalpha())
chave_otp = gerar_chave_otp_alfabetica(tamanho_para_chave)

print(f"Chave OTP Gerada:     {chave_otp}")
print("-" * 50)

# --- Criptografia ---
texto_cifrado = vernam_modular_completo(texto_plano, chave_otp, modo='criptografar')

print(f"Texto Cifrado:        {texto_cifrado}")
print("-" * 50)

# --- Descriptografia ---
texto_descriptografado = vernam_modular_completo(texto_cifrado, chave_otp, modo='descriptografar')
print(f"Texto Descriptografado: {texto_descriptografado}")