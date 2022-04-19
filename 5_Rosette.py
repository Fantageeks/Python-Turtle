import turtle

s = turtle.Screen() #宣告一個畫布，要在上面製作圖形，並用一個變數s紀錄畫布的位置資訊
s.setup(width=500, height=500, startx=0, starty=0)  #設定畫布的大小(寬pixels, 長pixels)，設定畫筆的起始位置

turtle.bgcolor("#FFE4E1")  #設定背景顏色，顏色的表示時RGB色碼表
turtle.shape("triangle")      #畫筆表示圖案 "arrow", "circle", "square", "triangle", "classic"

turtle.speed(0)
turtle.color("#008B8B")  #設定畫筆顏色


colors = ["red", "gray", "blue", "green"]

for _ in range(36):
    turtle.circle(90)
    turtle.left(10)
