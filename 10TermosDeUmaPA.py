print("=" * 35)
print("      10 TERMOS DE UMA PA    ")
print("=" * 35)
pt1 = int(input("Digite o primeiro termo: "))
r = int(input("Digite a razão: "))
termo = pt1
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total :
        print("{} -> ".format(termo), end="")
        termo += r
        cont +=1
    print("PAUSA")
    mais = int(input("Quantos termos voce quer mostrar a mais? "))
    print("Progressão finalizada com {} termos mostrados".format(total))