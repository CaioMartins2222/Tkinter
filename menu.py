from Cadastro import abrir_janela_cadastro
import tkinter as tk
from Venda import abrir_janela_venda

menu = tk.Tk()
menu.title("Menu Clientes")
menu.geometry("700x435+660+250")
menu.resizable(False, False)
menu.configure(bg="#FFE8E5")

# ID
id = tk.Entry(menu, font=14, width=6)
id.pack()
id.place(x=90, y=60)

# ID Nome
id_rotulo = tk.Label(menu, text="ID:", font=("Helvetica", 11), bg="#FFE8E5")
id_rotulo.pack()
id_rotulo.place(x=64, y=59)

# Nome
nome_completo = tk.Entry(menu, font=14, width=42)
nome_completo.pack()
nome_completo.place(x=245, y=60)

# Rotulo Nome
nome_rotulo = tk.Label(menu, text="Nome:", font=("Helvetica", 11), bg="#FFE8E5")
nome_rotulo.pack()
nome_rotulo.place(x=190, y=59)

# Data
data = tk.Entry(menu, font=14, width=12)
data.pack()
data.place(x=90, y=110)

# Data rotulo
data_rotulo = tk.Label(menu, text="Data:", font=("Helvetica", 11), bg="#FFE8E5")
data_rotulo.pack()
data_rotulo.place(x=45, y=110)



# Pesquisar
button_pesquisar = tk.Button(menu, text="Pesquisar", font=("Cooper Black", 12), bg="#EB0DAD", fg="White")
button_pesquisar.pack()
button_pesquisar.place(x=300, y=130)
button_pesquisar.config(width=10, height=1)

button_venda = tk.Button(menu, text="Cadastrar Venda", font=("Cooper Black", 12), bg="#EB0DAD", fg="White", command=abrir_janela_venda)
button_venda.pack()
button_venda.place(x=435, y=130)
button_venda.config(width=14, height=1)

# Cadastrar

button_cadastrar = tk.Button(menu, text="Cadastrar", bg="#EB0DAD", fg="White", font=("Cooper Black", 11),
                             command=abrir_janela_cadastro)
button_cadastrar.pack()
button_cadastrar.place(x=546, y=6)
button_cadastrar.config(width=10, height=1)

# Cadastrar rotulo
data_rotulo = tk.Label(menu, text="Clique para cadastrar um cliente.", font=("Helvetica", 9), bg="#FFE8E5")
data_rotulo.pack()
data_rotulo.place(x=355, y=10)

menu.mainloop()
