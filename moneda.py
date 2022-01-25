import random

def simulaciónMoneda():
    return random.randint(0,1)

def lanzamiento(rep = 1):
    resultados = [0, 0]
    for i in range(rep):
        lanzamiento = simulaciónMoneda()
        if lanzamiento == 0:
            resultados[0] += 1
        else:
            resultados[1] += 1
    return resultados

def análisisMoneda():
    tries = [3, 5, 50, 200]

    for i in range(5):
        print(f" ---- {i} iteración ----")
        for j in tries:
            print(f"{j} lanzamientos")
            r = lanzamiento(j)
            print(f"{r[0]} caras, {r[1]} cruces")
            print("")


análisisMoneda()

def reto():
    intentos = 0

    carasSimultaneas = 0
    for i in range(10):
        if carasSimultaneas > 3:
            return True

        intentos += 1
        moneda = simulaciónMoneda()
        if moneda == 0:
            carasSimultaneas += 1
        else:
            carasSimultaneas = 0
    return False



if __name__ == "__madfin__":
    resultados = [0, 0]
    for i in range(200):
        if reto():
            resultados[0] += 1
        else:
            resultados[1] += 1
    print(resultados)