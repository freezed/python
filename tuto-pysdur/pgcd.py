#!/usr/bin/env python3
# coding: utf8

"""
Author: freezed <2160318-free_zed@users.noreply.gitlab.com> 2021-04-13
Version: 0.1
Licence: `GNU GPL v3` GNU GPL v3: http://www.gnu.org/licenses/

This is a script following
https://gitlab.com/forga/process/fr/embarquement/-/issues/6

The goal is to build durable python script using standard library

:Tests:
>>> pgcd(561, 357)
51
"""


def pgcd(a,b):
    """
    This function find the Greatest Common Divisor (PGCD in French)
    between a & b

    :Tests:
    >>> pgcd(561, 357)
    51
    >>> pgcd(63, 42)
    21
    >>> pgcd(21, 15)
    3
    >>> pgcd(910, 42)
    14
    """
    rest = a - b
    check = b - rest

    while check != 0:
        a = max(b, rest)
        b = min(b, rest)
        rest = a - b
        check = max(b, rest) - min(b, rest)

    print(rest)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
