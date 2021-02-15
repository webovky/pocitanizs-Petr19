
from os.path import basename, splitext
import tkinter as tk
from random import randint

class Application(tk.Tk):
    name = basename(splitext(basename(__file__.capitalize()))[0])
    name = 'Foo'

    def __init__(self):
        super().__init__(className=self.name)

        self.title(self.name)

        self.lbl = tk.Label(self, text="operace:")
        self.lbl.grid(row=0, column=0, columnspan=3)

        self.ent = tk.Entry()
        self.ent.grid(row=0, column=3, columnspan=2)
        self.ent.insert(0,'+-*/')

        self.entX = tk.Entry()
        self.entX.grid(row=1, column=0)

        self.entY = tk.Entry()
        self.entY.grid(row=1, column=2)

        self.entV = tk.Entry()
        self.entV.grid(row=1, column=4)

        self.lbloperace = tk.Label(self, text='?')
        self.lbloperace.grid(row=1, column=1)

        self.lblop = tk.Label(self, text='=')
        self.lblop.grid(row=1, column=3)

        self.lblOK = tk.Label(self, text='?')
        self.lblOK.grid(row=2, column=0)

        self.lblstat = tk.Label(self, text='0/0')
        self.lblstat.grid(row=2, column=4)

        self.kkn = tk.Button(self, text='Výpočet', command=self.vypocet)
        self.kkn.grid()

        self.kkn.bind('<Enter>', self.ukazka)

        self.btn = tk.Button(self, text='Konec', command=self.quit)
        self.btn.grid()

        self.bind("<Escape>", self.quit)


    def quit(self, event=None):
        super().quit()


    def ukazka(self, event):
        print(event.x, event.y, event.num, event.type)
        print(dir(event))

    def show(self):
        self.entX.delete(0, tk.END)
        self.entX.insert(0, str(self.x))
        self.entY.delete(0, tk.END)
        self.entY.insert(0, str(self.y))
        self.entV.delete(0, tk.END)
        self.entV.insert(0, str(self.vysl))
    
    def plus(self):
        self.x = randint(1, 99)
        self.y = randint(0, 100 - self.x)
        self.vysl = self.x + self.y
        self.lbloperace.config(text='+')
        self.show()

    def minus(self):
        self.x = randint(1, 99)
        self.y = randint(0, self.x)
        self.vysl = self.x - self.y
        self.lbloperace.config(text='-')
        self.show()

    def krat(self):
        self.x = randint(1, 9)
        self.y = randint(1, 9)
        self.vysl = self.x * self.y
        self.lbloperace.config(text='*')
        self.show()

    def deleno(self):
        self.vysl = randint(1, 9)
        self.y = randint(1, 9)
        self.x = self.vysl * self.y
        self.lbloperace.config(text='/')
        self.show()

    def vypocet(self):
        operace = (self.plus, self.minus, self.krat, self.deleno)
        nahoda = randint(0, 3)
        funkce = operace[nahoda]
        funkce()
        print()
        print(self.x, funkce.__name__, self.y, '=', self.vysl)

app = Application()
app.mainloop()