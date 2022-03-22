from gettext import find


def get_fractions(valor):
    """

    Parameters
    ----------
    valor :Es el string que sera transformado a flotante.
        

    Returns
    ----------
    Regresa el valor en su forma decimal flotante.

    """
    if("/" in valor):
        d = valor.find("/")
        lenght = len(valor)
        decimal = int(valor[0:d]) / int(valor[d+1:lenght])
        return decimal
    else:
        return float(valor)


def suma(a, b):
    """

    Parameters
    ----------
    a : int, float, string.
    Primer valor definido para la operación.
        
    b : int, float, string.
    Segundo valor definifo para la operación.
        

    Returns
    -------
    float
    Valor obtenido por la suma de los parámetros.

    """
    sumando_a = float(a)
    sumando_b = float(b)
    return sumando_a + sumando_b


def multiplicacion(a, b):
    """

    Parameters
    ----------
    a :int, float, string.
    Primer valor definido para la operación.
        
    b : int, float, string.
    Segundo valor definido para la operación.
        

    Returns
    -------
    Valor obtenido por la multiplicación de los parámetros.

    """
    multiplicando = float(a)
    multiplicador = float(b)
    return multiplicando * multiplicador
