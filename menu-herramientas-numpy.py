import numpy as np

# incorporamos el parámetro para mostrar el nombre del menú


def mostrar_menu(nombre, opciones):
    print(f'# {nombre}. Seleccione una opción:')
    for clave in sorted(opciones):
        print(f' {clave}) {opciones[clave][0]}')


def leer_opcion(opciones):
    while (a := input('Opción: ')) not in opciones:
        print('Opción incorrecta, vuelva a intentarlo.')
    return a


def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1]()


# incorporamos el parámetro para mostrar el nombre del menú
def generar_menu(nombre, opciones, opcion_salida):
    opcion = None
    while opcion != opcion_salida:
        mostrar_menu(nombre, opciones)
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion, opciones)
        print()


def menu_principal():
    opciones = {
        '1': ('Transformar Array de 2Dimensiones a 1Dimension', funcion1),
        # la acción es una llamada a submenu que genera un nuevo menú
        '2': ('Funcion nºs Aleatorios: np.random', submenu),
        '3': ('Opción 3', funcion3),
        '4': ('Salir', salir)
    }

    # indicamos el nombre del menú
    generar_menu('Menú principal', opciones, '4')


def submenu():
    opciones = {
        'a': ('Opción nº aleatorio', funcionA),
        'b': ('Opción np.where', funcionB),
        'd': ('Opción estadistica, distribuciones', funcionD),
        'c': ('Volver al menú principal', salir)
    }

    generar_menu('Submenú', opciones, 'c')  # indicamos el nombre del submenú


# A partir de aquí creamos las funciones que ejecutan las acciones de los menús
def funcion1():
    # Creamos el primer array con np.arange, que nos permite 'saltarnos' los números pares y quedarnos
    # sólo con los impares:

    array_1 = np.arange(1, 100, 2)

# Vemos cuántos valores tiene el array_1:

    len(array_1)

# Creamos un array de 50 elementos con el número 1:

    array_2 = np.ones(50)

# Multiplicamos cada valor por 3:

    array_2 = array_2 * 3

# Creamos el array de 2 dimensiones con los que tenemos:

    array_2d = np.array([array_1, array_2])
    print(array_2d)
    print('////////////////////')
    print(array_2d.shape)
    print('////////////////////')

    # Esta función nos permite cambiar la forma de un array a nuestra conveniencia, indicando cómo queremos cambiar dimensiones y valores por dimensión. **Importante**: Para funcionar requiere que el nuevo array tenga el mismo número de valores!
    # > np.reshape(_array_, (_dimensiones_, *n_valores*))
    f = np.reshape(array_2d, (10, 10))
    print('////////////////////')
    print(f)
    print('////////////////////')
    print(array_2d.size)
    print('////////////////////')
    print('////////////////////')
    # arrLa **T** (nota que es mayúscula) se refiere a *transposición*. Lo que hace este atributo es mostrar la versión invertida del número de valores por el número de dimensiones y viceversa. Se explica mejor con un ejemplo:ay.T
    a = np.array([[1, 2, 3, 4, 5], [10, 20, 30, 40, 50]])
    print(a.shape)
    print('////////////////////')
    print('Tiene 5dimensiones por 2valores')
    # Array original
    # array([[1,  2,  3,  4,  5],
    #    [10, 20, 30, 40, 50]])
    print(a.T)
    # Resultado
    # Tiene 5dimensiones por 2valores
    # [[1 10]
    #  [2 20]
    #  [3 30]
    #  [4 40]
    #  [5 50]]


def funcion2():
    print('Has elegido la opción 2')


def funcion3():
    print('Has elegido la opción 3')


def funcionA():
    print('Has elegido la opción A')
    print('////////////////////')
    print('Esta función tiene un uso muy específico. Crea un número entero aleatorio entre el rango de números que le indiquemos (**rand**om **int**eger)')
    print(np.random.randint(0, 1000))


def funcionB():
    print('Has elegido la opción B')
    print('////////////////////')
    print('np.where')
    print('> np.where(*condicion*, *accion_si_se_cumple*, *accion_si_no_se_cumple*)')
    print('///////////////////////////////////')
    print('///////////////////////////////////')

    array_1 = np.arange(1, 100, 2)
    array_2 = np.ones(50)
    print('Array 1')
    print(array_1)
    print('///////////////////////////////////')
    print('///////////////////////////////////')
    print('Array 2')
    print(array_2)
    print('///////////////////////////////////')
    print('///////////////////////////////////')
    print('Creamos Array de 2Dimensiones')
    array_2d = np.array([array_1, array_2])
    print(array_2d)
    print('///////////////////////////////////')
    print('np.where')
    print('Esta función sirve para encontrar valores basándonos en una condición y ejecuta dos acciones: una para los valores donde se cumple la condición y otra para los valores donde **no** se cumple:')
    print('///////////////////////////////////')
    print('Multiplica cada elemento que has encontrado por 10 y si no se cumple la 1º condicion al array cada elemento le restamos 5')
    print('np.where(array_2d > 50, 0, array_2d - 5)')
    print('\n')
    print('///////////////////////////////////')
    print('Los que son iguales a 1 haz esta operacion pero los que no los dejamos igual')
    print('np.where(array_2d > 50, 0, array_2d)')

    # Multiplica el elemento que has encontrado por 10 y si no
    # se cumple la 1º condicion el array o el elemento que has encontrado  menos 5
    print(np.where(array_2d > 50, 0, array_2d - 5))


def funcionD():

    print('Tenemos 1000 personas y la media es de 1.75,la desviacion standar esde 5cm que son 0.05 y de 1000 personas calcule la media')
    print('array_normal = np.random.normal(1.75, 0.05, 1000)')

    array_normal = np.random.normal(1.75, 0.05, 1000)
    print(array_normal)

    print('\n')
    print('Con np.mean Una vez tenemos estos valores, podemos encontrar `la media` de ellos con esta función:')
    print(np.mean(array_normal))

    print('\n')
    print('Con np.median :Para encontrar `la mediana`, prácticamente lo mismo:')
    print(np.median(array_normal))
    # Resultado = 1.749146954949008

    print('\n')
    print('Lo mismo ocurre con la `desviación estándar`, se usarán las siglas _std_ de **St**andard **D**eviation:> np.std(_array_) ')
    print(np.std(array_normal))
    # Resultado = 0.05104637725574751


def salir():
    print('Saliendo')


if __name__ == '__main__':
    menu_principal()  # iniciamos el programa mostrando el menú principal
