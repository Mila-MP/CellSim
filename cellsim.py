import copy
import random


class Cell:
    ''' Represents a cell defined by 'O' when alive and '.' when dead.
        Attribute:
        alive: True representing alive and False representing dead.
    '''
   
    def __init__(self, alive=False):
        self.alive = alive

    def __str__(self):
        if self.alive:
            return 'O'
        return '.'

    def is_alive(self):
        return self.alive

    def update_cell(self, array):
        ''' Determines the next state(alive of dead) of the cell instance
            depending on the current state of it's 8 neighbours.
        '''
        alive_neighbours = 0
        for i in range(3):
            for j in range(3):
                # Skips the centre element of the 3x3 array
                if i == 1 and j == 1:
                    continue
                # Counts the number of neighbours that are alive
                if array[i][j].is_alive():
                    alive_neighbours += 1

        if self.alive:
            # Checks if overpopulation or loneliness criterias are met
            if alive_neighbours >= 4 or alive_neighbours <= 1:
                self.alive = False
        else:
            # Checks if birth criteria is met
            if alive_neighbours == 3:
                self.alive = True
                
        return self.alive


class Cancer(Cell):
    ''' Represents a cancer cell defined by 'X' when alive and '.' when dead.
        Attribute:
        alive: True representing alive and False representing dead.
    '''
    def __str__(self):
        if self.alive:
            return 'X'
        return '.'

    def update_cell(self, array):
        ''' Determines the next state (alive of dead) of the cell instance
            depending on the current state of it's 8 neighbours.
        '''
        alive_neighbours = 0
        for i in range(3):
            for j in range(3):
                if i == 1 and j == 1:
                    continue
                if array[i][j].is_alive():
                    alive_neighbours += 1
                    
        if self.alive:
            if alive_neighbours >= 5 or alive_neighbours <= 1:
                self.alive = False
        else:
            if alive_neighbours == 3:
                self.alive = True
                
        return self.alive


class Tissue:
    ''' Represents a tissue (2d array) populated by cells.
        Class Tissue has 4 attributes.
        rows: number of rows in the tissue (default to 1)
        cols: number of columns in the tissue (default to 1)
        CellType: defines the type of cell populating the tissue (default to Cell)
        matrix: 2D array of type list where each element should be of type CellType
    '''
    def __init__(self, rows=1, cols=1, CellType=Cell):
        self.rows = rows
        self.cols = cols
        self.CellType = CellType
        self.matrix = [[CellType() for i in range(cols)]for j in range(rows)]

    def __str__(self):
        matrix = [''.join([str(cell) for cell in row])for row in self.matrix]
        return '\n'.join(matrix)

    def __getitem__(self, coordinate):
        return self.matrix[coordinate]

    def __setitem__(self, coordinate, value):
        self.matrix[coordinate] = value

    def seed_from_matrix(self, array):
        ''' Overwrites the four attribute variables of the Tissue instance using
            a single argument (2D array of type list, where each element should
            be of a cell type).
        '''     
        rows = len(array)
        cols = len(array[0])
        self.matrix = [[array[j][i] for i in range(cols)]for j in range(rows)]
        return self.matrix

    def seed_from_file(self, filename, cell_type=Cell):
        '''Overwrites the 4 attribute variables using parameters extracted from
           a file (filename argument) and the cell type (cell_type argument).
        '''
        self.matrix = list()
        with open(filename) as file:
            lines = file.readlines()
            
        for i, row in enumerate(lines):
            self.matrix.append([])
            for cell in row.strip():
                if cell == '.':
                    self.matrix[i].append(cell_type())
                else:
                    self.matrix[i].append(cell_type(True))
        return self.matrix

    def seed_random(self, p, cell_type=Cell):
        ''' Creates a randomly distributed array of cells of a specified type
            (cell_type argument) which have an approximate confluency
            (confluency argument).
        '''
        array = list()
        for i, row in enumerate(self.matrix):
            array.append([])
            for cell in row:
                if random.choices(['O', '.'], weights=(p, 1-p)) == ['O']:
                    array[i].append(cell_type(True))
                else:
                    array[i].append(cell_type())
                    
        self.matrix = array
        return self.matrix

    def next_state(self):
        ''' Creates an updated version of a Tissue instance based on the
            state on the cells populating the tissue
        '''
        rows = len(self.matrix)
        cols = len(self.matrix[0])
        # Creates a Tissue instance but with additional borders of dead cell
        expanded_tissue = Tissue(rows + 2, cols + 2, self.CellType)
        for i, row in enumerate(expanded_tissue):
            for j, cell in enumerate(row):
                if (i == 0 or i == expanded_tissue.rows-1 or
                    j == 0 or j == expanded_tissue.cols-1):
                    continue
                else:
                    expanded_tissue[i][j] = self.matrix[i-1][j-1]
        expanded_tissue2 = copy.deepcopy(expanded_tissue)

        # For each cell, creates an array representing its
        # 8 surrounding cells to then update the state of the cell.
        array = [['' for a in range(3)]for b in range(3)]
        for i, row in enumerate(expanded_tissue):
            for j, cell in enumerate(row):
                if (i == 0 or i == expanded_tissue.rows-1 or
                    j == 0 or j == expanded_tissue.cols-1):
                    continue
                else:
                    array[0][0] = expanded_tissue2[i-1][j-1]
                    array[0][1] = expanded_tissue2[i-1][j]
                    array[0][2] = expanded_tissue2[i-1][j+1]
                    array[1][0] = expanded_tissue2[i][j-1]
                    array[1][1] = expanded_tissue2[i][j]
                    array[1][2] = expanded_tissue2[i][j+1]
                    array[2][0] = expanded_tissue2[i+1][j-1]
                    array[2][1] = expanded_tissue2[i+1][j]
                    array[2][2] = expanded_tissue2[i+1][j+1]
                    cell.update_cell(array)