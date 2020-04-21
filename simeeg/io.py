""" I/O utilities for VTK multiblock format """

import numpy as np
import os.path as op
import pyvista as pv

def read_sourcespaces(path):
    return {k:pv.read(op.join(path, 'sph{}-src.vtm'.format(k))) for k in [1, 3]}

def get_points_from_multiblock(mb):
    return np.vstack([b.points for b in mb])

def split_data_in_blocks(mb, data, ax):
    idx = np.cumsum([b.n_points for b in mb])
    # two split indices results in three splits
    return np.split(data, idx[:-1], axis=ax)

def write_data_to_multiblock(mb, data, name):
    for b,d in zip(mb, data):
        b[name] = d
