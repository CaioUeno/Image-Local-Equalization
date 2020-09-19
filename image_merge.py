import numpy as np
import matplotlib.pyplot as plt
def image_merge(equal_list,shape,rows,cols):
    aux = []

    #Merge images in each row
    for i in range(0,rows):
        aux.append(np.hstack((equal_list[j] for j in range(i*cols,((i*cols)+cols)))))
    
    #Merge all rows
    new_img = np.vstack(((aux[i] for i in range(0,rows))))
    
    return new_img
