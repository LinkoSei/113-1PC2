def gray(array, i, j, value):
    array[i][j] = value
    return array

# 初始化 5x5 圖像矩陣
image = [[0 for _ in range(5)] for _ in range(5)]

# 更新圖像矩陣的值
gray(image, 0, 1, 50)
gray(image, 1, 2, 120)
gray(image, 2, 4, 180)
gray(image, 3, 2, 255)

# 輸出結果
for row in image:
    print(row)
