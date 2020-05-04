from collections import defaultdict
class Solver:
    @staticmethod
    def isValid(rows, cols, boxs):
        for i in range(9):
            for j in range(1,10):
                val = str(j)
                
                if rows[i][val] > 1:
                    return False
                if cols[i][val] > 1:
                    return False
                if boxs[i][val] > 1:
                    return False
                
        return True

    @staticmethod
    def prune(rows, cols, boxs, cur, val):
        i,j = cur
        if rows[i][val] != 0:
            return False
        
        if cols[j][val] != 0:
            return False
        
        if boxs[3*(i//3)+(j//3)][val] != 0:
            return False
        return True

    @staticmethod
    def nextPt(cur):
        i, j = cur
        if i == 8 and j == 8:
            return (-1,-1)
        elif j == 8:
            return (i+1, 0)
        else:
            return (i, j+1)


    def helper(self, arr,rows, cols, boxs, cur, count,ans):
        if  ans: return
        valid = self.isValid(rows, cols, boxs)
        if not valid:
            return
        
        if count == 0:
            
            for row in arr:
                ans.extend(row)
            return
        if cur == (-1,-1):
            return
        i,j = cur
        nextcur = self.nextPt(cur)
        if arr[i][j] == '.':
            for val in range(1,10):
                sVal = str(val)
                if self.prune(rows, cols, boxs,cur, sVal):
                    rows[i][sVal] += 1
                    cols[j][sVal] += 1
                    boxs[3*(i//3)+(j//3)][sVal] += 1
                    arr[i][j] = sVal
                    self.helper(arr, rows, cols, boxs, nextcur, count-1, ans)
                    arr[i][j] = "."
                    boxs[3*(i//3)+(j//3)][sVal] -= 1
                    cols[j][sVal] -= 1
                    rows[i][sVal] -= 1
                    
        else:
            self.helper(arr, rows, cols, boxs, nextcur, count, ans)
        
        return

    
    def solver(self,arr):
        ans = []
        rows = [defaultdict(int) for _ in range(9)]
        cols = [defaultdict(int) for _ in range(9)]
        boxs = [defaultdict(int) for _ in range(9)]
        count = 0
        for i in range(9):
            for j in range(9):
                val = arr[i][j]
                if val != '.':
                    rows[i][val] += 1
                    cols[j][val] += 1
                    boxs[3*(i//3) + (j//3)][val] += 1
                else:
                    count += 1
                    
            
        self.helper(arr, rows, cols, boxs, (0,0), count, ans)            
        return ans