#!/usr/bin/env python3
"""Clusterin tasks"""
import numpy as np


def maximization(X, g):
    """Maximization function"""
    if type(X) is not np.ndarray or type(g) is not np.ndarray:
        return (None, None, None)
    if len(X.shape) != 2 or len(g.shape) != 2:
        return (None, None, None)
    if X.shape[0] != g.shape[1]:
        return (None, None, None)
    if not np.isclose(np.sum(g, axis=0), 1).all():
        return (None, None, None)
    n, d = X.shape
    k, _ = g.shape
    pi = g.sum(axis=1) / n
    m = np.dot(g, X) / g.sum(1)[:, None]
    S = np.zeros([k, d, d])
    for i in range(k):
        ys = X - m[i, :]
        S[i] = (g[i, :, None, None] *
                np.matmul(ys[:, :, None], ys[:, None, :])).sum(axis=0)
    S = S / g.sum(axis=1)[:, None, None]
    return (pi, m, S)
