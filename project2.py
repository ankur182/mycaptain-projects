#write a program of fibonacci series
f=0
s=1
n=int(input("enter no. of terms"))
print(f,s,end=" ")
for i in range(3,n+1):
	t=f+s
	print(t,end=" ")
	f=s
	s=t