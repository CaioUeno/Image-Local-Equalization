import numpy as np
import matplotlib.pyplot as plt

def equalize(m: np.ndarray) -> np.ndarray:
    caixas = range(0, 257)
    hist, _ = np.histogram(m, caixas)

    sum_hist = sum(hist)
    const = 255/sum_hist
    saida = np.zeros(256)
    for i in range(256):
        soma = sum(hist[:i+1])
        saida[i] = soma*const
    
    m_eq = np.zeros(m.shape)
    n_lin, n_col = m.shape
    for i in range(n_lin):
        for j in range(n_col):
            m_eq[i, j] = saida[m[i, j]]
    
    return m_eq
