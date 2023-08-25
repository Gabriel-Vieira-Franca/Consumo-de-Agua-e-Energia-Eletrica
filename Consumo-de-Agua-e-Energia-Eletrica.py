#software de consumo

#Login

#Cadastro de produtos elétricos
cad = float(input("Deseja cadastrar produto? (1-sim ou 2-não) "))
while (cad == 1):
    nome = input("Nome do aparelho: ")
    temp = float(input("Tempo de uso em horas: "))
    pot = float(input("Potência (Watt): "))
    
    kwh = float(pot/1000)*temp
    reais = kwh*0.649
    print (f"Valor de consumo (em R$): {reais}")
    print ("________________________________")
    cad = float(input("Deseja cadastrar produto? (1-sim ou 2-não) "))



