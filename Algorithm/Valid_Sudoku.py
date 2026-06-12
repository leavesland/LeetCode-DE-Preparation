class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val ==".":
                    continue
                
                row = (i,val)
                col = (val,j)
                box = (i//3,j//3,val)
                if row in seen or col in seen or box in seen:
                    return False
                seen.add(row)
                seen.add(col)
                seen.add(box)
            
        return True





        """
        def helper1(check:List[str]):
            x={}
            for i in check:
                if i in x and i != ".":
                    return False
                else:
                    x[i] = 1
            return 1
        for i in board: #horizontal 
            x=helper1(i)
            if x == False:
                return False
        for i in range(9): #vertical
            x=[]
            for item in board:
                x.append(item[i])
            
            y= helper1(x)
            if y== False:
                return False
        #cut 9 3x3
        def cut(lower,upper):
            x=[]
            y=[]
            z=[]
            for i in range(lower,upper):
                for item in board[0:3]:
                    
                    x.append(item[i])
                    
                for item in board[3:6]:
                    y.append(item[i])
                
                for item in board[6:9]:
                    z.append(item[i])
            return x,y,z
        x1,y1,z1=cut(0,3)
        print(x1)
        if helper1(x1)==False or helper1(y1) == False or helper1(z1) == False:
            return False
        x1,y1,z1=cut(3,6)
        if helper1(x1)==False or helper1(y1) == False or helper1(z1) == False:
            return False
        x1,y1,z1=cut(6,9)
        if helper1(x1)==False or helper1(y1) == False or helper1(z1) == False:
            return False
        

        return True
        """


