import numpy as np
import matplotlib.pyplot as plt
from split_image import split_image
from equalization import equalize
#from arquivo_do_Vinicius import funcao_do_Vinicius

# Load the image
#file_name = input('Insira o nome da imagem com extenção: ')
file_name = 'foto.jpg' # REMOVER DEPOIS
img = plt.imread(file_name)
print(img.shape)

# Ask the number of rows and columns and split the image
rows = int(input('Insira a quantidade de linhas que a imagem deve ser dividida: '))
cols = int(input('Insira a quantidade de colunas que a imagem deve ser dividida: '))
fragment_list = split_image(img, rows, cols)

# For each fragment, equalize it!
equal_list = []
for fragment in fragment_list:
    equal_list.append(equalize(fragment))

# Join all fragments in a new image
#new_img = funcao_do_Vinicius(equal_list)

plt.imshow(new_img, cmap="gray")
plt.savefig("foto2.jpg") # ALTERAR?
