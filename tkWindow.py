from matplotlib.figure import Figure

from algAnnealing import algAnnealing
from tkinter import *
import matplotlib.pyplot as plt


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
            "root":root,
            "startTemp": float(startTemp.get()),
            "endTemp": float(endTemp.get()),
            "sizeBoard": int(sizeBoard.get()),
            "alpha": float(alpha.get()),
            "stepRepChange": int(stepRepChange.get())
        }
    ))
    button.grid(column=1, row=6)

    root.mainloop()


def line_input(root, name, coord):
    label = Label(root, text=name)
    label.grid(column=coord[0], row=coord[1])
    inputData = Entry(root, width=10)
    inputData.grid(column=coord[0] + 1, row=coord[1])
    return inputData


def button_clicked(data):
    alg =  algAnnealing(data)
    solution = alg.process()
    if solution == None:
        label = Label(data["root"], text="Решения нет")
        label.grid(column=2, row=7)
    else:
        drawBoard(data["root"],data["sizeBoard"], solution[0])
        plt.plot(solution[1], solution[2])
        plt.xlabel("Температура")
        plt.ylabel("Энергия")
        plt.show()

def drawBoard(root, sizeBoard, solution):
    size = 10
    bg = 'white'

    canvas = Canvas(root, width=sizeBoard * size, height=sizeBoard* size, bg=bg)
    canvas.grid(column=2, row=7)

    for i in range(sizeBoard):
        for j in range(sizeBoard):
            x1, y1, x2, y2 = i * size, j * size, i * size + size, j * size + size
            if solution[i] == j:
                fill = "red"
            else:
                fill = 'black' if (i + j) % 2 else 'white'
            canvas.create_rectangle(x1, y1, x2, y2, fill=fill, outline=bg, width=3)

