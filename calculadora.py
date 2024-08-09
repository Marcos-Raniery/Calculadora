import tkinter as tk
from tkinter import messagebox

#Funções de operação:
#
def adicionar():
    try:
        resultado.set(float(entrada1.get()) + float(entrada2.get()))
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira números válidos.")

def subtrair():
    try:
        resultado.set(float(entrada1.get()) - float(entrada2.get()))
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira números válidos.")

def multiplicar():
        try:
            resultado.set(float(entrada1.get()) * float(entrada2.get()))
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira números válidos.")

def dividir():
            try:
                if float(entrada2.get()) == 0:
                    raise ZeroDivisionError
                resultado.set((float(entrada1.get())) / float(entrada2.get()))
            except ValueError:
                messagebox.showerror("Erro", "Por favor, insira números válidos")
            except ZeroDivisionError:
                messagebox.showerror("Erro", "Divisão por zero não é permitida")

#Criar a janela principal
root = tk.Tk()

#alterar o título da janela principal
root.title("Calculadora")

#variáveis de entrada e resultados
entrada1 = tk.StringVar()
entrada2 = tk.StringVar()
resultado = tk.StringVar()

#Criar o layout da calculadora
tk.Label(root, text="Primeiro número: ").grid(row=0, column=0)
tk.Entry(root, textvariable=entrada1).grid(row=0, column=1)

tk.Label(root, text="Segundo número: ").grid(row=1, column=0)
tk.Entry(root, textvariable=entrada2).grid(row=1, column=1)
button_style= {
 #Fonte
    'font': ('Arial', 16),
#Cor do fundo do botão
    'bg': '#D92525',
#Cor do texto
    'fg': '#ffffff',
#Tipo de borda do botão
    'relief': 'raised',
#Tamanho da borda
    'bd': 3,
#Largura do botão
    'width': 1,
#Altura do botão
    'height': 1
}

tk.Button(root, text="+", command=adicionar, **button_style).grid(row=0, column=2)
tk.Button(root, text="-", command=subtrair, **button_style).grid(row=0, column=3)
tk.Button(root, text="*", command=multiplicar, **button_style).grid(row=1, column=2)
tk.Button(root, text="/", command=dividir, **button_style).grid(row=1, column=3)

tk.Label(root, text="Resultado: ").grid(row=3, column=0)
tk.Entry(root, textvariable=resultado, state='readonly').grid(row=2, column=1)

#iniciar a aplicação
root.mainloop()
