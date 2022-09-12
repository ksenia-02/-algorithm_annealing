import algAnnealing
from tkinter import *


def settingWindow(root):
    root.geometry('1300x700')
    root.title("Задача ферзей")

    startTemp = line_input(root, "Начальная температура", (0, 0))
    endTemp = line_input(root, "Конечная температура", (0, 1))
    sizeBoard = line_input(root, "Размер доски", (0, 2))
    queen = line_input(root, "Кол-во ферзей", (0, 3))
    alpha = line_input(root, "Альфа", (0, 4))
    stepRepChange = line_input(root, "Кол-во итераций", (0, 5))

    button = Button(root, text="Ввод", command=lambda: button_clicked(
        {
            "startTemp": startTemp.get(),
            "endTemp": endTemp.get(),
            "sizeBoard": sizeBoard.get(),
            "queen": queen.get(),
            "alpga": alpha.get(),
            "stepRepChange": stepRepChange.get()
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
    algAnnealing.process(data)
