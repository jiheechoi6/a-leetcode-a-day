class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        if len(box) == 0:
            return box
        
        num_rows = len(box)
        num_col = len(box[0])
        
        result = []
        for i in range(num_col):
            result.append([])
            for j in range(num_rows):
                result[i].append(".")
                
        for i in range(num_rows):
            next_col = num_rows-i-1
            next_row = num_col-1
            for j in range(next_row, -1, -1):
                if box[i][j] == "#":
                    result[next_row][next_col] = '#'
                    next_row -= 1
                if box[i][j] == "*":
                    result[j][next_col] = "*"
                    next_row = j-1
        
        return result
