#!/usr/bin/python3
"""
Function that multiplies two atrices using Numpy
"""
import numpy

def lazy_matrix_mul(m_a, m_b):
    """
    Function multiplies two matrices using Numpy
    """
    x = numpy.einsum("ik,kj->ij", m_a, m_b)
    return x
