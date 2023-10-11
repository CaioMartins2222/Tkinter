import tkinter as tk


janela = tk.Tk()
janela.title("Loja de Roupas")
janela.geometry("600x335+700+300")
janela.resizable(False, False)

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

# Email1
email = tk.Entry(janela, font=14, width=28)
email.pack()
email.place(x=301, y=90)
# Email Rotulo
email_rotulo = tk.Label(janela, text="E-mail:")
email_rotulo.pack()
email_rotulo.place(x=298, y=66)

# Rua
rua = tk.Entry(janela, font=14, width=46)
rua.pack()
rua.place(x=50, y=139)

# Rua rotulo
rua_rotulo = tk.Label(janela, text="Rua:")
rua_rotulo.pack()
rua_rotulo.place(x=48, y=117)

# Numero
rua = tk.Entry(janela, font=14, width=5)
rua.pack()
rua.place(x=509, y=139)

# Numero rotulo
rua_rotulo = tk.Label(janela, text="N°:")
rua_rotulo.pack()
rua_rotulo.place(x=508, y=117)

# Cidade
cidade = tk.Entry(janela, font=14, width=20)
cidade.pack()
cidade.place(x=50, y=189)

# Cidade rotulo

rua_rotulo = tk.Label(janela, text="Cidade:")
rua_rotulo.pack()
rua_rotulo.place(x=48, y=167)

# UF
uf = tk.Entry(janela, font=14, width=5)
uf.pack()
uf.place(x=277, y=189)

# Uf rotulo
rua_rotulo = tk.Label(janela, text="UF:")
rua_rotulo.pack()
rua_rotulo.place(x=275, y=167)

# Cep
cep = tk.Entry(janela, font=14, width=20)
cep.pack()
cep.place(x=373, y=189)

# Cep Rotulo
cep_rotulo = tk.Label(janela, text="Cep:")
cep_rotulo.pack()
cep_rotulo.place(x=371, y=167)

# ID
id = tk.Entry(janela, font=14, width=10)
id.pack()
id.place(x=50, y=239)

# ID rotulo

id_rotulo = tk.Label(janela, text="ID:")
id_rotulo.pack()
id_rotulo.place(x=48, y=217)


# Celular DDD
celular_ddd = tk.Entry(janela, font=14, width=5)
celular_ddd.pack()
celular_ddd.place(x=277, y=239)

# Celular DDD rotulo

celular_Dd_rotulo = tk.Label(janela, text="DDD:")
celular_Dd_rotulo.pack()
celular_Dd_rotulo.place(x=276, y=217)

#  Numero
numero = tk.Entry(janela, font=14, width=20)
numero.pack()
numero.place(x=373, y=239)

# Numero rotulo

numero_rotulo = tk.Label(janela, text="Número do Celular:")
numero_rotulo.pack()
numero_rotulo.place(x=373, y=217)


button_cancelar = tk.Button(janela, text="Cancelar")
button_cancelar.pack()
button_cancelar.place(x=380, y=285)
button_cancelar.config(width=9, height=2)

button_salvar = tk.Button(janela, text="Salvar")
button_salvar.pack()
button_salvar.place(x=480, y=285)
button_salvar.config(width=9, height=2)

janela.mainloop()