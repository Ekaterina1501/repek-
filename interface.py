from tkinter import *
from tkinter import messagebox
from mixMethods import *
import copy

def createWindow():
    window = Tk()
    window.title("Sudoku")
    window.geometry('520x410')
    return window

def getEntry(window):  # функция отрисовки интерфейса
    # создание холста и разграничивающих ячейки линий
    n = 400
    c = Canvas(window, width=n, height=n, bg='white')
    c.grid(columnspan=9, rowspan=9)
    c.create_line(1, n / 3, n, n / 3)
    c.create_line(1, 2 * n / 3, n, 2 * n / 3)
    c.create_line(n / 3, 1, n / 3, n)
    c.create_line(2 * n / 3, 1, 2 * n / 3, n)

    # прорисовка рамки судоку
    c.create_line(n, 1, n, n)
    c.create_line(1, n, n, n)
    c.create_line(2, 2, n, 2)
    c.create_line(2, 2, 2, n)

    # надпись о выборе уровня сложности
    label1 = Label(window, text="Выбрать уровень \n сложности:")
    label1.grid(column=9, row=6)

    # создание выпадащего списка с выбором уровня сложности
    global variable
    variable = StringVar(window)
    variable.set("Легкий     ")  # default value
    w = OptionMenu(window, variable, "Легкий     ", "Средний  ", "Сложный")
    w.grid(column=9, row=7)

    # создание ячеек
    entries = []
    for i in range(9):
        for j in range(9):
            entry = Entry(window, width=2, font=("Helvetica", 12), justify=CENTER, state=DISABLED)
            entries.append(entry)
            entry.grid(row=j, column=i, ipadx=5, ipady=3, padx=5, pady=5)
    return entries

window = createWindow()
entries = getEntry(window)


# создание кнопок
def unlock():
    global difficult
    difficult = 0
    # при нажатии кнопка "новая игра" необходимо генерировать каждый раз новую матрицу, в зависимости от выбранного уровня сложности
    if variable.get() == "Легкий     ":
        while difficult < 25:
            tableStart = getStartMatrix()
            table = mix(tableStart)
            newTable = copy.deepcopy(table)
            result = deleteElements(table)
            table = result[0]
            difficult = result[1]
            trTable = transposing(table)
    elif variable.get() == "Средний  ":
        while difficult < 22 or difficult > 24 :
            tableStart = getStartMatrix()
            table = mix(tableStart)
            newTable = copy.deepcopy(table)
            result = deleteElements(table)
            table = result[0]
            difficult = result[1]
            trTable = transposing(table)
    elif variable.get() == "Сложный":
        while difficult < 1 or difficult > 22:
            tableStart = getStartMatrix()
            table = mix(tableStart)
            newTable = copy.deepcopy(table)
            result = deleteElements(table)
            table = result[0]
            difficult = result[1]
            trTable = transposing(table)

    # принт нужен только для того, чтобы знать правильный ответ на судоку для теста кнопки "проверка"
    print("--------------")
    for i in newTable:
        print(i)
    newTable = transposing(newTable)

    # с ch будет сравниваться ввод с клавиатуры
    global ch
    ch = []
    for i in range(len(newTable)):
        for j in range(len(newTable)):
            ch.append(newTable[i][j])


    # приводим матрицу к нужному виду для заполнения
    global tableForInsert
    tableForInsert = []
    for i in range(len(trTable)):
        for j in range(len(trTable)):
            tableForInsert.append(str(trTable[i][j]))

    # делаем доступными все ячейки и очищаем их
    for i in entries:
        if i['state'] == DISABLED:
            i['state'] = NORMAL
        if i.get() != "":
            i.delete(0, END)

    # заполняем новыми значениями
    k = 0
    for q in entries:
        q.insert(0, tableForInsert[k])
        if q.get() != "":
            q['state'] = DISABLED
        k+=1

def check():
    k = 0
    for i in entries:
        p = i.get()
        if p == "":
            messagebox.showinfo("Oшибка", "Есть пустые ячейки")
            break
        if p != "1" and p != "2" and p != "3" and p != "4" and p != "5" and p != "6" and p != "7" and p != "8" and p != "9":
            messagebox.showinfo("Oшибка", "Где-то в ячейке присутствуют другие символы, помимо цифр 1-9")
            break
        if float(p) != ch[k]:
            u = str(k+1)
            messagebox.showinfo("Oшибка", "Есть ошибки в k =" + u)
            break
        k+=1
    if k == 81:
        messagebox.showinfo(" ", "Победа! ")

def createButtons(window):
    btnStart = Button(window, text="Новая игра", command = unlock)
    btnStart.grid(column = 9, row=8)

    btnCheck = Button(window, text="Проверить", command = check)
    btnCheck.grid(column = 9, row=0)