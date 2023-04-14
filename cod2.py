num = int(input("Digite um número: "))

fib1, fib2 = 0, 1
while fib2 < num:
    fib1, fib2 = fib2, fib1 + fib2

if fib2 == num:
    print(num, "pertence à sequência de Fibonacci.")
else:
    print(num, "não pertence à sequência de Fibonacci.")
