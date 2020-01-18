import math
from collections import Iterable


def h(p, base=2):
    return - p * math.log(p, base=base)


def entropy(p, base=2):
    """

    :param p:
    :param base:
    :return:
    """
    ret = 0.0
    if isinstance(p, Iterable):
        for item in p:
            ret += h(item, base)
    else:
        ret = h(p, base)
    return ret


# def joint_entropy(X, Y, base=2):
#     if len(X) == len(Y) and isinstance(X, Iterable) and isinstance(Y, Iterable):
#         ret = 0.0
#         for x in X:
#             for y in Y:
#             ret += h(item, base)
#     else:
#         ret = h(p, base)
#     return ret


def conditional_entropy(given, base):
    pass


def relative_entropy(P, Q, base=2):
    """

    :param P:
    :param Q:
    :param base:
    :return:
    """
    ret = 0.0
    if len(P) == len(Q) and isinstance(P, Iterable) and isinstance(Q, Iterable):
        for p in P:
            for q in Q:
                ret += (-p * math.log(p / q, base=base))
    elif Q != 0:
        ret = - P * math.log(P / Q, base=base)
    return ret


def cross_entropy(P, Q, base=2):
    """

    :param P:
    :param Q:
    :param base:
    :return:
    """
    ret = 0.0
    if len(P) == len(Q) and isinstance(P, Iterable) and isinstance(Q, Iterable):
        for p in P:
            for q in Q:
                ret += (-p * math.log(q, base=base))
    else:
        ret = - P * math.log(Q, base=base)
    return ret


def perplexity():
    """

    :return:
    """
    pass


def mutual_information(x, y):
    """
    
    :param x:
    :param y:
    :return:
    """
    pass
