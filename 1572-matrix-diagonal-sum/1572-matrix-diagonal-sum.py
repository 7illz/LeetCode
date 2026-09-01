class Solution(object):

  def diagonalSum(self, mat):
    
    sum = 0
    for i in range(len(mat)):

        sum += mat[i][i]

    j=len(mat[i])-1

    for i in range(len(mat)):
        if i==j:
            j-=1
            continue
        sum+=mat[i][j]
        j-=1

    return sum