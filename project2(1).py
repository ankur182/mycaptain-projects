# Python program to print positive Numbers in a List
  
# list of numbers
list = [-10, 21, -4, -45, -66, 93]
n = 0
  
# using while loop     
while(n < len(list)):
      
    # checking condition
    if list[n] >= 0:
        print(list[n], end = " ")
      
    n+= 1