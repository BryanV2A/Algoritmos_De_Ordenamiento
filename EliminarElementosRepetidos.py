class Arreglos:

    # Método encargado de eliminar elementos repetidos en un arreglo
    def EliminarDuplicados(self, Arreglo):

        Arreglo_Ordenado = []

        # Ciclo for para comparar elemtos iguales en el arreglo
        for elemento in Arreglo:
            if not elemento in Arreglo_Ordenado:
                Arreglo_Ordenado.append(elemento)

        return Arreglo_Ordenado

# Declaración del arreglo a ordenar
Arreglo = [4, 7, 11, 4, 9, 5, 11, 7, 3, 5]

#Creación del objeto y acceso o salto al método EliminarDuplicado
Ordenar = Arreglos()
Resultado = Ordenar.EliminarDuplicados(Arreglo)

print(Resultado)    # Mensaje para imprimir el resultado del Arreglo