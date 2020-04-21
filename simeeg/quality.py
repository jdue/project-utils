"""Simplex quality metrics """

from itertools import combinations
import numpy as np

def tetrahedron_volume(tetra):
    tetra_det = np.c_[np.broadcast_to(1, (tetra.shape[0],tetra.shape[1],1)), tetra]
    V = np.array([np.linalg.det(i) for i in tetra_det]) / 6
    return V

def gamma(tetra, normalize=True):
    V = tetrahedron_volume(tetra)
    edge_combinations = list(combinations(np.arange(4), 2))
    edges = tetra[:, edge_combinations]
    # edge length
    S = np.linalg.norm(edges[:,:,1]-edges[:,:,0], axis=2)
    Srms = np.sqrt(np.sum(S**2, 1) / 6)
    gamma = Srms**3 / V
    if normalize:
        # value for equilateral tetrahedron
        gamma /= 8.479670
    return gamma