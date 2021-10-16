class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        idx = [0, 0]
        dirc = (-1, 1)  # when going down, (1, -1)
        m = len(mat)
        n = len(mat[0])
        result = []
        tst = [1, 2, 3]

        for i in range(len(mat)* len(mat[0])):
            result.append(mat[idx[0]][idx[1]])
            
            y = idx[0]
            x = idx[1]
            if dirc[0]>0 and (x==0 or y==m-1):  # going down
                if y == m-1:
                    idx[1] += 1
                elif x == 0:
                    idx[0] += 1
                dirc = (-dirc[0], -dirc[1])
            elif dirc[0]<0 and (y==0 or x==n-1):  # going up
                if x == len(mat[0])-1:
                    idx[0] +=1
                elif y == 0:
                    idx[1] +=1
                dirc = (-dirc[0], -dirc[1])
            else:
                idx[0] += dirc[0]
                idx[1] += dirc[1]
                    
        return result
                
