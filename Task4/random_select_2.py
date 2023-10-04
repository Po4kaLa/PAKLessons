import numpy as np
import sys

def random_select(file1, file2, p):
    data1 = np.loadtxt(file1)
    data2 = np.loadtxt(file2)
    
    mask = np.random.rand(len(data1)) < p
    print(mask)
    result = np.where(mask, data1, data2)
    
    print(result)

if __name__ == "__main__":
    file1 = sys.argv[1]
    file2 = sys.argv[2]
    p = float(sys.argv[3])
    
    random_select(file1, file2, p)