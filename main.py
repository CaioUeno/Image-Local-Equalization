import numpy as np
import matplotlib.pyplot as plt
from split_image import split_image
from equalization import equalize
from image_merge import image_merge

def rgb2gray(m: np.ndarray, r=0.299, g=0.578, b=0.144) -> np.ndarray:
    m_gray = r*m[:,:,0] + g*m[:,:,1] + b*m[:,:,2]
    return np.array(m_gray)

# Load the image
#file_name = input('Insira o nome da imagem com extenção: ')
file_name = 'foto.jpg' # REMOVER DEPOIS
img = plt.imread(file_name)

# Converts to grayscale if the image is RGB
if len(img.shape) == 3:
    img = rgb2gray(img)

img = img.astype(int)
# Ask the number of rows and columns and split the image
rows = int(input('Insira a quantidade de linhas que a imagem deve ser dividida: '))
cols = int(input('Insira a quantidade de colunas que a imagem deve ser dividida: '))
fragment_list = split_image(img, rows, cols)

# For each fragment, equalize it!
equal_list = [equalize(fragment, size=img.max()) for fragment in fragment_list]

# Join all fragments in a new image
new_img = image_merge(equal_list, img.shape, rows, cols)

plt.imshow(new_img, cmap="gray")
plt.savefig("foto2.png") # ALTERAR?
