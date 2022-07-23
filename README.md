# Comprehensions, Lambdas y manejo de errores.

# El zen de Python

El Zen de Python se compone por los principios para escribir tu código de manera clara, sencilla y precisa. Estos son:

- Bello es mejor que feo:
    - Python es estéticamente superior a cualquier otro lenguaje de programación. Al momento de escribir código, es mejor que sea de manera limpia y estética.
- Explícito es mejor que implícito:
    - Hacer más fácil que las otras personas entiendan el código.
- Simple es mejor que complejo:
    - Es mejor tener una implementación simple, que ocupe pocas líneas de código y sea entendible, a que sea una larga y complicada.
- Complejo es mejor que complicado:
    - Si tenemos que extendernos en la implementación y hacerla más compleja para que el código si se entienda, esto es mejor que hacerlo simple y mal.
- Plano es mejor que anidado:
    - El anidamiento es cuando tenemos un bloque de código dentro de otro bloque de código (dependiento de este). Esto se nota en Python por la identación, nos quuedarían estos bloques muy corridos a la derecha. Es mejor evitar anidamiento y hacer las cosas de manera plana.
- Espaciado es mejor que denso:
    - Por la identación de Python (sus sangrías), este principio se nos hace imposible de esquivar. El código inevitablemente es espaciado.
- La legibilidad es importante:
    - Es importante que otros programadores puedan entender lo que estamos escribiendo. Esto hace más fáciles las cosas cuando trabajamos con otros proyectos.
- Los casos especiales no son lo suficientemente especiales como para romper las reglas (sin embargo), la practicidad le gana a la pureza:
    - Siempre que podamos respetar estas reglas que nos plantea Python, es mejor así. Sin embargo, si por el hecho de hacer un código muy “Pythonista”, este pierde legibilidad, es mejor ser más prácticos o romper saltarnos algunas de estas reglas para que el código sea más eficiente.
- Los errores nunca deberían pasar silenciosamente (a menos que se silencien explicitamente):
    - Manejar los errores es fundamental. Cada error nos dice algo y hay que prestarles atención. A menos que seas capaz de silenciar un error, aunque para esto no hay que tener criterio.
- Frente a la ambiguedad, evitar la tentación de adivinar:
    - Nuestro código debería solamente tener una interpretación. Si en un contexto significa algo, y en otro otra cosa, es mejor que lo revisemos y busquemos una solución.
- Debería haber una y preferiblemente solo una manera obvia de hacerlo:
    - Esto hace referencia a Python “Guido Van Rossum” que de manera muy inteligente encontrar las soluciones precisas a los problemas, y deberíamos imitarlo.
- Ahora es mejor que nunca:
    - Es mejor desarrollar nuestra solución cuánto antes, no dejarlo para mañana o para mas adelante.
- A pesar de que nunca es muchas veces mejor que ahora mismo:
    - Si por hacer las cosas ya y tenemos poco tiempo, si es mejor dejarlo para después y no hacerlo apurado y mal.
- Si la implementación es difícil de explicar, es una mala idea y si es fácil de explicar es buena idea:
    - Si somos capaces de explicar nuestra implementación a otros desarrolladores paso a paso, es una buena idea. En cambio si no podemos hacerlo, significa que ni nosotros entendemos la implementación y deberíamos repensar nuestra forma de encarar la solución.
- Los espacios de nombres son una gran idea, ¡Tengamos más de esos! (namespaces):
    - Es el nombre que se ha indicado luego de la palabra import, es decir la ruta (namespace) del módulo. (Lo veremos a profundidad más adelante).

Para ver el zen de Python es necesario correr la consola interactiva. Esto se hace escribiendo `python3` en ubuntu y colocando `import this`. Este es un módulo oculto secreto que incluye 20 principios de Software.

# La documentación

Es como un manual de usuario, donde te indican usos y todo lo necesario para entender un idioma. No solo los lenguajes tienen su documentación, cada una de las librerías utilziadas tienen la información necesaria para comprender su uso total.

# ¿Qué es un entorno virtual?

Un entorno virtual es un directorio que contiene una instalación de Python de una versión en particular, además de unos cuántos paquetes adicionales.

Los entornos virtuales son de mucha utilidad ya que nos ayudan a tener versiones específicas de librerías o módulos a un proyecto con distintas versiones de la misma librería o modulo.

## Creación de un entorno virtual para Python

Existen muchas maneras de crear un entorno virutal, como desde el mismo Python, utilizando Mamba pero el más recomendado sería Conda. Para este ejemplo se utilizará Python.

Para la creación del ambiente virtual se utiliza `python3 -m venv nombre_ambiente_virtual` 

Para activar el entorno virtual se tiene que ir a la carpeta donde se guardó el entorno y escribir `source nombre_ambiente_virtual/bin/activate`.  Para salir del entorno virtual se utiliza `deactivate`. Una buena manera de activar el entorno virtual es con un alias: alias nombre-`alias”nombre_ambiente_virtual/bin/activate"` . 

## Instalación de dependencias con pip

pip (package installer for Python) nos permite descargar paquetes de terceros para utilizarlos en nuestro enviroment, además se puede definir una versión específica del paquete.

- pip install «paquete»
    - Instala el paquete (pandas, matplotlib, bokeh, numpy, etc) que se especifique,
- pip freeze
    - Muestra todos los paquetes instalados en tu ambiente virtual.
    

Si quisieramos que alguien más pueda ejecutar nuestro proyecto es importante compartir que librería y versión hemos empleado; eso se hace con el comando `pir freeze > requirements.txt`.

El resultado de pip freeze se escribe en el archivo txt. 

Para instalar paquetes desde un archivo como requirements.txt se ejecuta `pip install -r requirements.txt.`

# Listas y diccionarios anidados

```python
def run():
    my_list = [1, "helllo", True, 4.5]
    my_dict = {"firstname": "Jefferson", "lastname": "Rodriguez"}

    super_list = [
        {"firstname": "Jefferson", "lastname": "Rodriguez"},
        {"firstname": "Miguel", "lastname": "Torres"},
        {"firstname": "Pepe", "lastname": "Rodelo"},
        {"firstname": "Chanchito", "lastname": "Feliz"}
    ]

    super_dict = {
        "natural_nums": {1,2,3,4,5},
        "integer_nums": {-1,-2,0,1,2},
        "float_nums": {1.1, 4.5, 6.43}
    }

    for key, value in super_dict.items():
        print(key, '-',value)

    for i in range(len(super_list)):
        print(super_list[i])
        

if __name__ == '__main__':
    run()
```

# List comprehensions

[ element for element in iterable if condition ]

- Element
    - Rerpesenta a cada uno de los elementos a poner en la nueva lista.
- for element in iterable
    - Ciclo a partir del cual se extraerán elementos de otra lista o cualquier iterable.
- if condition
    - condición opcional para filtrar los elementos del ciclo.

```python
# List comprehensions
# Código que guarda los cuadrados del 1 al 100 si es divisble entre 3

def run():

    squares = [i**2 for i in range(1,100) if i % 3 != 0]
    print(squares)
if __name__ == "__main__":
    run()
```

Para cada elemento en el iterable se va a guardar el elemento solo si se cumple la condición.

# Dictionary comprehensions

{ key: value for value in iterable if condition }

- key: value
    - Representa a cada una de las llaves y valores a poner en el nuevo diccionario.
- for value in iterable
    - Ciclo a partir del cual se extraerán elementos de cualquier iterable.
- if condition
    - Condición opcional para filtrar los elementos del ciclo.
    

```python
def run():
    my_dict = {i: i**3 for i in range(1,101) if i % 3 != 0}
    print(my_dict)
if __name__ == "__main__":
    run()
```

```python
def run():

    my_dict = {i : round(i**0.5,2) for i in  range(1,1001)}

    print(my_dict)

if __name__=='__main__':
    run()
```

# Funciones anónimas: lambda

Son funcione que no tienen un identificador. 

```python
lambda argumentos: expresión
```

En lugar de usar def, se utiliza lambda.  Estas pueden tener el valor que nosotros queramos, pero solamente puede tener una línea de código

![https://runestone.academy/runestone/books/published/fopp/_images/lambda.gif](https://runestone.academy/runestone/books/published/fopp/_images/lambda.gif)

1. Las funciones lambda no deberían sustituir a las funciones def en python, usar las funciones lambda para sustituir una funcion def es una mala practica..
2. lambda != arrow_func.Si vienes de Javascript es probable que quieras usar una funcion lambda como si fuera una arrow function, no hagas eso. Una arrow function puede llegar a ser mucho mas completa y estas si pueden sustituir a una función clásica en Javascript..
3. Las Funciones lambda solo deberían de usarse en caso muy específicos o para competencias de programación en las que tengas que programar lo mas rápido posible..
4. Por favor lean esto: [https://stackoverflow.com/questions/25010167/e731-do-not-assign-a-lambda-expression-use-a-def](https://stackoverflow.com/questions/25010167/e731-do-not-assign-a-lambda-expression-use-a-def).
5. En serio es muy importante que lean y entiendan el link del punto anterior si quieren convertirse en unos crack en python!

## Funciones de orden superior: filter, map y reduce

Se tiene el código que imprime un saludo.

La función saludo es de orden superior, dado que recibe como parámetro otra función.

Esta imprime un hola o un adiós.

Existen 3 tipos de funciones de orden superior súper importantes, que son filter, map y reduce.

```python
def saludo(func):
    func()

def hola():
    print("Hola")

def adios():
    print("Adios")

saludo(hola)
saludo(adios)
```

![Untitled](Comprehensions,%20Lambdas%20y%20manejo%20de%20errores%2089ba962f5b6f464ba9d2c8127c59b0ca/Untitled.png)

### Filter

Supongamos que tenemos la lista [1, 4, 5, 6, 9, 13, 19, 21] y queremos obtener de esa lista, la siguiete [1, 5, 9, 13, 19, 21] Esto se puede hacer con list comprehensions y también con una función de orden superior, filter

```python
#Utilizando list comprehensions.
my_list = [1,4,5,6,9,13,19,21]
odd = [i for i in my_list if i % 2 != 0]
odd
```

Este mismo problema se puede resolver con filter:

```python
#utilizando filter

my_list = [1,4,5,6,9,13,19,21]
odd = list(filter(lambda x: x%2 != 0, my_list))
odd
```

*filter* devuelve True or False según el valor esté dentro de los criterios buscados o no. En caso de que no cumpla con la condición, no será devuelto y la lista se verá reducida por este filtro.

### Map

Supongamos que teenemos la lista [1, 2, 3, 4, 5] y queremos convertirla en [1, 4, 9, 16, 25].

```python
#Utilizando list comprehensions
my_list = [1,2,3,4,5]
odd = [i**2 for i in my_list]
odd
```

Esto mismo se puede resolver con map.

```python
#usando map

my_list = [1,2,3,4,5]
squares = list(map(lambda x: x**2, my_list))
squares
```

*Map* funciona muy parecido, pero su diferencia radica en que no puede eliminar valores de la lista del array entregado. Es decir, el output tiene la misma cantidad de valores que el input.

### reduce

Se tiene una lista [2, 2, 2, 2, 2] en 32. 

```python
from functools import reduce

my_list = [2, 2, 2, 2, 2]

all_multiplied = reduce(lambda a, b: a*b, my_list)
all_multiplied
```

Es necesario importar la función reduce de functools dado que esta no viene de forma nativa como las anteriores. Reduce necesita dos valores.

*Reduce* toma 2 valores entregados como parámetros y el iterador como otro parámetro. Realiza la función con estos 2 valores, y luego con el resultado de esto y el valor que le sigue en el array. Y así hasta pasar por todos los valores de la lista.

# Proyecto: filtrando datos

```python
DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

def run():
    #Todos los programadores de python
    all_python_devs = [worker["name"] for worker in DATA if worker["language"] == "python"]

    for worker in all_python_devs:
        print(worker)

    #Todos los trabajadores de platzi
    all_platzi_workers = [worker["name"] for worker in DATA if worker["organization"] == "Platzi"]

    for worker in all_platzi_workers:
        print(worker)

    #Todos los adultos del diccionario utilizando filter
    adults = list(filter(lambda worker: worker['age'] > 18, DATA))
    adults = list(map(lambda worker: worker['name'],adults))
    for worker in adults:
        print(worker)
    #Todos los worker mayores de 70 años
    old_people = list(map(lambda worker: worker | {"old": worker['age']>70},DATA))
    for worker in old_people:
        print(worker)      

if __name__ == '__main__':
    run()
```

# Los errores en el código

El manejo de errores es muy importante y los mejores trucos:

1. Leer el error (Conozco programadores y hasta yo en un inicio trataba de revisar el código sin revisar el traceback)
2. Leer el traceback de abajo hacia arriba

![Untitled](Comprehensions,%20Lambdas%20y%20manejo%20de%20errores%2089ba962f5b6f464ba9d2c8127c59b0ca/Untitled%201.png)

Cuando python nos avisa que tenemos un error en el código nos avienta un mensaje que conocemos como traceback, puesde ser debido a:

- Errores de Sintaxis (SyntaxError)
    - escribimos mal alguna palabra clave (typo), el programa no se ejecuta.
- Excepciones (Exeption)
    - Producen un colapso o interrupción de la lógica del programa en alguna línea en específico por ejemplo (todas las líneas anteriores se ejecutan), pueden ser de varios tipos, generalmente aparecen cuando no existe un componente clave en la ejecución o hay alguna imposibilidad lógica (matemática) para efectuar la instrucción, tambipen pueden generarse dentro del código o fuera de el (elevar una excepción)

**Lectura de un traceback**

- La manera correcta de leer un traceback es iniciar por el final, en el caso de un error de sintaxis nos indicará en qué línea se encuentra dicho error.
- En el caso de excepciones la última línea nos indicará el tipo de exepcion que se generó (generalmente son autoexplicativas pero si no entienedes que paso puedes buscar este error)
- La penúltima línea nos indicará dende se encuentra el error (archivo y línea)
- La antepenúltima línea nos muestra “most recent call last” lo que significa que la llamada más reciente es la última (el programa se cerró después de esa llamada, se genero un error)

**Elevar una excepción**

- Cuando tenemos una excepción en python lo que sucede es que se crea un objeto de tipo exception que se va moviendo a través de los bloques de código hasta llegar al bloque principal si es que no se maneja dicha excepción en algún bloque intermedio el programa se interrumpe y genera el traceback

## Debugging

- O depuración es una herramienta que traen varios editores de código con el objetivo de solucionar nuestros errores de lógica. Revisemos la herramienta debugging de VSCode
- En este entorno podemos acceder a funcionalidades como:
    - pause → permite pausar la ejecución del programa
    - step over → permite avanazr un solo paso en el programa
    - step in → igresamos a un bloque secundario del programa (funciones)
    - step out → salimos del bloque secundario
    - restart → reinicia el programa
    - stop → detiene el programa
- Además podemos generar breakpoints, que son puntos en los que el programa se detendrá para ayudarnos a depurar el código

**Nota:**

- Existen herramientas de debugging propias de python como el módulo pdb o los breakpoints (a partir de python 3.7)

## Manejo de excepciones

Utilizando try y except puedes controlar errores. Por ejemplo cuando le pides a un usuario que ingrese un número entero pero este ingresa una letra, el código dará error pero con

```python
except TypeError:
	print('Ingresa un número válido') 
```

puedes tener control de estos problemas.

En el try se coloca código que esperamos que pueda lanzar algún error.

En el except se maneja el error, es decir, si ocurre un error dentro del bloque de código del try, se deja de ejecutar el código del try y se ejecuta lo que se haya definido en el Except.

El else se ejecuta sólo si no hubo ninguna excepción lanzada desde el try

finally: Se ejecuta SIEMPRE, haya sido lanzada la excepción o no haya sido lanzada.

![Untitled](Comprehensions,%20Lambdas%20y%20manejo%20de%20errores%2089ba962f5b6f464ba9d2c8127c59b0ca/Untitled%202.png)

Raise esta instrucción nos permite generar errores, es decir crear nuestros propios errores cuando detectemos que nuestro programa no actúa como debería con cierto tipo de datos

Su sintaxis es:

```python
raise <NombreError>("<descripci[on del error>")
```

Finally es una bloque de código que se ejecuta exista un error o no (un tercer bloque después de try except), no es muy usual pero puede darse para cerrar archivos, conexiones a BBDD o liberar recursos

![Untitled](Comprehensions,%20Lambdas%20y%20manejo%20de%20errores%2089ba962f5b6f464ba9d2c8127c59b0ca/Untitled%203.png)

```python
def divisors(num):
    divisors = []
    for i in range(1, num+1):
        if num % i ==0:
            divisors.append(i)
    return divisors

def run():
    try:
        num = int(input("Ingrese numero: "))
        print(divisors(num))
        print("Terminó mi programa")
    except ValueError:
        print("Please enter a number")
        
if __name__ == '__main__':
    run()
```

## Assert statements

![Untitled](Comprehensions,%20Lambdas%20y%20manejo%20de%20errores%2089ba962f5b6f464ba9d2c8127c59b0ca/Untitled%204.png)

- Es una manera poco usual de manejar los errores en python
- Evalúa una condicional, si esta se cumple continuamos con el flujo normal del python, si no se cumple eleva un error del tipo `AssertionError` y nos muestra un mensaje.
- Su sintaxis es:

```python
assert <condicion>, <"mensaje">
<código>
```

```python
def divisors(num):
    divisors = []
    for i in range(1, num+1):
        if num % i ==0:
            divisors.append(i)
    return divisors

def run():
    num = input("Ingrese numero: ")
    #Evalua si es un número
    assert num.isnumeric(), "Debes ingresar un número"
    print(divisors(int(num)))
    print("Terminó mi programa")
        
if __name__ == '__main__':
    run()
```

# ¿Cómo trabajar con archivos?

Archivos de texto y archivos binarios:

![Untitled](Comprehensions,%20Lambdas%20y%20manejo%20de%20errores%2089ba962f5b6f464ba9d2c8127c59b0ca/Untitled%205.png)

Solamente trabajaremos con archivos de texto dado que los binarios son complicados de trabajar. 

**Modos de Apertura**

- **r** -> Solo lectura
- **r+** -> Lectura y escritura
- **w** -> Solo escritura. Sobre escribe el archivo si existe. Crea el archivo si no existe
- **w+** -> Escritura y lectura. Sobre escribe el archivo si existe. Crea el archivo si no existe
- **a** -> Añadido (agregar contenido). Crea el archivo si éste no existe
- **a+** -> Añadido (agregar contenido) y lectura. Crea el archivo si éste no existe.

```python
with open("./ruta/del/archivo.txt", "r") as f:
```

## Manejo de archivos

```python
def read():
    numbers = []
    with open("./archivos/numbers.txt", "r", encoding='utf-8') as f:
        for line in f:
            numbers.append(int(line))
    print(numbers)

def write():
    names = ["Jeff", "Miguel", "John", "Facundo", "Chanchito"]
    names2 = ["Feliz", "Doe", "Adios"]
    #with open("./archivos/names.txt", "w", encoding='utf-8') as f:
    #    for name in names:
    #        f.write(name)
    #        f.write('\n')
    with open("./archivos/names.txt", "a", encoding='utf-8') as f:
        for name in names2:
            f.write(name)
            f.write('\n')
def run():
    #read()
    write()

if __name__ == '__main__':
    run()
```

#