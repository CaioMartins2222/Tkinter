import tkinter as tk


def abrir_janela_venda():
    janela = tk.Tk()
    janela.title("Realizar Venda")
    janela.geometry("650x300+670+260")
    janela.resizable(False, False)
    janela.configure(bg="#FFE8E5")

    # Titulo
    titulo = tk.Label(janela, text="Glamour Fashion", anchor="center", bg="#FFE8E5")
    titulo.config(font=("Cooper Black", 25), fg="#EB0DAD")
    titulo.pack()
    subtitulo = tk.Label(janela, text="REALIZAR VENDA", anchor="center", bg="#FFE8E5")
    subtitulo.config(font=("Arial Black", 10))
    subtitulo.pack()

    # ID venda
    codigo = tk.Entry(janela, font=14, width=5)
    codigo.pack()
    codigo.place(x=50, y=108)

    # Rotulo ID Venda
    codigo_rotulo = tk.Label(janela, text="Código:", bg="#FFE8E5")
    codigo_rotulo.pack()
    codigo_rotulo.place(x=48, y=85)

    # Nome produto
    produto = tk.Entry(janela, font=14, width=40)
    produto.pack()
    produto.place(x=120, y=108)

    # Rotulo produto
    produto_rotulo = tk.Label(janela, text="Produto:", bg="#FFE8E5")
    produto_rotulo.pack()
    produto_rotulo.place(x=118, y=85)

    # Valor produto
    valor = tk.Entry(janela, font=14, width=9)
    valor.pack()
    valor.place(x=50, y=160)

    # Rotulo Valor produto
    valor_rotulo = tk.Label(janela, text="Valor:", bg="#FFE8E5")
    valor_rotulo.pack()
    valor_rotulo.place(x=50, y=138)

    # Data da venda
    data = tk.Entry(janela, font=14, width=12)
    data.pack()
    data.place(x=163, y=160)

    # Rotulo data da venda
    data_rotulo = tk.Label(janela, text="Data:", bg="#FFE8E5")
    data_rotulo.pack()
    data_rotulo.place(x=164, y=138)

    # Nome
    nome_completo = tk.Entry(janela, font=14, width=23)
    nome_completo.pack()
    nome_completo.place(x=309, y=160)

    # Rotulo Nome
    nome_rotulo = tk.Label(janela, text="Cliente:", bg="#FFE8E5")
    nome_rotulo.pack()
    nome_rotulo.place(x=311, y=138)

    def salvar_cadastro_venda():
        # Implemente a lógica de salvamento aqui
        codigo_valor = codigo.get()
        produto_valor = produto.get()
        valor_produto = valor.get()
        data_venda = data.get()
        cliente_nome = nome_completo.get()

        # Aqui você pode fazer o que quiser com os valores,
        # como salvar em um banco de dados, exibir em uma mensagem, etc.

        print("Código:", codigo_valor)
        print("Produto:", produto_valor)
        print("Valor do Produto:", valor_produto)
        print("Data da Venda:", data_venda)
        print("Cliente:", cliente_nome)
        janela.destroy()

    def cancelar_cadastro_venda():
        janela.destroy()

    button_cancelar = tk.Button(janela, text="Cancelar", font=("Cooper Black", 10), bg="#FC0FC0", fg="white", command= cancelar_cadastro_venda)
    button_cancelar.pack()
    button_cancelar.place(x=400, y=200)
    button_cancelar.config(width=9, height=1)

    button_salvar = tk.Button(janela, text="Salvar", font=("Cooper Black", 10), bg="#FC0FC0", fg="white", command= salvar_cadastro_venda)
    button_salvar.pack()
    button_salvar.place(x=495, y=200)
    button_salvar.config(width=9, height=1)


