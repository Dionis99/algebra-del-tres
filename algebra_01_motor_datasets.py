#!/usr/bin/env python3
"""
ALGEBRA DEL TRES - Parte 1: Motor algebraico y datasets
"""

import numpy as np
import random
import time
from typing import List, Tuple, Optional
from collections import Counter

P_VALS = [-1, 0, 1]

# Tablas lookup para operaciones ternarias
INTERACTION_TABLE = np.zeros((3, 3), dtype=np.int8)
COPRESENCE_TABLE = np.zeros((3, 3), dtype=np.int8)

for i, a in enumerate([-1, 0, 1]):
    for j, b in enumerate([-1, 0, 1]):
        INTERACTION_TABLE[i, j] = 0 if (a == 0 or b == 0) else a * b
        if a == b:
            COPRESENCE_TABLE[i, j] = a
        elif a == 0:
            COPRESENCE_TABLE[i, j] = b
        elif b == 0:
            COPRESENCE_TABLE[i, j] = a
        else:
            COPRESENCE_TABLE[i, j] = 0

IDX = {-1: 0, 0: 1, 1: 2}


def interaction(a: int, b: int) -> int:
    return int(INTERACTION_TABLE[IDX[a], IDX[b]])


def copresence(a: int, b: int) -> int:
    return int(COPRESENCE_TABLE[IDX[a], IDX[b]])


def up(x: int) -> int:
    return 1 if x == 0 else x


def down(x: int) -> int:
    return -1 if x == 0 else x


def apply_op(x: int, op: Optional[str]) -> int:
    if op == 'up':
        return up(x)
    if op == 'down':
        return down(x)
    return x


DATASET_SENTIMIENTO = [
    (-1, -1, 1), (-1, 0, -1), (-1, 1, 0),
    (0, -1, -1), (0, 0, 0), (0, 1, 1),
    (1, -1, 0), (1, 0, 1), (1, 1, 1),
]

DATASET_XOR = [
    (-1, -1, -1), (-1, 0, 1), (-1, 1, 1),
    (0, -1, 1), (0, 0, 0), (0, 1, -1),
    (1, -1, 1), (1, 0, -1), (1, 1, -1),
]

DATASET_MAYORIA = [
    (-1, -1, -1), (-1, 0, -1), (-1, 1, 0),
    (0, -1, -1), (0, 0, 0), (0, 1, 0),
    (1, -1, 0), (1, 0, 0), (1, 1, 1),
]
