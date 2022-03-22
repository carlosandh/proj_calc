from gettext import find


def get_fractions(valor):
    if("/" in valor):
      d = valor.find("/")
      l = len(valor)
      decimal = int (valor[0:d]) / int (valor[d+1:l])
      return decimal
    else:
      return float(valor)

def multiplicacion(a,b):
    multiplicando = float(a)
    multiplicador = float(b)
    return multiplicando * multiplicador