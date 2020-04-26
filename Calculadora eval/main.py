from tkinter import *

window = Tk()
window.geometry("200x230")

resposta = str
strcalcu = str
listcalcu = []


def listacalcu(strcalcu, num):
    listcalcu.append(num)
    return listcalcu


def calculo(strcalcu):
    strcalcu = " ".join(listcalcu)
    resposta = eval(strcalcu)


resp = Label(window, height=3, width=42, bg='white', text='').grid(row=0, column=0, columnspan=20)
Button(window, height=1, width=4, text='1', command=lambda: listacalcu(listcalcu, "1")).grid(row=9, column=0, padx=0.15,
                                                                                             pady=0.15)
Button(window, height=1, width=4, text='2', command=lambda: listacalcu(listcalcu, "2")).grid(row=10, column=0,
                                                                                             padx=0.15,
                                                                                             pady=0.15)
Button(window, height=1, width=4, text='3', command=lambda: listacalcu(listcalcu, "3")).grid(row=11, column=0,
                                                                                             padx=0.15,
                                                                                             pady=0.15)
Button(window, height=1, width=4, text='4', command=lambda: listacalcu(listcalcu, "4")).grid(row=9, column=1, padx=0.15,
                                                                                             pady=0.15)
Button(window, height=1, width=4, text='5', command=lambda: listacalcu(listcalcu, "5")).grid(row=10, column=1,
                                                                                             padx=0.15,
                                                                                             pady=0.15)
Button(window, height=1, width=4, text='6', command=lambda: listacalcu(listcalcu, "6")).grid(row=11, column=1,
                                                                                             padx=0.15,
                                                                                             pady=0.15)
Button(window, height=1, width=4, text='7', command=lambda: listacalcu(listcalcu, "7")).grid(row=9, column=2, padx=0.15,
                                                                                             pady=0.15)
Button(window, height=1, width=4, text='8', command=lambda: listacalcu(listcalcu, "8")).grid(row=10, column=2,
                                                                                             padx=0.15,
                                                                                             pady=0.15)
Button(window, height=1, width=4, text='9', command=lambda: listacalcu(listcalcu, "9")).grid(row=11, column=2,
                                                                                             padx=0.15,
                                                                                             pady=0.15)
Button(window, height=1, width=4, text='+', command=lambda: listacalcu(listcalcu, "+")).grid(row=9, column=3, padx=0.15,
                                                                                             pady=0.15)
Button(window, height=1, width=4, text='-', command=lambda: listacalcu(listcalcu, "-")).grid(row=10, column=3,
                                                                                             padx=0.15, pady=0.15)
Button(window, height=1, width=4, text='/', command=lambda: listacalcu(listcalcu, "/")).grid(row=11, column=3,
                                                                                             padx=0.15, pady=0.15)
Button(window, height=1, width=4, text='*', command=lambda: listacalcu(listcalcu, "*")).grid(row=12, column=3,
                                                                                             padx=0.15, pady=0.15)

Button(window, height=4, width=14, text='Calcular',
       command=lambda: calculo(listcalcu)).grid(row=12, column=0, rowspan=7, columnspan=3, padx=0.15,
                                                pady=0.15)
window.mainloop()
