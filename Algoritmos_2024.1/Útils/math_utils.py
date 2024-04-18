#Verifica se dois números são iguais
def eh_igual(num1, num2):
    if num1 == num2:
        return True

    return False

#Verifica se um número é par
def eh_par(num):
    if num % 2 == 0:
        return True
    
    return False

#Verifica se um número é ímpar
def eh_impar(num):
    if num % 2 != 0:
        return True
    
    return False

#Verifica se um número é primo (Válido apenas para números entre 0 e 100)
def eh_primo(num):
    dezena = num // 10
    unidade = num % 10

    if ((num != 2 and num % 2 == 0) or (num != 3 and (dezena + unidade) % 3 == 0) or 
    (num != 5 and unidade % 5 == 0) or (num != 7 and num % 7 == 0)):
        return True
    
    return False

#Retorna o maior entre dois números (Ignorando casos de números iguais)
def checar_maior(num1, num2):
    if num1 > num2:
        return num1
    elif num2 > num1:
        return num2

#Retorna o menor entre dois números (Ignorando casos de números iguais)
def checar_menor(num1, num2):
    if num1 > num2:
        return num1
    elif num2 > num1:
        return num2

#Separa números com duas casas decimais
def dividir_dezena(num):
    dezena = num // 10
    unidade = num % 10

    return dezena, unidade

#Separa números com três casas decimais
def dividir_centena(num):
    centena = num // 100
    resto = num % 100
    dezena, unidade = dividir_dezena(resto)

    return centena, dezena, unidade

#Separa números com quatro casas decimais
def dividir_milhar(num):
    milhar = num // 1000
    resto = num % 1000
    centena, dezena, unidade = dividir_centena(resto)
    
    return milhar, centena, dezena, unidade

#Calcula a média aritmética
def calcular_media_aritmetica(somatorio, quant_elementos):
    return somatorio / quant_elementos

#Verifica se os lados digitados formam um triângulo
def eh_triangulo(maior_lado, lado_menor1, lado_menor2):
    if lado_menor1 + lado_menor2 > maior_lado:
        return True
    
    return False

#Verifica se um valor é positivo
def eh_positivo(num):
    if num > 0:
        return True
    
    return False
    
#Verifica se um valor é negativo
def eh_negativo(num):
    if num < 0:
        return True
    
    return False

#Verifica se um valor é nulo (0)
def eh_nulo(num):
    if num == 0:
        return True
    
    return False

#Calcula o módulo de um número
def calcular_modulo(num):
    if num >= 0:
        return num
    
    return num * (-1)
