n=int(input("enter n value:"))
fact=0
for i in range(1,n):
	if n%i==0:
		print(i)
		fact+=1
print(fact)