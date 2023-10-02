exp = input ("Digite a sequencia de parênteses a validar: ")
pilha []
x = 0
while x < len(exp):
    if exp[x] == "(":
        pilha.append("(")
    if exp[x] == ")" :
        pilha.pop(-1)
        x == 1

    if len(pilha) == 0:
        print ("OK")
    else:
        print("ok")       