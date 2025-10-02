import os
import random

def gerar_chave_otp(tamanho):
    """
    Gera uma chave OTP verdadeiramente aleatória do tamanho especificado.
    
    Atenção: 'os.urandom' é a melhor opção para aleatoriedade criptográfica,
    mas em um cenário real, a chave deve ser gerada por uma fonte de entropia
    física e trocada de forma segura.
    """
    # A chave deve ser gerada por uma fonte de aleatoriedade criptográfica forte
    return os.urandom(tamanho)

def vernam_cipher_xor(dados, chave):
    """
    Criptografa ou Descriptografa os dados usando a Cifra de Vernam (OTP)
    com a operação XOR.
    
    :param dados: Sequência de bytes do texto plano ou texto cifrado.
    :param chave: Sequência de bytes da chave OTP. Deve ter o mesmo tamanho.
    :return: Sequência de bytes do texto cifrado ou texto plano.
    :raises ValueError: Se o tamanho dos dados e da chave for diferente.
    """
    if len(dados) != len(chave):
        raise ValueError("O tamanho da chave deve ser idêntico ao tamanho dos dados (One-Time Pad).")

    # Realiza a operação XOR byte a byte
    resultado = bytes([dado ^ chave_byte for dado, chave_byte in zip(dados, chave)])
    
    return resultado

# --- Exemplo de Uso ---

# 1. Defina a mensagem (Texto Plano)
texto_plano = input("Digite a mensagem: ")
dados_plano = texto_plano.encode('utf-8') # Converte a string para bytes

# 2. Gere a chave OTP (com o mesmo tamanho da mensagem)
tamanho_chave = len(dados_plano)
chave_otp = gerar_chave_otp(tamanho_chave)

print(f"Texto Plano Original: {texto_plano}")
# print(f"Chave OTP (bytes - visualização parcial): {chave_otp[:10]}...") 
print("-" * 30)

## Criptografia
# 3. Criptografe o Texto Plano usando a chave OTP
dados_cifrados = vernam_cipher_xor(dados_plano, chave_otp)
texto_cifrado_hex = dados_cifrados.hex() # Representação em hexadecimal para visualização

print(f"Texto Cifrado (Hex): {texto_cifrado_hex}")
print("-" * 30)

## Descriptografia
# 4. Descriptografe o Texto Cifrado usando a *mesma* chave OTP
# Note que a mesma função é usada (simetria do XOR: A ^ B ^ B = A)
dados_descriptografados = vernam_cipher_xor(dados_cifrados, chave_otp)
texto_descriptografado = dados_descriptografados.decode('utf-8') # Converte os bytes de volta para string

print(f"Texto Descriptografado: {texto_descriptografado}")