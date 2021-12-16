#!/usr/bin/python3
"""
Function that multiplies two matrices
"""

def matrix_mul(m_a, m_b):
    """
    Function that multiplies two matrices and must be a list
    """
    if type(m_a) not in [list]:
        raise TypeError("m_a must be a list")
    if type(m_b) not in [list]:
        raise TypeError("m_b must be a list")
    for x in m_a:
        if not x or not isinstance(x,list):
            raise TypeError("m_a must be a list of lists")
    for y in m_a:
        if not y or not isinstance(y,list):
            raise("m_b must be a list of lists")
    if len(m_a) == 0 or (len(m_a) == 1 and len(m_a[0])==0):
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0 or (len(m_b) == 1 and len(m_b[0])==0) :
        raise ValueError("m_b can't be empty")
    for i in m_a:
        for g in i:
            if type(g) not in [int,float]:
                raise TypeError("m_a should contain only integers or floats")
    for j in m_b:
        for h in j:
            if type(h) not in [int,float]:
                raise TypeError("m_b should contain only integers or floats")
    result = [[sum(a * b for a, b in zip(m_a_row, m_b_col))
               for m_b_col in zip(*m_b)]
             for m_a_row in m_a]
    return result
