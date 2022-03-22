from gettext import find


def get_fractions(valor):
    if("/" in valor):
      d = valor.find("/")
      l = len(valor)
      decimal = int (valor[0:d]) / int (valor[d+1:l])
      return decimal
    else:
      return float(valor)

def suma(a ,b):
    sumando_a = float(a)
    sumando_b = float(b)
    return sumando_a + sumando_b