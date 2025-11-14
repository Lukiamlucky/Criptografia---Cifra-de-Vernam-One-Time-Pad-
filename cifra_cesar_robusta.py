import string 

# --- Cifra de César ---

# O Alfabeto (letras, dígitos, alguns símbolos e acentos) que serão cifrados.
# Caracteres que não estão nesta string (como espaço, vírgula, etc.) serão ignorados.
alfabeto = string.ascii_letters + string.digits + "!?-()ÁÉÍÓÚÀÈÌÒÙÃÕÂÊÎÔÛÇ" + "áéíóúàèìòùãõâêîôûç"
# N é o tamanho do alfabeto, o módulo da nossa operação criptográfica.
N = len(alfabeto)

# --- Funções de Mapeamento (Tradução) ---
def letra_num(c): 
    """Retorna o índice numérico (P) do caractere no alfabeto."""
    return alfabeto.find(c)

def num_letra(i):
    """
    Converte um índice numérico de volta para o caractere correspondente.
    A operação 'i % N' (MÓDULO N)
    """
    return alfabeto[i % N]

# --- Algoritmo Central de Processamento ---

def processa(texto, chave, modo='criptografia'):
    """Executa a cifragem ou decifragem, aceitando chaves de qualquer tamanho."""
    
    # Validação inicial para garantir que o modo de operação é válido.
    if modo not in ('criptografia', 'descriptografia'):
        raise ValueError("modo deve ser 'criptografia' ou 'descriptografia'")
    
    # Define o Fator de Deslocamento (K).
    # Se decifrando, K é negativo. Usar a chave bruta (sem módulo ) garante 
    # que a decifragem funcione com a lógica de módulo em 'num_letra'.
    K = chave if modo == 'criptografia' else -chave
    
    resultado = []
    for c in texto:
        if c in alfabeto:
            # 1. Obtém a posição P.
            P = letra_num(c)
            # 2. Aplica o deslocamento: C = P + K.
            # 3. Converte para o caractere final (usando módulo N).
            resultado.append(num_letra(P + K))
        else:
            # Mantém qualquer caractere que não esteja no alfabeto (ex: espaço, :)
            resultado.append(c)
            
    return "".join(resultado)

# --- Interface do Usuário ---

def menu():
    """Controla o loop de interação com o usuário e a validação de entradas."""
    while True:
        # Formatação do Menu
        print("\n" + "="*50)
        print("   C I F R A   D E   C É S A R   (SIMÉTRICA)")
        print("="*50)
        print(f"Alfabeto: {N} caracteres")
        print("1. Criptografia\n2. Descriptografia\n3. Sair")

        escolha = input("\nEscolha (1, 2 ou 3): ").strip()
        if escolha == "3":
            print("Encerrado.")
            break
        if escolha not in {"1", "2"}:
            print("Opção inválida.")
            continue

        modo = 'criptografia' if escolha == "1" else 'descriptografia'
        texto = input(f"\nDigite o texto para {modo}: ")

        # Validação de CHAVE: Garante que a entrada seja um número inteiro.
        while True:
            try:
                chave = int(input("Digite a CHAVE de deslocamento (K): "))
                break
            except ValueError:
                print("A chave deve ser um número inteiro.")

        # Execução e Saída do Resultado
        resultado = processa(texto, chave, modo=modo)
        print("-"*50)
        print(f"MODO: {modo.upper()} | CHAVE: {chave}")
        print(f"RESULTADO: {resultado}")
        print("-"*50)

if __name__ == "__main__":
    menu()