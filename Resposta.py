def verifica_fibonacci(numero):
    # Inicializa os dois primeiros números da sequência de Fibonacci
    a, b = 0, 1
    # Continua calculando os próximos números da sequência até que b seja menor que o número fornecido
    while b < numero:
        # Atualiza os valores de a e b para os próximos números na sequência
        a, b = b, a + b
    # Verifica se o número fornecido está na sequência de Fibonacci
    if b == numero:
        return True
    else:
        return False

def inverte_string(string):
    # Inicializa uma string vazia para armazenar a string invertida
    string_invertida = ''
    # Itera sobre os caracteres da string original em ordem reversa
    for i in range(len(string)-1, -1, -1):
        # Adiciona cada caractere à string invertida
        string_invertida += string[i]
    # Retorna a string invertida
    return string_invertida

# 1) Valor da variável SOMA ao final do processamento
INDICE = 13
SOMA = 0
K = 0

while K < INDICE:
    K = K + 1
    SOMA = SOMA + K

print("Resposta 1): Valor de SOMA ao final:", SOMA)

# 2) Verifica se um número pertence à sequência de Fibonacci
numero_fibonacci = 21

if verifica_fibonacci(numero_fibonacci):
    print(numero_fibonacci, "pertence à sequência de Fibonacci.")
else:
    print(numero_fibonacci, "não pertence à sequência de Fibonacci.")

# 3) Completando as sequências lógicas
resposta_3a = 7 + 2  # 9
resposta_3b = 64 * 2  # 128
resposta_3c = 36 + 13  # 49
resposta_3d = 8 ** 2  # 64
resposta_3e = 5 + 8  # 13
resposta_3f = 19 + 1  # 20

print("Respostas 3):")
print("a) Próximo número:", resposta_3a)
print("b) Próximo número:", resposta_3b)
print("c) Próximo número:", resposta_3c)
print("d) Próximo número:", resposta_3d)
print("e) Próximo número:", resposta_3e)
print("f) Próximo número:", resposta_3f)

# 4) Descobrir qual interruptor controla cada lâmpada
print("Resposta 4):")
print("Para descobrir, primeiro ligue um interruptor por alguns minutos e depois desligue-o.")
print("Em seguida, ligue outro interruptor e entre na sala. A lâmpada que estiver acesa estará conectada ao segundo interruptor,")
print("a lâmpada que estiver quente estará conectada ao primeiro interruptor (pois foi ligada e depois desligada, mas já esteve ligada anteriormente)")
print("e a lâmpada que estiver fria e apagada estará conectada ao terceiro interruptor.")

# 5) Inverter os caracteres de uma string
string_original = "Exemplo"  # String definida previamente no código
string_invertida = inverte_string(string_original)
print("Resposta 5):")
print("String original:", string_original)
print("String invertida:", string_invertida)
