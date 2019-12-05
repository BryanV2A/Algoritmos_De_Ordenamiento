class Arreglos:

    def EliminarDuplicados(self, Arreglo):

        Arreglo_Ordenado = []

        for elemento in Arreglo:
            if not elemento in Arreglo_Ordenado:
                Arreglo_Ordenado.append(elemento)

        return Arreglo_Ordenado

Arreglo = [4, 7, 11, 4, 9, 5, 11, 7, 3, 5]
Ordenar = Arreglos()
Resultado = Ordenar.EliminarDuplicados(Arreglo)
print(Resultado)