A = input('Enter the value of A\n')
B = input('Enter the value of B\n')
C = input('Enter the value of C\n')

A = int(A)
B = int(B)
C = int(C)


Asq = A * A
Bsq = B * B
Csq = C * C

if Asq + Bsq == Csq or Asq + Csq == Bsq or Csq + Bsq == Asq:
    print("right\n")
else:
    print("wrong\n")

