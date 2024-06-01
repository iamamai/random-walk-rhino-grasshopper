import math
import random

from ghpythonlib import treehelpers


class Grid:
    def __init__(self, rows, columns):
        self.__rows = rows
        self.__columns = columns
    
    @property
    def rows(self):
        return self.__rows
    
    @property
    def columns(self):
        return self.__columns
    
    @property
    def size(self):
        return self.__rows * self.__columns
        
        
    def get_index(self, x, y):
        return x + y * self.__columns
    
    def get_row(self, i):
        return int(i / self.__columns)
    
    def get_column(self, i):
        return int(math.floor(i % self.__columns))
    
    def get_adjacent(self, i):
        x = self.get_column(i)
        y = self.get_row(i)
        
        adjacent = [] 
        if y - 1 >= 0:  # northern neighbour
            adjacent.append(self.get_index(x, y-1))
        if x + 1 < self.__columns:  # eastern neighbour
            adjacent.append(self.get_index(x+1, y))
        if y + 1 < self.__rows:  # southern neighbour
            adjacent.append(self.get_index(x, y+1))
        if x - 1 >= 0:  # western neighbour
            adjacent.append(self.get_index(x-1, y))
        
        return adjacent
        

if __name__ == "__main__":
    if S is not None:
        random.seed(S)
    
    g = Grid(Ex, Ey)
    
    visited = {i: False for i in range(g.size)}
    
    paths = []
    pi = 0  # current path index
    ppi = -1  # previous path index
    
    while not all(visited.values()):
        if pi > ppi:  # start new path
            paths.append([])
            
            available = [k for k, v in visited.iteritems() if not v]
            if len(available) < 1:
                break
            
            ci = random.choice(available)  # current index
            paths[pi].append(ci)
            visited[ci] = True
            
            ppi = pi
            
        else:  # continue with current path
            if len(paths[pi]) == L:
                pi += 1
                continue
            
            ci = paths[pi][-1]
            
            candidates = [i for i in g.get_adjacent(ci) if not visited[i]]
            if len(candidates) < 1:
                print "Cell {} is a dead end".format(ci)
                pi += 1
                continue
            
            ni = random.choice(candidates)  # next index
            paths[pi].append(ni)
            visited[ni] = True
        

    # Outputs
    I = treehelpers.list_to_tree(paths)
    
    
    