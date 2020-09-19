import numpy as np
import matplotlib.pyplot as plt
from split_image import split_image
from equalization import equalize
from image_merge import image_merge

# Load the image
#file_name = input('Insira o nome da imagem com extenção: ')
file_name = 'foto.jpg' # REMOVER DEPOIS
img = plt.imread(file_name)

# Ask the number of rows and columns and split the image
rows = int(input('Insira a quantidade de linhas que a imagem deve ser dividida: '))
cols = int(input('Insira a quantidade de colunas que a imagem deve ser dividida: '))
fragment_list = split_image(img, rows, cols)

# For each fragment, equalize it!3
equal_list = []
for fragment in fragment_list:
    equal_list.append(equalize(fragment))

# Join all fragments in a new image3
new_img = image_merge(equal_list,img.shape,rows,cols)

plt.imshow(new_img, cmap="gray")
plt.savefig("foto2.jpg") # ALTERAR?
