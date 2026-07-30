def floodFill(image, sr, sc, color):
    if color == image[sr][sc]:
        return image
    return floodFill_recur(image, sr, sc, color, image[sr][sc], len(image[0]), len(image))

def floodFill_recur(image, sr, sc, color, og, length, breadth):
    print(f"Coloring {sr}, {sc}")
    image[sr][sc] = color
    #base case -> no adjacent cells are og color 
    if sr - 1 >= 0:

        if image[sr - 1][sc] == og:
            floodFill_recur(image, sr-1, sc, color, og, length, breadth)
   
    if sr + 1 < breadth:
        
        if image[sr + 1][sc] == og:
            floodFill_recur(image, sr+1, sc, color, og, length, breadth)

    if sc - 1 >= 0:

        if image[sr][sc - 1] == og:
            floodFill_recur(image, sr, sc-1, color, og, length, breadth)

    if sc + 1 < length:

        if image[sr][sc + 1] == og:
            floodFill_recur(image, sr, sc+1, color, og, length, breadth)
   
    return image



# print(floodFill([[1,1,1],
#                  [1,1,0],
#                  [1,0,1]], 1, 1, 2))

print(floodFill([[0,0,0],
                 [0,0,0],
                 [0,0,0]], 0, 0, 0))