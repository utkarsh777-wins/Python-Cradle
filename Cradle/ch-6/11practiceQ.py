#factorial function
# n = 5
# fact = 1
# for i in range(1, n+1):
#     fact *= i
# print(fact)

def fact_fn(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)

fact_fn(5)