Finterms = int(input("Number of terms to be printed "))
n1, n2 = 0, 1
count = 0
if nterms <= 0:
   print("Enter a vaild positive integer")
elif nterms == 1:
   print("Fibonacci sequence upto",nterms, "is ")
   print(n1)
else:
   print("Fibonacci sequence is")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1
