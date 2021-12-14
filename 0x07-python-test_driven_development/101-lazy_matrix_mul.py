#!/usr/bin/python3
"""
Function that multiplies two atrices using Numpy
"""
import numpy as np

def lazy_matrix_mul(m_a,m_b):
    """
    Function multiplies two matrices using Numpy
    """
    m = np.dot(m_a,m_b)
    print(m)
