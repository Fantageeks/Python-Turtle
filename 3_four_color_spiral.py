import turtle

s = turtle.Screen() #宣告一個畫布，要在上面製作圖形，並用一個變數s紀錄畫布的位置資訊
s.setup(width=500, height=500, startx=-30, starty=-30)  #設定畫布的大小(寬pixels, 長pixels)，設定畫筆的起始位置

turtle.bgcolor("#FFE4E1")  #設定背景顏色，顏色的表示時RGB色碼表
turtle.shape("triangle")      #畫筆表示圖案 "arrow", "circle", "square", "triangle", "classic"

turtle.speed(0)
turtle.color("#008B8B")  #設定畫筆顏色
turtle.pensize(2)

colors = ["red", "gray", "blue", "green"]
turtle.penup()
turtle.goto(0, 0)
turtle.pendown()

for x in range(300):
    turtle.color(colors[x%4])
    turtle.forward(x*2)
    turtle.right(91)

turtle.hideturtle()
turtle.penup()
turtle.goto(-150, -150)
turtle.pendown()
turtle.write("Four-colors Sqaure Spiral", font=("Times", 25, "bold"))
