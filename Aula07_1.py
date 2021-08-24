# Instrução Return
# Instruções condicionais

"""

def cubo(num):
    return num * num * num

result = cubo(5)
print(result)

"""

"""

acordei = True 
fome = False 

if acordei and fome:
    print("Eu faço meu café da manha")
elif acordei == True and fome == False:   
    print("Acordei mas estou sem fome") 
else:
    print("Estou dormindo")  
     
"""

"""

saindo_casa = True
nublado = True

if saindo_casa and nublado:
    print("Eu vou pegar meu guarda-chuva")
elif saindo_casa == True and nublado == False:
    print("Eu pego meu oculos de sol")
else:
    print("Fico em casa")
    
"""

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else: 
        return num3

print(max_num(11, 11.5, 5))
