#coding = utf-8

class leetcode_middle:
    def spira_order(self, matrix: list)->list:
        """
        54:给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。
        """
        m = len(matrix)
        n = len(matrix[0])
        ans = []
        use = [[False for _ in range(n)] for _ in range(m)]
        top_right = n - 1
        bottom_right = m - 1
        top_left = 0
        bottom_left = 0
        row = 0
        col = 0
        while row < bottom_right or col < top_right:
            if not use[row][col]:
                ans.append(matrix[row][col])
            else:
                #碰到等于True，则退一个格转向
                pass
                 
        return ans
                

lm = leetcode_middle()
print(lm.spira_order(matrix = [[1,2,3],[4,5,6],[7,8,9]]))