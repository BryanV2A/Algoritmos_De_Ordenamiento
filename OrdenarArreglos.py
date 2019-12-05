from random import *

# Declaración de Clase QuickSort para ordenar los arreglos
class QuickSort:
    A = []
    B = []
    C = []

    def intercambia(self, a, x, y):
        tmp = a[x]
        a[x] = a[y]
        a[y] = tmp

    def Particionar(self, a, p, r):
        x = a[r]
        i = p - 1
        for j in range(p, r):
            if (a[j] <= x):
                i = i + 1
                self.intercambia (a, i, j)
        self.intercambia(a, i+1, r)
        return i + 1

    def QuickSort(self, a, p, r):
        if (p < r):
            q = self.Particionar(a, p, r)
            #print (A[p:r])
            self.QuickSort(a, p, q-1)
            self.QuickSort(a, q+1, r)
        return a

    def ordenar(self, a):
        p = 0
        r = len(a) - 1
        q = int((p + r) / 2)
        return self.QuickSort(a, p, r)

    # Método encargado de generar dos arreglos uno de 100 elementos y el segundo de 60, ambos con números aleatorios
    def Generar_Areglos(self):

        for a in range(0, 100):
            self.A.append(randrange(1, 1000))

        for b in range(0, 60):
            self.B.append(randrange(1, 1000))

    #  Método encargado de ordenar los arreglos creando dentro del método un objeto para realizar saltos al método
    #  ordenamiento de la clase QuickSort
    def OrdenarArreglos(self):

        ordenar = QuickSort()

        # Arreglo A
        ordenar.ordenar(self.A)
        print('Arreglo "A" ordenado: ', self.A)

        # Arreglo B
        ordenar.ordenar(self.B)
        print('Arreglo "B" ordenado: ', self.B)

        # Arreglo C
        self.C = self.A
        self.C.extend(self.B)
        ordenar.ordenar(self.C)
        print('Arreglo "C" ordenado: ', self.C)

#Creación del objeto y acceso o salto a los método Generar y Ordenar Arreglos
ordenar = QuickSort()
ordenar.Generar_Areglos()
ordenar.OrdenarArreglos()