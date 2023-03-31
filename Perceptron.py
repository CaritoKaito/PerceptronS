import random
class Perceptron:

    def __init__(self, n_bits, compuerta, epoch):
        self.n_bits = n_bits
        self.compuerta = compuerta
        self.epoch = epoch
        self.bias = 0  
        self.pesos = [random.randint(1, 10) for _ in range(n_bits)]

    def activacion(self, entradas):
        suma = sum([peso * entrada for peso,
                   entrada in zip(self.pesos, entradas)]) + self.bias  
        # agregamos el bias a la suma ponderada
        # la función de activación es la función escalón unitario
        return 1 if suma >= 0 else 0

    def entrenar(self):
        if self.compuerta == "NOT" and self.n_bits != 1:
            print("Compuerta NOT solo funciona con 1 bit")
            return SystemExit
        for ep in range(self.epoch):
            for entrada, salida_esperada in self.tabla_verdad():
                salida_obtenida = self.activacion(entrada)
                if salida_esperada != salida_obtenida:
                    signo = 1 if salida_esperada > salida_obtenida else -1
                    self.bias += signo * 1  # actualizamos el bias
                    self.pesos = [peso + signo * entrada[i]
                                  for i, peso in enumerate(self.pesos)]
        print(f"Aprendizaje exitoso para la epoca:{ep}")
        print(f"Valor del Bias = {self.bias}")
        print(f"Valor de los Pesos = {self.pesos}")

    def evaluar(self, entrada):
        if len(entrada) != self.n_bits:
            print("La cantidad de bits dada no es igual a el numero de bits entrenados")
            return SystemExit
        salida = self.activacion(entrada)
        salida_esperada = bool(self.tabla_verdad()[int(
            "".join(str(i) for i in entrada), 2)][1])
        print(f'Salida esperada: {salida_esperada}')
        print(f'Salida obtenida: {salida}')
        return salida == salida_esperada

    def tabla_verdad(self):
        n = self.n_bits
        if self.compuerta == "AND":
            return [([int("{0:b}".format(i).zfill(n)[j]) for j in range(n)], int(all([int("{0:b}".format(i).zfill(n)[j]) for j in range(n)]))) for i in range(2**n)]
        elif self.compuerta == "OR":
            return [([int("{0:b}".format(i).zfill(n)[j]) for j in range(n)], int(any([int("{0:b}".format(i).zfill(n)[j]) for j in range(n)]))) for i in range(2**n)]
        elif self.compuerta == "NOT":
            return [([0], 1), ([1], 0)]
        else:
            print("Compuerta desconocida")
            raise SystemExit

    def tt(self):
        for entrada, salida_esperada in self.tabla_verdad():
            salida_obtenida = self.activacion(entrada)
            salida_esperada = bool(salida_esperada)
            print(f"{entrada}:{salida_obtenida == salida_esperada}")
