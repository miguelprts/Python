from datetime import datetime 

#variáveis essenciais
valor_inserido = 0
LIMITE_TOTAL_SAQUES = 500
QUANTIDADE_TOTAL = 3

saldo = 0
extrato =''

opc = 0

menu = """
=================== Banco Meu Cofrinho ===================

Insira um dos digitos à seguir para realizar alguma operação:
    [1]: Depósito
    [2]: Saque
    [3]: Extrato
    [4]: Sair   
    : """

while True:

    opc = int(input(menu))
    #deposito
    if opc == 1:
        valor_inserido = float(input("Insira o valor: R$"))

        if valor_inserido < 0:
            print("Não é aceito valores negativos! ")
        else:
            saldo += valor_inserido
            extrato += f"DEPÓSITO DE R${valor_inserido:.2f}.\n"

    #saque
    elif opc == 2:
        valor_inserido = float(input("Insira o valor: R$"))

        if (valor_inserido > LIMITE_TOTAL_SAQUES) and (QUANTIDADE_TOTAL > 3):
             print("Atingiu o valor de saques diários permitidos! Tente novamente amanhã.")
        
        elif (valor_inserido > saldo):
            print("Você não tem este valor em saldo!")

        else:
            saldo -= valor_inserido 
            extrato += f"SAQUE DE R${valor_inserido:.2f}.\n"

    #extrato
    elif opc == 3:
        data = datetime.now().strftime('%d-%m-%Y')
        hora = datetime.now().strftime('%H:%M:%S')

        print(f"""
=================== Banco Meu Cofrinho - Extrato ===================
        Data: {data}                    Hora: {hora}
        Saldo atual: R${saldo:.2f}
        Movimentações:
        {extrato}
====================================================================
        
""")
    else:
        break

    
    #extrato
