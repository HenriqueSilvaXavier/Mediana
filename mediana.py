números=[]
while True:
	k=int(input("Digite um número: "))
	números.append(k)
	r=input("Quer continuar?[S/N] ")
	if r in "Nn":
		break
	while r not in "Ss":
		r=input("Quer continuar?[S/N] ")
números=sorted(números)
if len(números)%2==1:
	n=len(números)//2
	mediana=números[n]
if len(números)%2==0:
	n=(len(números)-1)//2
	mediana=(números[n]+números[n+1])/2
print("A quantidade de números é {}.".format(len(números)))
print("A mediana da lista é {}.".format(mediana))