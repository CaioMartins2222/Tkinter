import tkinter as tk


janela = tk.Tk()
janela.title("Loja de Roupas")
janela.geometry("600x360+750+300")

# Nome
nome_completo = tk.Entry(janela, font=14, width=56)
nome_completo.pack()
nome_completo.place(x=50, y=40)

# Rotulo Nome
nome_rotulo = tk.Label(janela, text="Nome:")
nome_rotulo.pack()
nome_rotulo.place(x=48, y=17)

# Nascimeto
nascimento = tk.Entry(janela, font=14, width=14)
nascimento.pack()
nascimento.place(x=50, y=90)

# Rotulo nascimento
nascimento_rotulo = tk.Label(janela, text="Nascimento:")
nascimento_rotulo.pack()
nascimento_rotulo.place(x=48, y=67)

# Botao Feminino
radio_feminino = tk.Radiobutton(janela, text="F")
radio_feminino.pack()
radio_feminino.place(x=195, y=89)
# Botao Masculino
radio_masculino = tk.Radiobutton(janela, text="M")
radio_masculino.pack()
radio_masculino.place(x=245, y=89)

# Email
email = tk.Entry(janela, font=14, width=28)
email.pack()
email.place(x=301, y=90)
# Email Rotulo
email_rotulo = tk.Label(janela, text="E-mail:")
email_rotulo.pack()
email_rotulo.place(x=298, y=66)

# Rua
rua = tk.Entry(janela, font=14, width=56)
rua.pack()
rua.place(x=50, y=139)

# Rua rotulo
rua_rotulo = tk.Label(janela, text="Rua:")
rua_rotulo.pack()
rua_rotulo.place(x=48, y=117)

# Cidade
cidade = tk.Entry(janela, font=14, width=20)
cidade.pack()
cidade.place(x=50, y=189)

# Cidade rotulo

rua_rotulo = tk.Label(janela, text="Cidade:")
rua_rotulo.pack()
rua_rotulo.place(x=48, y=167)

janela.mainloop()