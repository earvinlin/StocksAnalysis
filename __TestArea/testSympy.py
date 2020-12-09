# import sympy  
from sympy import * 
  
#M = Matrix([[1, 0, 1, 3], [2, 3, 4, 7], [-1, -3, -3, -4]]) 
#M = Matrix([[0,0,0,1,2],[1,1,1,1,3],[8,4,2,1,4],[27,9,3,1,4]])
M = Matrix([[0,0,0,1,-2],[1,1,1,1,1],[8,4,2,1,1],[27,9,3,1,2]])

print("Matrix : {} ".format(M)) 
#print("Matrix : {} ".format(M1)) 
#print("Matrix : {} ".format(M2)) 
   
# Use sympy.rref() method  
M_rref = M.rref()   
      
print("The Row echelon form of matrix M and the pivot columns : {}".format(M_rref)) 