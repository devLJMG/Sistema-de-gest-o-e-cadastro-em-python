#Desenvolvido por Luciano Gonçalves:

#Desenvolvido em 05/2023

 .python

import pyodbc

from tkinter import *

from tkinter import ttk

dadosConexao = ("Driver={SQLite3 ODBC Driver};Server=hostname;Database=Compras_dados.db")


conexao = pyodbc.connect(dadosConexao)

conexao.execute("Select * From Produtos")
       
janela = Tk()
janela.title("Cadastro de Produtos")

janela.configure(bg="#F5DEB3")


def cadastrar():

    
    janela_cadastrar = Toplevel(janela)
    janela_cadastrar.title("Cadastrar Cliente")
    janela_cadastrar.configure(bg="#F5DEB3")
    
    largura_janela = 800
    altura_janela = 500

    largura_tela = janela_cadastrar.winfo_screenwidth()
    altura_tela = janela_cadastrar.winfo_screenheight()

    pos_x = (largura_tela // 2) - (largura_janela // 2)
    pos_y = (altura_tela // 2) - (altura_janela // 2)

    janela_cadastrar.geometry('{}x{}+{}+{}'.format(largura_janela, altura_janela, pos_x, pos_y ))
    
    
    estilo_borda = {"borderwidth": 2, "relief": "groove"}
     
    
    Label(janela_cadastrar, text="Nome do Cliente:", font=("Arial", 16), bg="#F5DEB3").grid(row=0, column=0, padx=10, pady=10, stick="W")
    cliente_cadastrar = Entry(janela_cadastrar, font=("Arial", 16), **estilo_borda)
    cliente_cadastrar.grid(row=0, column=1, padx=10, pady=10)    
    
    Label(janela_cadastrar, text="Endereço: ", font=("Arial", 16), bg="#F5DEB3").grid(row=1,  column=0, padx=10, pady=10, stick="W")
    cliente_cadastrar = Entry(janela_cadastrar, font=("Arial", 16), **estilo_borda)
    cliente_cadastrar.grid(row=1, column=1, padx=10, pady=10)    
    
    Label(janela_cadastrar, text="Contato(email ou tel)", font=("Arial", 16), bg="#F5DEB3").grid(row=2, column=0, padx=10, pady=10, stick="W")
    cliente_cadastrar = Entry(janela_cadastrar, font=("Arial", 16), **estilo_borda)
    cliente_cadastrar.grid(row=2, column=1, padx=10, pady=10) 
    
    Label(janela_cadastrar, text="Fumante:", font=("Arial", 16), bg="#F5DEB3").grid(row=3, column=0, padx=10, pady=10, stick="W")
    cliente_dados = Entry(janela_cadastrar, font=("Arial", 16), **estilo_borda)
    cliente_dados.grid(row=3, column=1, padx=10, pady=10) 
    
    
    Label(janela_cadastrar, text="Biótipo Cutâneo", font=("Arial", 28), bg="#F5DEB3").grid(row= 4, column=0, padx=10, pady=10, stick="W")
        
    var1 = IntVar()  
    
    chek = Checkbutton(janela_cadastrar, text="Pele Normal (Eudérmica)", font=("Arial", 12), bg="#F5DEB3", var="var1", onvalue=1, offvalue=0, command=salvar_dados)
    chek.grid(row=6, column=0)
    
    Var2 = IntVar()  
    
    chek = Checkbutton(janela_cadastrar, text="Pele Mista", font=("Arial", 12), bg="#F5DEB3", var="Var2", onvalue=1, offvalue=0, command=salvar_dados)
    chek.grid(row=6, column=1,  stick="W")
    
    Var3 = IntVar()  
    
    chek = Checkbutton(janela_cadastrar, text="Pele Lipídica", font=("Arial", 12), bg="#F5DEB3", var="Var3", onvalue=1, offvalue=0, command=salvar_dados)
    chek.grid(row=6, column=2,  stick="W")
    
    Var4 = IntVar()  
    
    chek = Checkbutton(janela_cadastrar, text="Pele Atipíca", font=("Arial", 12), bg="#F5DEB3", var="Var4", onvalue=1, offvalue=0, command=salvar_dados)
    chek.grid(row=6, column=3,  stick="W")
    

    
    Label(janela_cadastrar, text="Desequilibrios", font=("Arial", 28), bg="#F5DEB3").grid(row= 7, column=0, padx=10, pady=10, stick="W")
    
    Var5 = IntVar()  
    
    chek = Checkbutton(janela_cadastrar, text="Pele Desidratada", font=("Arial", 12), bg="#F5DEB3", var="Var5", onvalue=1, offvalue=0, command=salvar_dados)
    chek.grid(row=8, column=0)
    
    Var6 = IntVar()
        
    chek = Checkbutton(janela_cadastrar, text="Pele Sensível", font=("Arial", 12), bg="#F5DEB3", var="Var6", onvalue=1, offvalue=0, command=salvar_dados)
    chek.grid(row=8, column=1, stick="W")
    
    Var7 = IntVar()
        
    chek = Checkbutton(janela_cadastrar, text="Pele Reativa", font=("Arial", 12), bg="#F5DEB3", var="Var7", onvalue=1, offvalue=0, command=salvar_dados)
    chek.grid(row=8, column=2,  stick="W")
    
    Var8 = IntV

    chek = Checkbutton(janela_cadastrar, text="Pele com acne", font=("Arial", 12), bg="#F5DEB3", var="Var8", onvalue=1, offvalue=0, command=salvar_dados)
    chek.grid(row=8, column=3)
    
    Var9 = IntVar()
    
    chek = Checkbutton(janela_cadastrar, text="Acne inflamatória", font=("Arial", 12), bg="#F5DEB3", var="Var9", onvalue=1, offvalue=0, command=salvar_dados)
    chek.grid(row=9, column=0)
    
    Var10 = IntVar()
    
    chek = Checkbutton(janela_cadastrar, text="Pele com Manchas", font=("Arial", 12), bg="#F5DEB3", var="Var10", onvalue=1, offvalue=0, command=salvar_dados)
    chek.grid(row=9, column=1, stick="W")
    
    Var11 = IntVar()
    
    chek = Checkbutton(janela_cadastrar, text="Manchas Espalhadas", font=("Arial", 12), bg="#F5DEB3", var="Var11", onvalue=1, offvalue=0, command=salvar_dados)
    chek.grid(row=9, column=2,  stick="W")
    
    Var12 = IntVar()
    
    chek = Checkbutton(janela_cadastrar, text="Melasma", font=("Arial", 12), bg="#F5DEB3", var="Var12", onvalue=1, offvalue=0, command=salvar_dados)
    chek.grid(row=9, column=3,  stick="W")
    
    Var13 = IntVar()
        
    chek = Checkbutton(janela_cadastrar, text="Manchas Espalhadas", font=("Arial", 12), bg="#F5DEB3", var="Var13", onvalue=1, offvalue=0, command=salvar_dados)
    chek.grid(row=9, column=4, stick="W")
    
    Label(janela_cadastrar, text="Presença de Rugas", font=("Arial", 28), bg="#F5DEB3").grid(row= 10, column=0, padx=10, pady=10, stick="W")

    Label(janela_cadastrar, text="Intensidade de Rugas", font=("Arial", 28), bg="#F5DEB3").grid(row= 10, column=2, padx=10, pady=10, stick="W")    
    
    Var14 = IntVar()
    
    chek = Checkbutton(janela_cadastrar, text="Rugas de Exressão (30+) - Periorbitais/Glabela", font=("Arial", 12), bg="#F5DEB3", var="Var14", onvalue=1, offvalue=0, command=salvar_dados)
    chek.grid(row=11, column=0, stick="W")

    Var15 = IntVar()
    
    chek = Checkbutton(janela_cadastrar, text="Rugas Estáticas (40+) - Sulco Nasolabial/Bolsas Oculares", font=("Arial", 12), bg="#F5DEB3", var="Var15", onvalue=1, offvalue=0, command=salvar_dados)
    chek.grid(row=12, column=0, stick="W")
    
     
    Var16 = IntVar()
        
    chek = Checkbutton(janela_cadastrar, text="Rugas Gravitacionais (50+) - Labiais/Contorno Mandibular", font=("Arial", 12), bg="#F5DEB3", var="Var16", onvalue=1, offvalue=0, command=salvar_dados)
    chek.grid(row=13, column=0, stick="W")
    
    Var17 = IntVar()
    
    chek = Checkbutton(janela_cadastrar, text="Rugas Compostas (60+) - Generalizadas/Perda Volumétrica", font=("Arial", 12), bg="#F5DEB3", var="Var17", onvalue=1, offvalue=0, command=salvar_dados)
    chek.grid(row=14, column=0, stick="W")
    
    Var18 = IntVar()
    
    chek = Checkbutton(janela_cadastrar, text="Suave", font=("Arial", 12), bg="#F5DEB3", var="Var18", onvalue=1, offvalue=0, command=salvar_dados)
    chek.grid(row=11, column=2, stick="W")
    
    Var19 = IntVar()
    
    
    chek = Checkbutton(janela_cadastrar, text="Moderada", font=("Arial", 12), bg="#F5DEB3", var="Var19", onvalue=1, offvalue=0, command=salvar_dados)
    chek.grid(row=12, column=2, stick="W")
    
    Var20 = IntVar()
    
    chek = Checkbutton(janela_cadastrar, text="Avançada", font=("Arial", 12), bg="#F5DEB3", var="Var20", onvalue=1, offvalue=0, command=salvar_dados)
    chek.grid(row=13, column=2, stick="W")
    
    Var21 = IntVar()
    
    chek = Checkbutton(janela_cadastrar, text="Severa", font=("Arial", 12), bg="#F5DEB3", var="Var21", onvalue=1, offvalue=0, command=salvar_dados)
    chek.grid(row=14, column=2, stick="W")
    
    
    Label(janela_cadastrar, text="Fototipo", font=("Arial", 28), bg="#F5DEB3").grid(row=15, column=0, padx=10, pady=10, stick="W")    
    
    chek = Checkbutton(janela_cadastrar, text="I - Branco/Loiro-nunca bronzeia", font=("Arial", 12), bg="#F5DEB3", var="Var21", onvalue=1, offvalue=0, command=salvar_dados)
    chek.grid(row=16, column=0, stick="W")
    
    chek = Checkbutton(janela_cadastrar, text=

    Label(janela_cadastrar, text="Fototipo", font=("Arial", 28), bg="#F5DEB3").grid(row=15, column=0, padx=10, pady=10, stick="W")    
    
    chek = Checkbutton(janela_cadastrar, text="I - Branco/Loiro-nunca bronzeia", font=("Arial", 12), bg="#F5DEB3", var="Var21", onvalue=1, offvalue=0, command=salvar_dados)
    chek.grid(row=16, column=0, stick="W")
    
    chek = Checkbutton(janela_cadastrar, text="II - Branco/Dificilmente bronzeia", font=("Arial", 12), bg="#F5DEB3", var="Var21", onvalue=1, offvalue=0, command=salvar_dados)
    chek.grid(row=17, column=0, stick="W")
    
    chek = Checkbutton(janela_cadastrar, text="III - Moreno Claro/bronzeia moderadamente", font=("Arial", 12), bg="#F5DEB3", var="Var21", onvalue=1, offvalue=0, command=salvar_dados)
    chek.grid(row=18, column=0, stick="W")
    
    chek = Checkbutton(janela_cadastrar, text="IV - Moreno Moderado - bronzeia facilmente", font=("Arial", 12), bg="#F5DEB3", var="Var21", onvalue=1, offvalue=0, command=salvar_dados)
    chek.grid(row=19, column=1, stick="W")
    
    chek = Checkbutton(janela_cadastrar, text="V - Moreno Escuroo - bronzeia intensamente", font=("Arial", 12), bg="#F5DEB3", var="Var21", onvalue=1, offvalue=0, command=salvar_dados)
    chek.grid(row=20, column=1, stick="W")
    
    chek = Checkbutton(janela_cadastrar, text="VI - Negro - não se queima", font=("Arial", 12), bg="#F5DEB3", var="Var21", onvalue=1, offvalue=0, command=salvar_dados)
    chek.grid(row=21, column="10", stick="W")
     
    vbar = ttk.Scrollbar(janela_cadastrar, orient=VERTICAL)      ## vertical scrollbar
    vbar.grid(row=9, column=2, sticky="NS")
    hbar = ttk.Scrollbar(janela_cadastrar, orient=HORIZONTAL)    ## horizontal scrollbar
    hbar.grid(row=9, column=2, sticky="EW")

    
def salvar_dados():
        
        cursor.execute("SELECT * From Usuarios")

        novo_produto_cadastrar = (novo_produto_cadastrar.get(), descricao_produto_cadastrar.get(), preco_produto_cadastrar.get())
        cursor.execute("INSERT INTO Usuarios (NomeProduto, Descricao, preco) values (?, ?, ?)", dados_usuario)
        conexao.commit()
        
        janela_cadastrar.destroy()
        
        listar_dados()

        cursor.execute("SELECT * From Usuarios")

        valores = cursor.fetchall()

        botao_salvar_dados = Button(janela_cadastrar, text="Salvar", font=("Arial 12"), command=salvar_dados)
        botao_salvar_dados.grid(row=3, column=0, padx=10, pady=10, stick="NSEW")

        
        
        botao_cancelar_dados = Button(janela_cadastrar, text="cancelar", font=("Arial 12"), command=janela_cadastrar.destroy)
        botao_cancelar_dados.grid(row=4, column=0, padx=10, pady=10, stick="NSEW")
     
botao_gravar = Button(janela, text="Novo", command=cadastrar, font="Arial 26")
botao_gravar.grid(row=4, column=0, columnspan=4, stick="NSEW")

janela.attributes("-fullscreen", True)

menu_barra = Menu(janela)
janela.configure(menu=menu_barra)


Label(janela, text="Nome do Produto: ", font="Arial 16", bg="#F5F5F5").grid(row=0, column=2, padx=10,pady=10)
nome_produto = Entry(janela, font="Arial 16")
nome_produto.grid(row=0, column=3, padx=10, pady=10)

Label(janela, text="Descrição do Produto: ", font="Arial 16", bg="#F5F5F5").grid(row=0, column=5, padx=10,pady=10)
descricao_produto = Entry(janela, font="Arial 16")
descricao_produto.grid(row=0, column=6, padx=10, pady=10)

Label(janela, text="Produtos", font="Arial 16", bg="#F5F5F5").grid(row=2, column=0, columnspan=8, padx=20, pady=10)


style = ttk.Style(janela)

treeview = ttk.Treeview(janela, style="mystyle.Treeview")
style.theme_use("default")


style.configure("mystyle.Treevieew", font=("Arial", 14))

treeview = ttk.Treeview(janela, style="mystyle.Treeview", columns=("ID", "Nome", "Descricao", "Preco"), show="headings", height=20)

treeview.heading("ID", text="ID")
treeview.heading("Nome", text="Nome")
treeview.heading("Descricao", text="Descricao do Produto")
treeview.heading("Preco", text="Preço do Produto")


treeview.column("#0",

treeview.column("#0", width=0)
treeview.column("ID", width=100)
treeview.column("Nome", width=300)
treeview.column("Descricao", width=500)
treeview.column("Preco", width=200)

treeview.grid(row=3, column=0, columnspan=10, stick="NSEW")


menu_arquivo = Menu(menu_barra, tearoff=0)
menu_barra.add_cascade(label="Arquivo", menu=menu_arquivo)

menu_arquivo.add_command(label="Cadastrar", command=cadastrar)

menu_arquivo.add_command(label="Sair", command=janela.destroy)

botao_deletar = Button(janela, text="Deletar", command=cadastrar, font="Arial 26")
botao_gravar.grid(row=4, column=4, columnspan=4, stick="NSEW", padx=10, pady=5)

janela.mainloop()
