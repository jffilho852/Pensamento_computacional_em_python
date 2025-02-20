def soma(n1,n2):
    resultado = n1 + n2
    return resultado 

def subtracao(n1,n2):
    resultado = n1 - n2
    return resultado 

def multiplicacao(n1,n2):
    resultado = n1 * n2
    return resultado 

def divisao(n1,n2):
    if n2 == 0 :
        return print("NAO É POSSIVEL REALIZAR DIVISAO POR ZERO ")
        
    else:
        resultado = n1 / n2

        return resultado 

def definir_numero1():
    numero1 = int(input("informe o primeiro numero:"))
    return numero1 

def definir_numero2():
    numero2 = int(input("informe o segundo numero:"))
    return numero2


def calculadora():
    while True:
        print("""
==========Calculadora simples========= 
==========informe a operaçao==========
[1].soma 
[2].subtracao
[3].multiplicacao
[4].Divisao 
[s].Sair            
""")
        escolher_acao = input("Escolha a operacao que deseja realizar:")
        if escolher_acao == "1":
            print(f"O RESULTADO DA SOMA É : {soma(definir_numero1(),definir_numero2())}")
        elif escolher_acao == "2":
            print(f"O RESULTADO DA SUBATRACAO É : {subtracao(definir_numero1(),definir_numero2())}")
        elif escolher_acao == "3":
            print(f"O RESULTADO DA SOMA É : {multiplicacao(definir_numero1(),definir_numero2())}")
        elif escolher_acao == "4":
            divisao(definir_numero1(),definir_numero2())
        elif escolher_acao == "s" or "S":
            print("OBRIGADO POR UTILIZAR NOSSA CALCULADORA")
            print("SAINDO...")
            break
        else:
            print("INFORME UMA AÇAO VALIDA ")
        


calculadora()
