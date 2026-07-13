class Solution:
    def floodFill(self, image, sr: int, sc: int, color: int):
        source = image[sr][sc]
        rows = len(image)
        columns =len(image[0])
        if image[sr][sc] == color:
            return image
        def dfs(r,c):
            if r<0 or c<0 or r>rows-1 or c>columns-1 or image[r][c] != source:
                return
            image[r][c] = color
            dfs(r-1,c)
            dfs(r+1,c)
            dfs(r,c-1)
            dfs(r,c+1)
        dfs(sr,sc)
        return image

                
