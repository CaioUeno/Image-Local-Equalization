import numpy as np
import matplotlib.pyplot as plt

def equalize(m: np.ndarray, size=256) -> np.ndarray:
    caixas = range(0, size+1)
    hist, _ = np.histogram(m, caixas)

    sum_hist = sum(hist)
    const = (size-1)/sum_hist
    saida = np.zeros(size+1)
    for i in range(size+1):
        soma = sum(hist[:i+1])
        saida[i] = soma*const
    
    m_eq = np.zeros(m.shape)
    n_lin, n_col = m.shape
    
    for i in range(n_lin):
        for j in range(n_col):
            m_eq[i, j] = saida[int(m[i, j])]
    
    return m_eq
