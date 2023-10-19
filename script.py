import cellsim
import time
import os

# Instantiate a Tissue object (2D array), which can be populated by cells.
tissue = cellsim.Tissue(30,40)

'''Populates the tissue using a text file. This method overwrites the attributes
previously given to the tissue object using parameters extracted from the file
and the cell type defined in the argument.'''

tissue.seed_from_file('test_tissue_03.txt', cellsim.Cell) 
print('time step:', 0) 
print(tissue) 
for i in range(1,100): 
    os.system('cls')  #will be os.system('cls') 
    print('time step:', i)     
    tissue.next_state() 
    print(tissue) 
    time.sleep(0.05)

'''Populates the tissue using a single argument, which is a 2D array of type list.
Each element of the array should be of a cell type (Cell, Cancer...) '''

test_matrix = list()
for i in range(10):
    test_matrix.append([])
    for j in range(40):
        test_matrix[i].append(cellsim.Cell(False))
test_matrix[5][5] = cellsim.Cell(True)
test_matrix[5][6] = cellsim.Cell(True)
test_matrix[5][7] = cellsim.Cell(True)
tissue.seed_from_matrix(test_matrix)

print('time step:', 0) 
print(tissue) 
for i in range(1,100): 
    os.system('cls') 
    print('time step:', i)     
    tissue.next_state() 
    print(tissue) 
    time.sleep(0.05)

''' Create a randomly distributed array of cells which have an
approximate confluency'''

tissue.seed_random(0.5,cellsim.Cell)
print('time step:', 0) 
print(tissue) 
for i in range(1,100): 
    os.system('cls') 
    print('time step:', i)     
    tissue.next_state() 
    print(tissue) 
    time.sleep(0.05)
