import numpy as np
import matplotlib.pyplot as plt

def equalize(m: np.ndarray) -> np.ndarray:
    bins = range(0, 257)
    hist, _ = np.histogram(m, bins)

    mn = sum(hist)
    c = 255./mn
    out_intensity = np.zeros(256)
    for k in range(256):
        soma = sum(hist[:k+1])
        out_intensity[k] = c*soma
    
    img_eq = np.zeros(m.shape)
    num_rows, num_cols = m.shape
    for row in range(num_rows):
        for col in range(num_cols):
            img_eq[row, col] = out_intensity[m[row, col]]
    
    return img_eq

img = plt.imread("foto.jpg")
print(img.shape)
img2 = equalize(img[0:200, 0:200])
plt.imshow(img2, cmap="gray")
plt.savefig("foto2.jpg")

