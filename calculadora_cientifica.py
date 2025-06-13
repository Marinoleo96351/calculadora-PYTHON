import tkinter as tk
from math import *

class CalculadoraCientifica:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora Científica - Tema Escuro")
        self.root.geometry("400x550")
        self.root.resizable(False, False)
        self.expressao = ""

        self.entrada_texto = tk.StringVar()

        self.criar_interface()

    def criar_interface(self):
        self.root.configure(bg="#1e1e1e")

        entrada = tk.Entry(self.root, font=('Consolas', 20), textvariable=self.entrada_texto,
                           bd=10, insertwidth=2, width=22, borderwidth=4, relief='ridge',
                           justify='right', bg="#2e2e2e", fg="white")
        entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        botoes = [
            ('C', 1, 0), ('←', 1, 1), ('(', 1, 2), (')', 1, 3),
            ('sin', 2, 0), ('cos', 2, 1), ('tan', 2, 2), ('√', 2, 3),
            ('7', 3, 0), ('8', 3, 1), ('9', 3, 2), ('÷', 3, 3),
            ('4', 4, 0), ('5', 4, 1), ('6', 4, 2), ('×', 4, 3),
            ('1', 5, 0), ('2', 5, 1), ('3', 5, 2), ('-', 5, 3),
            ('0', 6, 0), ('.', 6, 1), ('π', 6, 2), ('+', 6, 3),
            ('log', 7, 0), ('ln', 7, 1), ('^', 7, 2), ('=', 7, 3),
            ('e', 8, 0), ('e^x', 8, 1), ('x!', 8, 2)
        ]

        for (texto, linha, coluna) in botoes:
            tk.Button(self.root, text=texto, padx=20, pady=20, font=('Arial', 14),
                      bg="#333", fg="white", activebackground="#00ffcc", activeforeground="black",
                      command=lambda t=texto: self.clique(t)).grid(row=linha, column=coluna, sticky='nsew')

        for i in range(9):
            self.root.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.root.grid_columnconfigure(i, weight=1)

    def clique(self, item):
        if item == "C":
            self.expressao = ""
        elif item == "←":
            self.expressao = self.expressao[:-1]
        elif item == "=":
            try:
                expressao = self.expressao.replace('÷', '/').replace('×', '*').replace('π', str(pi))
                expressao = expressao.replace('^', '**').replace('√', 'sqrt').replace('e', str(e))
                resultado = eval(expressao)
                self.expressao = str(resultado)
            except:
                self.expressao = "Erro"
        elif item == "ln":
            self.expressao += "log("
        elif item == "e^x":
            self.expressao += f"{e}**"
        elif item == "x!":
            try:
                valor = int(eval(self.expressao))
                self.expressao = str(factorial(valor))
            except:
                self.expressao = "Erro"
        elif item in ["sin", "cos", "tan", "log", "√"]:
            self.expressao += item + "("
        elif item == "e":
            self.expressao += str(e)
        else:
            self.expressao += str(item)

        self.entrada_texto.set(self.expressao)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculadoraCientifica(root)
    root.mainloop()
