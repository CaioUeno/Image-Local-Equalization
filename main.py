import numpy as np
import matplotlib.pyplot as plt
from split_image import split_image
from equalization import equalize
from image_merge import image_merge

# Load the image
file_name = input('Insira o nome da imagem com extensão: ')
img = plt.imread(file_name)

# Ask the number of rows and columns and split the image
rows = int(input('Insira a quantidade de linhas que a imagem deve ser dividida: '))
cols = int(input('Insira a quantidade de colunas que a imagem deve ser dividida: '))
fragment_list = split_image(img, rows, cols)

# For each fragment, equalize it!
equal_list = [equalize(fragment) for fragment in fragment_list]

# Join all fragments in a new image
new_img = image_merge(equal_list, img.shape, rows, cols)

# Show and save
new_file_name = input('Insira o nome da imagem alterada com extensão: ')
plt.imshow(new_img, cmap='gray')
plt.savefig(new_file_name) 
