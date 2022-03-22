import sys
sys.path.append('/src')
sys.path.append('./')

import src.calc as fc
import pytest

#Funciones calculadora

def test_fractions():
    assert fc.get_fractions("3/4")==.75


def test_suma():
    assert fc.suma("3",4)==7


def test_multiplicacion():
    assert fc.multiplicacion(7.3, 2)==14.6