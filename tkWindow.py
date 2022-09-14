import algAnnealing
from tkinter import *


def settingWindow(root):
    root.geometry('1300x700')
    root.title("Задача ферзей")

    startTemp = line_input(root, "Начальная температура", (0, 0))
    endTemp = line_input(root, "Конечная температура", (0, 1))
    sizeBoard = line_input(root, "Размер доски", (0, 2))
    alpha = line_input(root, "Альфа", (0, 3))
    stepRepChange = line_input(root, "Кол-во итераций", (0, 4))

    button = Button(root, text="Ввод", command=lambda: button_clicked(
        {
            "startTemp": startTemp.get(),
            "endTemp": endTemp.get(),
            "sizeBoard": sizeBoard.get(),
            "alpga": alpha.get(),
            "stepRepChange": stepRepChange.get()
        }
    ))
    button.grid(column=1, row=6)
    drawBoard(root,8,[i for i in range(int(8))])
    root.mainloop()


def line_input(root, name, coord):
    label = Label(root, text=name)
    label.grid(column=coord[0], row=coord[1])
    inputData = Entry(root, width=10)
    inputData.grid(column=coord[0] + 1, row=coord[1])
    return inputData


def button_clicked(data):
    algAnnealing.process(data)

def drawBoard(root, sizeBoard, solution):
    size = 30
    bg = 'white'
    canvas = Canvas(root, width=sizeBoard * size, height=sizeBoard* size, bg=bg)
    canvas.grid(column=2, row=7)

    for i in range(8):
        for j in range(8):
            x1, y1, x2, y2 = i * size, j * size, i * size + size, j * size + size
            if solution[i] == j:
                fill = "red"
            else:
                fill = 'black' if (i + j) % 2 else 'white'
            canvas.create_rectangle(x1, y1, x2, y2, fill=fill, outline=bg, width=3, tags="Q")

