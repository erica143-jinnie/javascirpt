num = int(input("Enter the number : "))
t = num
numlen = 0
while t>0:
  numlen = numlen+1
  t = int(t/10)
if numLen>=4:
  numLen = int(numLen/2)
  chk = 0
  while num>0:
    rem = num%10
    if chk==numLen:
     midTwo = rem
    num = int(num/10)
    chk = chk+1
  prod = midOne*midTwo 
  print ("\nproduct of mid digits"(" +str(midOne)+ "*" +str(midTwo)+ ") = ", prod)

else:
  print("\nIt's not a 4 or more than 4-digit number!")"))
