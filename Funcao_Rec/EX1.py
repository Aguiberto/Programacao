def conta_divisores(n,d):
    if d == 1:
        contador = 1
        return contador
    else:
        contador = 0
        if n % d == 0:
            contador = 1
        return contador + conta_divisores(n, d - 1)

d, n = map(int, (input("Digite um número: ").split()))

divisores = conta_divisores(n,d)
print(f"O número {n} tem {divisores} divisores entre 1 e {d}.")

