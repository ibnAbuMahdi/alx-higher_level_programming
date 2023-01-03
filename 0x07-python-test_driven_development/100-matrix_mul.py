#!/usr/bin/python3
""" 100-matrix_mul """


def matrix_mul(ma, mb):
    """ multiplies two matrices """

    if type(ma) is not list:
        raise TypeError('m_a must be a list')
    if type(mb) is not list:
        raise TypeError('m_b must be a list')

    for row in ma:
        if type(row) is not list:
            raise TypeError('m_a must be a list of lists')
    for row in mb:
        if type(row) is not list:
            raise TypeError('m_b must be a list of lists')

    if len(ma) == 0 or len(ma[0]) == 0:
        raise ValueError("m_a can't be empty")
    if len(mb) == 0 or len(mb[0]) == 0:
        raise ValueError("m_b can't be empty")

    for row in ma:
        for i in row:
            if type(i) is not int and type(i) is not float:
                raise ValueError("m_a should contain only integers or floats")
    for row in mb:
        for i in row:
            if type(i) is not int and type(i) is not float:
                raise ValueError("m_b should contain only integers or floats")
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

    mul = [[sum([ra[i] * rb[i] for i in range(len(ra))])
            for rb in t_mb] for ra in ma]

    return mul
