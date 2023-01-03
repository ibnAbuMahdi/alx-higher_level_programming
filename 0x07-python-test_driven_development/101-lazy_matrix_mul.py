#!/usr/bin/python3
""" 101-lazy_matrix_mul """
import numpy as np


def lazy_matrix_mul(ma, mb):
    """ multiplies two matrices using numpy """

    if type(ma) is not list and type(ma) is not np.ndarray:
        raise TypeError('m_a must be a list or numpy.ndarray')
    if type(mb) is not list and type(mb) is not np.ndarray:
        raise TypeError('m_b must be a list or numpy.ndarray')

    for row in ma:
        if type(row) is not list and type(row) is not np.ndarray:
            raise TypeError('m_a must be a list of lists or \
numpy array of arrays')
    for row in mb:
        if type(row) is not list and type(row) is not np.ndarray:
            raise TypeError('m_b must be a list of lists or \
numpy array of arrays')

    if len(ma) == 0 or len(ma[0]) == 0:
        raise ValueError("m_a can't be empty")
    if len(mb) == 0 or len(mb[0]) == 0:
        raise ValueError("m_b can't be empty")

    for row in ma:
        for i in row:
            if type(i) is not int and type(i) is not float \
                    and type(i) is not np.int64 and type(i) is not np.float64:
                raise ValueError("m_a should contain only integers,\
 floats, numpy.int64 or numpy.float64")
    for row in mb:
        for i in row:
            if type(i) is not int and type(i) is not float \
                    and type(i) is not np.int64 and type(i) is not np.float64:
                raise ValueError("m_b should contain only integers,\
 floats, numpy.int64 or numpy.float64")
    s_ma = len(ma[0])
    for row in ma:
        if s_ma != len(row):
            raise TypeError('each row of m_a must be of the same size')
    s_mb = len(mb[0])
    for row in mb:
        if s_mb != len(row):
            raise TypeError('each row of m_b must be of the same size')

    t_mb = [[row[i] for row in mb] for i in range(len(mb[0]))]
    if len(ma[0]) != len(t_mb[0]):
        raise ValueError("m_a and m_b can't be multiplied")

    return np.matmul(ma, mb)
