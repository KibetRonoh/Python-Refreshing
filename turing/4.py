# what is the output of the following code?

print(2**(3**2), (2**(3**2, (2**(3**3)

#(512, 512, 1342177728)

 2**(3**2)
 (2**3)**2
 2**3**2

Answer: d
Explanation: Expression 1 is evaluated as 2**9, which is equal to 512. Expression 2 is evaluated as 8**2, which is equal to 64. The last expression is evaluated as 2**(3**2). This is because the associativity of ** operator is from right to left. Hence the result of the third expression is 512.