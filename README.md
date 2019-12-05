#ALGORITMOS DE ORDENAMIENTO

###Algoritmos de ordenamiento

 En una colección de elementos, el objetivo es reorganizarlos
 para tenerlos en ordenen de menor a mayor (o producir una nueva 
 copia de la secuencia con ese orden o tambien inversamente). 
 
 En Python, el orden natural de los objetos se define típicamente 
 utilizando el operador *"<"* tiene las siguientes propiedades:
 
 - Propiedad irreflexiva: k < k. 
 
 - Propiedad transitiva: if k1 < k2 y k2 < k3, luego k1 < k3.
  
 La propiedad transitiva es importante ya que nos permite 
 inferir el resultado de ciertas comparaciones sin tomar el tiempo para realizar 
 esas comparaciones, lo que conduce a algoritmos más eficientes.

Fuente: Goodrich, M. T., Tamassia, R., & Goldwasser, M. H. (2013). Data Structures and Algorithms in Python, (pág. 537).
 River Street: John Wiley & Sons, Inc
 #
####Problema 1:
 
Se desea eliminar todos	los	números	duplicados de una lista o vector (array).

Por ejemplo, si	el array toma los valores	

    4	7	11	4	9	5	11	7	3	5 

ha de cambiarse a	

    4	7	11	9	5	3 

Escribir un	método que elimine los elementos duplicados de un array.

*"Resuleto en el archivo EliminarElementosRepetidos"*

#

####Problema 2:

Se leen dos	listas de números enteros, A y B, de 100 y 60 elementos, respectivamente.
Se desea resolver las siguientes tareas: 

- a) Ordenar aplicando el método de Quicksort cada una de las listas A y B.

- b) Crear una lista	C por intercalación	o mezcla de	las	listas A y B.

- c) Visualizar la lista C ordenada.

*"Resuleto en el archivo OrdenarArreglos"*