
#-----------------------------------------------------------------------------------------------------------------------
import tkinter
import tkinter as tk
from tkinter import *
from tkinter import ttk
from time import strftime
import mysql.connector
from tkinter import messagebox
import math
from PIL import ImageTk, Image


#-----------------------------------------------------------------------------------------------------------------------

nomeAA = None

def pegarNome():

    global nomeAA

    banco = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="infoCaixa"
    )

    cursor = banco.cursor()

    comando1 = f"SELECT nome FROM cadastros WHERE id = {id.get()}"
    cursor.execute(comando1)

    u = cursor.fetchone()

    nomeAA = (u[0])




def app():

#-----------------------------------------------------------------------------------------------------------------------

    #CONEXÃO COM BANCO DE DADOS

    banco = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="infoCaixa"
    )

    cursor = banco.cursor()

#-----------------------------------------------------------------------------------------------------------------------

    #Função para tornar Entry apenas numeros

    def testVal(inStr,acttyp):
        if acttyp == '1': #insert
            if not inStr.isdigit():
                return False
        return True

#----------------------------------------------------------------------------------------------------------------------

    #Botão de editar

    def editarProduto():

        opc_menu = [
            'Outros',
            'Padaria',
            'Alimentos (cereais e grãos)',
            'Congelados e frios',
            'Hortifruti',
            'Produtos de limpeza',
            'Higiene pessoal',
            'Bebidas',
            'Papelaria'
        ]

        def FecharJanela():
            newWindow2.destroy()

        def resetPesq():
            newWindow2.destroy()
            editarProduto()

        def my_details():
            codigo1 = codigo.get()

            if codigo1 == '':
                Msg = tk.messagebox.showinfo(title="Alerta", message="Campo do nome está vazio! Formule-o novamente.")
                return addProduto()

            comando_SQL = "SELECT * from produtos WHERE codigo LIKE '%"+codigo1+"%'"
            cursor.execute(comando_SQL)
            records = cursor.fetchall()

            for i in records:
                m.insert("", "end", values=i)

        def select_item():
            name_box.delete(0, END)
            codigo_box.delete(0, END)
            preco_box.delete(0, END)
            estoque_box.delete(0, END)

            selected = m.focus()
            values = m.item(selected, 'values')

            name_box.insert(0, values[0])
            codigo_box.insert(0, values[1])
            preco_box.insert(0, values[2])
            estoque_box.insert(0, values[3])

        def update_item():
            selected = m.focus()

            m.item(selected, text='', values=(name_box.get(), codigo_box.get(), preco_box.get(), estoque_box.get(), variable.get()))

            sql_add = "UPDATE produtos SET nome = %s, codigo = %s, preco = %s, estoque = %s, tipo = %s WHERE codigo = %s"
            val = (f"{name_box.get()}", f"{codigo_box.get()}", f"{preco_box.get()}", f"{estoque_box.get()}", f"{variable.get()}", f"{codigo_box.get()}")

            cursor.execute(sql_add, val)
            banco.commit()


    #-----------------------------------------------------------------------------------------------------------------------

        #JANELA PARA ALGUMA FUNÇÃO

        newWindow2 = tk.Toplevel()

        newWindow2.geometry('800x455')
        center(newWindow2)
        newWindow2.resizable(width=False, height=False)

    #-----------------------------------------------------------------------------------------------------------------------

        txt1 = Label(newWindow2, text='Código do item:', fg='black', font='poppins 16')
        txt1.place(x=40, y=50)

        codigo = Entry(newWindow2, validate="key", background='#c1c1c3', fg='black', font='poppins 20 bold')
        codigo['validatecommand'] = (codigo.register(testVal),'%P','%d')
        codigo.place(x=40, y=100, width=290)

    #-----------------------------------------------------------------------------------------------------------------------

        btnFechar = Button(newWindow2, text='╳', background='#252525', fg='white', font='poppins 25', command=FecharJanela, borderwidth=0, cursor='tcross')
        btnFechar.place(x=590, y=22, width=190)

        btnPesq = Button(newWindow2, text='🔍', background='#252525', fg='white', font='poppins 13', command=my_details, borderwidth=0, cursor='tcross')
        btnPesq.place(x=340, y=99, width=60)

        btnReset = Button(newWindow2, text='↺', background='#252525', fg='white', font='poppins 13 bold', command=resetPesq, borderwidth=0, cursor='tcross')
        btnReset.place(x=720, y=380, width=60)

        comando_SQL = "SELECT * from produtos"
        cursor.execute(comando_SQL)
        records = cursor.fetchall()



        name_box = Entry(newWindow2, background='gray', fg='white', font='poppins 13 normal')
        name_box.place(x=40, y=300, width=200)

        codigo_box = Entry(newWindow2, background='gray', fg='white', font='poppins 13 normal')

        preco_box = Entry(newWindow2, background='gray', fg='white', font='poppins 13 normal')
        preco_box.place(x=245, y=300, width=100)

        estoque_box = Entry(newWindow2, background='gray', fg='white', font='poppins 13 normal')
        estoque_box.place(x=350, y=300, width=100)

        variable = tk.StringVar(newWindow2)
        variable.set(opc_menu[0])

        opt = tk.OptionMenu(newWindow2, variable, *opc_menu)
        opt.config(width=90, font='poppins 14', background='gray', foreground='white', borderwidth=3)
        opt.place(x=452, y=297, width=333, height=39)




        select_button = Button(newWindow2, text='Selecione o item', background='#252525', fg='white', font='poppins 13 normal', command=select_item, borderwidth=0, cursor='tcross')
        select_button.place(x=40, y=370)

        update_button = Button(newWindow2, text='Salve a alteração', background='#252525', fg='white', font='poppins 13 normal',  command=update_item, borderwidth=0, cursor='tcross')
        update_button.place(x=220, y=370)



        m = ttk.Treeview(newWindow2, columns=('Nome', 'Codigo', 'Preco', 'Estoque', 'Tipo'), show='headings')

        style = ttk.Style()
        style.configure("Treeview", font='Poppins 15', rowheight=35)
        style.configure("Treeview.Heading", font='Poppins 15')

        m.column('Nome', minwidth=0, width=250)
        m.column('Codigo', minwidth=0, width=100)
        m.column('Preco', minwidth=0, width=100)
        m.column('Estoque', minwidth=0, width=100)
        m.column('Tipo', minwidth=0, width=190)
        m.heading('Nome', text='Nome')
        m.heading('Codigo', text='Código')
        m.heading('Preco', text='Preço')
        m.heading('Estoque', text='Estoque')
        m.heading('Tipo', text='Tipo')
        m.place(x=40, y=180, height=80)


    #-----------------------------------------------------------------------------------------------------------------------

        atualiza()

        newWindow2.mainloop()

#----------------------------------------------------------------------------------------------------------------------

    #Botão de adicionar produto

    def pesqCadastro():

        def FecharJanela():
            newWindow.destroy()

        def resetPesq():
            id.delete(0, END)

        def my_details():
            id1 = id.get()

            if id1 == '':
                Msg = tk.messagebox.showinfo(title="Alerta", message="Campo do ID está vazio! Formule-o novamente.")
                return addProduto()

            comando_SQL = "SELECT * from cadastros WHERE id LIKE '%"+id1+"%'"
            cursor.execute(comando_SQL)
            records = cursor.fetchall()

            for i in records:
                m.insert("", "end", values=i)


    #-----------------------------------------------------------------------------------------------------------------------

        #JANELA PARA ALGUMA FUNÇÃO

        newWindow = tk.Toplevel()

        newWindow.geometry('700x455')
        center(newWindow)
        newWindow.resizable(width=False, height=False)

    #-----------------------------------------------------------------------------------------------------------------------

        txt1 = Label(newWindow, text='ID do item:', fg='black', font='poppins 16')
        txt1.place(x=40, y=50)

        id = Entry(newWindow, validate="key", background='#c1c1c3', fg='black', font='poppins 20 bold')
        id['validatecommand'] = (id.register(testVal),'%P','%d')
        id.place(x=40, y=100, width=290)

    #-----------------------------------------------------------------------------------------------------------------------

        btnFechar = Button(newWindow, text='╳', background='#252525', fg='white', font='poppins 25', command=FecharJanela, borderwidth=0, cursor='tcross')
        btnFechar.place(x=490, y=22, width=190)

        btnPesq = Button(newWindow, text='🔍', background='#252525', fg='white', font='poppins 13', command=my_details, borderwidth=0, cursor='tcross')
        btnPesq.place(x=340, y=99, width=60)

        btnReset = Button(newWindow, text='↺', background='#252525', fg='white', font='poppins 13 bold', command=resetPesq, borderwidth=0, cursor='tcross')
        btnReset.place(x=620, y=380, width=60)

        m = ttk.Treeview(newWindow, columns=('Nome', 'id', 'senha'), show='headings')

        style = ttk.Style()
        style.configure("Treeview", font='Poppins 15', rowheight=35)
        style.configure("Treeview.Heading", font='Poppins 15')

        m.column('Nome', minwidth=0, width=250)
        m.column('id', minwidth=0, width=100)
        m.column('senha', minwidth=0, width=100)
        m.heading('Nome', text='Nome')
        m.heading('id', text='ID')
        m.heading('senha', text='Senha')
        m.place(x=40, y=180, height=80)

    #-----------------------------------------------------------------------------------------------------------------------

        atualiza()

        newWindow.mainloop()

#----------------------------------------------------------------------------------------------------------------------

    #Botão de adicionar produto

    def pesqProduto():

        def FecharJanela():
            newWindow.destroy()

        def resetPesq():
            codigo.delete(0, END)

        def my_details():
            codigo1 = codigo.get()

            if codigo1 == '':
                Msg = tk.messagebox.showinfo(title="Alerta", message="Campo do nome está vazio! Formule-o novamente.")
                return addProduto()

            comando_SQL = "SELECT * from produtos WHERE codigo LIKE '%"+codigo1+"%'"
            cursor.execute(comando_SQL)
            records = cursor.fetchall()

            for i in records:
                m.insert("", "end", values=i)


    #-----------------------------------------------------------------------------------------------------------------------

        #JANELA PARA ALGUMA FUNÇÃO

        newWindow = tk.Toplevel()

        newWindow.geometry('700x455')
        center(newWindow)
        newWindow.resizable(width=False, height=False)

    #-----------------------------------------------------------------------------------------------------------------------

        txt1 = Label(newWindow, text='Código do item:', fg='black', font='poppins 16')
        txt1.place(x=40, y=50)

        codigo = Entry(newWindow, validate="key", background='#c1c1c3', fg='black', font='poppins 20 bold')
        codigo['validatecommand'] = (codigo.register(testVal),'%P','%d')
        codigo.place(x=40, y=100, width=290)

    #-----------------------------------------------------------------------------------------------------------------------

        btnFechar = Button(newWindow, text='╳', background='#252525', fg='white', font='poppins 25', command=FecharJanela, borderwidth=0, cursor='tcross')
        btnFechar.place(x=490, y=22, width=190)

        btnPesq = Button(newWindow, text='🔍', background='#252525', fg='white', font='poppins 13', command=my_details, borderwidth=0, cursor='tcross')
        btnPesq.place(x=340, y=99, width=60)

        btnReset = Button(newWindow, text='↺', background='#252525', fg='white', font='poppins 13 bold', command=resetPesq, borderwidth=0, cursor='tcross')
        btnReset.place(x=620, y=380, width=60)

        m = ttk.Treeview(newWindow, columns=('Nome', 'Codigo', 'Preco', 'Estoque'), show='headings')

        style = ttk.Style()
        style.configure("Treeview", font='Poppins 15', rowheight=35)
        style.configure("Treeview.Heading", font='Poppins 15')

        m.column('Nome', minwidth=0, width=250)
        m.column('Codigo', minwidth=0, width=100)
        m.column('Preco', minwidth=0, width=100)
        m.column('Estoque', minwidth=0, width=100)
        m.heading('Nome', text='Nome')
        m.heading('Codigo', text='Código')
        m.heading('Preco', text='Preço')
        m.heading('Estoque', text='Estoque')
        m.place(x=40, y=180, height=80)

    #-----------------------------------------------------------------------------------------------------------------------

        atualiza()

        newWindow.mainloop()

#----------------------------------------------------------------------------------------------------------------------

    #Botão de adicionar produto

    def removerCadastro():

        def FecharJanela():
            newWindow.destroy()

        def resetPesq():
            id.delete(0, END)

        def confirmarRem():

            if id.get() == "":
                tk.messagebox.showinfo(title="Alerta", message="Insira algo no campo de remoção!")
                return False

            else:
                id1 = id.get()

                if id1 == '':
                    Msg = tk.messagebox.showinfo(title="Alerta", message="Campo do id está vazio! Formule-o novamente.")
                    return addProduto()

                comando_SQL = "DELETE FROM cadastros WHERE id = "+ id1 +""

                cursor.execute(comando_SQL)
                banco.commit()

                Msg = tk.messagebox.askquestion(title="Alerta", message="Removido com sucesso! Deseja remover mais um cadastro?")

                if Msg == 'yes':
                    removerCadastro()
                else:
                    return False

    #-----------------------------------------------------------------------------------------------------------------------

        #JANELA PARA ALGUMA FUNÇÃO

        newWindow = tk.Toplevel()

        newWindow.geometry('700x455')
        center(newWindow)
        newWindow.resizable(width=False, height=False)

    #-----------------------------------------------------------------------------------------------------------------------

        txt1 = Label(newWindow, text='ID do item:', fg='black', font='poppins 16')
        txt1.place(x=40, y=160)

        id = Entry(newWindow, validate="key", background='#c1c1c3', fg='black', font='poppins 20 bold')
        id['validatecommand'] = (id.register(testVal),'%P','%d')
        id.place(x=40, y=210, width=290)

    #-----------------------------------------------------------------------------------------------------------------------

        btnRem = Button(newWindow, text='Remover', background='#252525', fg='white', font='poppins 25', command=confirmarRem, borderwidth=0, cursor='tcross')
        btnRem.place(x=490, y=330, width=190)

        btnFechar = Button(newWindow, text='╳', background='#252525', fg='white', font='poppins 25', command=FecharJanela, borderwidth=0, cursor='tcross')
        btnFechar.place(x=490, y=22, width=190)

        btnReset = Button(newWindow, text='↺', background='#252525', fg='white', font='poppins 13 bold', command=resetPesq, borderwidth=0, cursor='tcross')
        btnReset.place(x=620, y=260, width=57)

    #-----------------------------------------------------------------------------------------------------------------------

        atualiza()

        newWindow.mainloop()

#----------------------------------------------------------------------------------------------------------------------

    #Botão de adicionar produto

    def removerProduto():

        def FecharJanela():
            newWindow.destroy()

        def resetPesq():
            codigo.delete(0, END)

        def confirmarRem():

            if codigo.get() == "":
                tk.messagebox.showinfo(title="Alerta", message="Insira algo no campo de remoção!")
                return False

            else:
                codigo1 = codigo.get()

                if codigo1 == '':
                    Msg = tk.messagebox.showinfo(title="Alerta", message="Campo do nome está vazio! Formule-o novamente.")
                    return addProduto()

                comando_SQL = "DELETE FROM produtos WHERE codigo = "+ codigo1 +""

                cursor.execute(comando_SQL)
                banco.commit()

                Msg = tk.messagebox.askquestion(title="Alerta", message="Removido com sucesso! Deseja remover mais um produto?")

                if Msg == 'yes':
                    removerProduto()
                else:
                    return False

    #-----------------------------------------------------------------------------------------------------------------------

        #JANELA PARA ALGUMA FUNÇÃO

        newWindow = tk.Toplevel()

        newWindow.geometry('700x455')
        center(newWindow)
        newWindow.resizable(width=False, height=False)

    #-----------------------------------------------------------------------------------------------------------------------

        txt1 = Label(newWindow, text='Código do item:', fg='black', font='poppins 16')
        txt1.place(x=40, y=160)

        codigo = Entry(newWindow, validate="key", background='#c1c1c3', fg='black', font='poppins 20 bold')
        codigo['validatecommand'] = (codigo.register(testVal),'%P','%d')
        codigo.place(x=40, y=210, width=290)

    #-----------------------------------------------------------------------------------------------------------------------

        btnRem = Button(newWindow, text='Remover', background='#252525', fg='white', font='poppins 25', command=confirmarRem, borderwidth=0, cursor='tcross')
        btnRem.place(x=490, y=330, width=190)

        btnFechar = Button(newWindow, text='╳', background='#252525', fg='white', font='poppins 25', command=FecharJanela, borderwidth=0, cursor='tcross')
        btnFechar.place(x=490, y=22, width=190)

        btnReset = Button(newWindow, text='↺', background='#252525', fg='white', font='poppins 13 bold', command=resetPesq, borderwidth=0, cursor='tcross')
        btnReset.place(x=620, y=260, width=57)

    #-----------------------------------------------------------------------------------------------------------------------

        atualiza()

        newWindow.mainloop()

#----------------------------------------------------------------------------------------------------------------------

    #Botão de adicionar produto

    def addProduto2():

        opc_menu = [
            'ADM',
            'FUNC',
        ]

        def FecharJanela():
            newWindow.destroy()

        def resetPesq():
            nome.delete(0, END)
            senha.delete(0, END)


        def VerificarDados():

            codigo10 = "SELECT MAX(id) FROM cadastros"

            cursor.execute(codigo10)

            res = cursor.fetchone()

            cdg = res[0] + 1

            codigo1 = str(cdg)


            nome1 = nome.get()
            senha1 = senha.get()
            menu1 = variable.get()




            if nome1 == '':
                Msg = tk.messagebox.showinfo(title="Alerta", message="Campo do nome está vazio! Formule-o novamente.")
                return addProduto2()

            if senha == '':
                Msg = tk.messagebox.showinfo(title="Alerta", message="Campo do nome está vazio! Formule-o novamente.")
                return addProduto2()



            comando_SQL = "INSERT INTO cadastros(nome,id,senha,cargo) VALUES ('" + nome1 + "', '" + codigo1 + "', '" + senha1 + "', '" + menu1 +"')"


            cursor.execute(comando_SQL)
            banco.commit()

            Msg = tk.messagebox.askquestion(title="Alerta", message="Cadastro realizado com sucesso! Deseja adicionar outro?")

            if Msg == 'yes':
                newWindow.destroy()
                addProduto2()
            else:
                newWindow.destroy()
                return False

    #-----------------------------------------------------------------------------------------------------------------------

        #JANELA PARA ALGUMA FUNÇÃO

        newWindow = tk.Toplevel()

        newWindow.geometry('700x455')
        center(newWindow)
        newWindow.resizable(width=False, height=False)

    #-----------------------------------------------------------------------------------------------------------------------

        txt2 = Label(newWindow, text='Nome:', fg='black', font='poppins 15')
        txt2.place(x=40, y=50)

        nome = Entry(newWindow, background='#c1c1c3', fg='black', font='poppins 20 bold')
        nome.place(x=40, y=90, width=290)

    #-----------------------------------------------------------------------------------------------------------------------

        txt4 = Label(newWindow, text='Senha:', fg='black', font='poppins 15')
        txt4.place(x=40, y=150)

        senha = Entry(newWindow, background='#c1c1c3', fg='black', font='poppins 20 bold')
        senha.place(x=40, y=190, width=290)

    #-----------------------------------------------------------------------------------------------------------------------

        btnEnviar = Button(newWindow, text='Enviar', background='#252525', fg='white', font='poppins 25', command=VerificarDados, borderwidth=0, cursor='tcross')
        btnEnviar.place(x=490, y=330, width=190)

        btnFechar = Button(newWindow, text='╳', background='#252525', fg='white', font='poppins 25', command=FecharJanela, borderwidth=0, cursor='tcross')
        btnFechar.place(x=490, y=22, width=190)

        btnReset = Button(newWindow, text='↺', background='#252525', fg='white', font='poppins 13 bold', command=resetPesq, borderwidth=0, cursor='tcross')
        btnReset.place(x=620, y=260, width=57)

        variable = tk.StringVar(newWindow)
        variable.set(opc_menu[0])

        opt = tk.OptionMenu(newWindow, variable, *opc_menu)
        opt.config(width=90, font='poppins 14', background='#252525', foreground='white', borderwidth=3)
        opt.place(x=40, y=300, width=100)


    #-----------------------------------------------------------------------------------------------------------------------

        atualiza()

        newWindow.mainloop()

#----------------------------------------------------------------------------------------------------------------------

    #Botão de adicionar produto

    def addProduto():

        opc_menu = [
            'Outros',
            'Padaria',
            'Alimentos (cereais e grãos)',
            'Congelados e frios',
            'Hortifruti',
            'Produtos de limpeza',
            'Higiene pessoal',
            'Bebidas',
            'Papelaria'
        ]

        def FecharJanela():
            newWindow.destroy()

        def resetPesq():
            nome.delete(0, END)
            custo.delete(0, END)
            estoque.delete(0, END)
            estoque.delete(0, END)


        def VerificarDados():

            codigo10 = "SELECT MAX(codigo) FROM produtos"

            cursor.execute(codigo10)

            res = cursor.fetchone()

            cdg = res[0] + 1

            codigo1 = str(cdg)


            nome1 = nome.get()
            preco = custo.get()
            estoque1 = estoque.get()
            menu1 = variable.get()



            if nome1 == '':
                Msg = tk.messagebox.showinfo(title="Alerta", message="Campo do nome está vazio! Formule-o novamente.")
                return addProduto()

            if preco == '':
                Msg = tk.messagebox.showinfo(title="Alerta", message="Campo do nome está vazio! Formule-o novamente.")
                return addProduto()

            if estoque1 == '':
                Msg = tk.messagebox.showinfo(title="Alerta", message="Campo do nome está vazio! Formule-o novamente.")
                return addProduto()


            comando_SQL = "INSERT INTO produtos(nome,codigo,preco,estoque,tipo) VALUES ('" + nome1 + "', '" + codigo1 + "', '" + preco + "', '" + estoque1 + "', '" + menu1 + "')"


            cursor.execute(comando_SQL)
            banco.commit()

            Msg = tk.messagebox.askquestion(title="Alerta",
                                            message="Enviado com sucesso! Deseja adicionar mais um produto?")

            if Msg == 'yes':
                newWindow.destroy()
                addProduto()
            else:
                newWindow.destroy()
                return False

    #-----------------------------------------------------------------------------------------------------------------------

        #JANELA PARA ALGUMA FUNÇÃO

        newWindow = tk.Toplevel()

        newWindow.geometry('700x455')
        center(newWindow)
        newWindow.resizable(width=False, height=False)

    #-----------------------------------------------------------------------------------------------------------------------

        txt2 = Label(newWindow, text='Nome do item:', fg='black', font='poppins 15')
        txt2.place(x=40, y=50)

        nome = Entry(newWindow, background='#c1c1c3', fg='black', font='poppins 20 bold')
        nome.place(x=40, y=90, width=290)

    #-----------------------------------------------------------------------------------------------------------------------

        txt4 = Label(newWindow, text='Preço do item:', fg='black', font='poppins 15')
        txt4.place(x=40, y=150)

        custo = Entry(newWindow, background='#c1c1c3', fg='black', font='poppins 20 bold')
        custo.place(x=40, y=190, width=290)

    #-----------------------------------------------------------------------------------------------------------------------

        txt5 = Label(newWindow, text='Estoque do item:', fg='black', font='poppins 15')
        txt5.place(x=40, y=250)

        estoque = Entry(newWindow, validate="key", background='#c1c1c3', fg='black', font='poppins 20 bold')
        estoque['validatecommand'] = (estoque.register(testVal),'%P','%d')
        estoque.place(x=40, y=290, width=290)

    #-----------------------------------------------------------------------------------------------------------------------

        btnEnviar = Button(newWindow, text='Enviar', background='#252525', fg='white', font='poppins 25', command=VerificarDados, borderwidth=0, cursor='tcross')
        btnEnviar.place(x=490, y=330, width=190)

        btnFechar = Button(newWindow, text='╳', background='#252525', fg='white', font='poppins 25', command=FecharJanela, borderwidth=0, cursor='tcross')
        btnFechar.place(x=490, y=22, width=190)

        btnReset = Button(newWindow, text='↺', background='#252525', fg='white', font='poppins 13 bold', command=resetPesq, borderwidth=0, cursor='tcross')
        btnReset.place(x=620, y=260, width=57)

        variable = tk.StringVar(newWindow)
        variable.set(opc_menu[0])

        opt = tk.OptionMenu(newWindow, variable, *opc_menu)
        opt.config(width=90, font='poppins 14', background='#252525', foreground='white', borderwidth=3)
        opt.place(x=40, y=377, width=400)

    #-----------------------------------------------------------------------------------------------------------------------

        atualiza()

        newWindow.mainloop()

#----------------------------------------------------------------------------------------------------------------------

    #Centralizando janela

    def center(win):
        win.update_idletasks()

        width = win.winfo_width()
        frm_width = win.winfo_rootx() - win.winfo_x()
        win_width = width + 2 * frm_width

        height = win.winfo_height()
        titlebar_height = win.winfo_rooty() - win.winfo_y()
        win_height = height + titlebar_height + frm_width

        x = win.winfo_screenwidth() // 2 - win_width // 2
        y = win.winfo_screenheight() // 2 - win_height // 2

        win.geometry('{}x{}+{}+{}'.format(width, height, x, y))

        win.deiconify()

#----------------------------------------------------------------------------------------------------------------------

    #Pegando a hora atual

    def time():
        string = strftime('%H:%M:%S %p')
        hora.config(text = string)
        hora.after(1000, time)

#----------------------------------------------------------------------------------------------------------------------

    #Puxando o total de linhas

    def totalLinhas():
        comando_SQL = "SELECT COUNT(codigo) FROM produtos"
        cursor.execute(comando_SQL)

        record = cursor.fetchone()

        outro = Label(bd, text=f"Total de {(record[0] - 1)} Linhas.", background='#c1c1c3', fg='#383837', font='Poppins 24').place(x=1220, y=200, width=396, height=80)

        bd.update()

    def totalLinhas2():
        cursor.execute("SELECT COUNT(id) FROM cadastros")
        r = cursor.fetchone()

        outro = Label(login, text=f"Total de {(r[0] - 1)} Linhas.", background='#c1c1c3', fg='#383837', font='Poppins 24').place(x=1220, y=200, width=396, height=80)

        login.update()

#----------------------------------------------------------------------------------------------------------------------

    root = Tk()


    #Estilização

    root.title('SISTEMA CAIXA E ESTOQUE')
    root.configure(background="#D3D3D3")
    root.geometry('1700x930')
    center(root)
    root.resizable(width=False, height=False)


    tela = ttk.Notebook(root)
    tela.place(x=0, y=0, width=1700, height=930)

    bd = Frame(tela)
    tela.add(bd, text='Banco de dados')


    #Objetos para Estilização

    caixa1 = Label(bd, text='', background='#c1c1c3').place(x=0, y=0, width=1700, height=170)
    titulo = Label(bd, text='SuperMercado Alvorada', background='#c1c1c3', fg='#383837', font='Poppins 44 bold').place(x=-400, y=0, width=1700, height=170)
    titulo = Label(bd, text='Banco de dados', background='#c1c1c3', fg='#383837', font='Poppins 12').place(x=650, y=105)

    titulo_m = Label(bd, text='Tabela do banco de dados', background='#c1c1c3', fg='#383837', font='Poppins 24').place(x=50, y=200, width=1092, height=80)

    NomePessoa = Label(bd, text=f'Olá, {nomeAA}', background='#c1c1c3', fg='#383837', font='Poppins 12').place(x=80, y=125)

    hora = Label(bd, background='#c1c1c3', fg='#383837', font='Arial 50 normal')
    hora.place(x=1245, y=0, height=170)
    time()

#----------------------------------------------------------------------------------------------------------------------

    compra = Frame(tela)
    tela.add(compra, text='Realizar Compra')

    def TelaCompra():

        def preco():
            banco = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="infoCaixa"
            )

            cursor = banco.cursor()

            codigo0 = codigo20.get()

            comando = "SELECT preco FROM produtos WHERE codigo = '" + codigo0 + "'"
            cursor.execute(comando)

            i2 = cursor.fetchone()


        def remove_all():
            for record in n.get_children():
                try:
                    n.delete(record)
                    atualizarJanela()
                except:
                    tk.messagebox.showinfo(title="Alerta", message="Não há linhas na tabela para deletar!")



        def selecionado():
            try:
                x = n.selection()[0]
                n.delete(x)
            except:
                tk.messagebox.showinfo(title="Alerta", message="Selecione uma linha da tabela, e, tente novamente!")


        def generar():

            total = 0.0

            for child in n.get_children():
                total += float(n.item(child, 'values')[4])

            painel['text'] = f'R$ {"%.2f" % (total)}'



        def details():

            def funcEnviar():
                codigo0 = codigo20.get()
                unidades0 = unidades.get()

                if codigo0 == '':
                    Msg = tk.messagebox.showinfo(title="Alerta", message="Campo do código está vazio! Formule-o novamente.")
                    return False

                if unidades0 == '':
                    Msg = tk.messagebox.showinfo(title="Alerta", message="Campo da quantidade está vazio! Formule-o novamente.")
                    return False

                elif unidades0 == '0':
                    Msg = tk.messagebox.showinfo(title="Alerta",message="Campo da quantidade não pode ser 0! Formule-o novamente.")
                    return False


                comando_SQL = "SELECT * FROM produtos WHERE codigo = '" + codigo0 + "'"
                cursor.execute(comando_SQL)
                records = cursor.fetchall()

                comando_SQL2 = "SELECT estoque FROM produtos WHERE codigo = '" + codigo0 + "'"
                cursor.execute(comando_SQL2)
                retorno = cursor.fetchone()

                estoque10 = (retorno[0] - float(unidades0))

                estoque1 = ("%.0f" % (estoque10))

                #comando_SQL3 = "UPDATE produtos SET estoque = '" + estoque1 + "' WHERE " -------------------------------------------------------------------------------------------------------------
                #comando_SQL3 = "UPDATE produtos SET estoque = '" + estoque1 + "' WHERE " -------------------------------------------------------------------------------------------------------------
                #comando_SQL3 = "UPDATE produtos SET estoque = '" + estoque1 + "' WHERE " -------------------------------------------------------------------------------------------------------------


                for i in records:
                    valorTotal0 = (i[2] * float(unidades0))


                for i in records:
                    n.insert("", "end", values=(i[1], i[0], i[2], unidades0, ("%.2f" % (valorTotal0))))


                for record in n.get_children():
                    valores = n.item(record, "values")
                    #print(valores[4])


                outro2 = Label(compra, text=f"Total de {(len(n.get_children()))} itens.", background='#c1c1c3', fg='#383837', font='Poppins 24').place(x=1220, y=200, width=396, height=80)


                codigo20.delete(0, END)
                unidades.delete(0, END)

                generar()
                n.update()
                compra.update()
                preco()


            funcEnviar()


        def enviar():
            res = (len(n.get_children()))
            if res == 0:
                Msgg = tk.messagebox.showinfo(title="Alerta", message="Você deve adicionar pelo menos 1 produto!")
                return False
            else:
                aaa = tk.messagebox.askquestion(title='Alerta', message='Você deseja finalizar a compra?')

                if aaa == 'yes':
                    enviar2()
                else:
                    return False


        def enviar2():

            def limitar_tamanho(p):
                if len(p) > 11:
                    return False
                return True

            def FecharJanela():
                newWindow.destroy()

            def resetPesq():
                nomeCliente.delete(0, END)
                cpfCliente.delete(0, END)

            string = strftime('%d/%m/%Y')
            hora.config(text=string)

            def VerificarDados():

                nome = nomeCliente.get()
                cpf = cpfCliente.get()

                if nome == '':
                    Msgg = tk.messagebox.showinfo(title="Alerta", message="Campo do nome está vazio! Formule-o novamente.")
                    return enviar()

                if cpf == '':
                    Msge = tk.messagebox.showinfo(title="Alerta", message="Campo do CPF está vazio! Formule-o novamente.")
                    return enviar()


                for record in n.get_children():
                    try:
                        n.delete(record)
                        atualizarJanela()
                    except:
                        tk.messagebox.showinfo(title="Alerta", message="Você não adicionou nenhum produto!")



                id = "SELECT MAX(idCompra) FROM vendas"

                cursor.execute(id)

                res = cursor.fetchone()

                cdg = res[0] + 1

                idCompra = str(cdg)


                comando_SQL = "INSERT INTO vendas (nome,cpf,idCompra,dataVenda) VALUES ('" + nome + "', '" + cpf + "', '" + str(idCompra) + "', '" + str(string) + "')"

                cursor.execute(comando_SQL)

                banco.commit()

                newWindow.destroy()




            newWindow = tk.Toplevel()

            vcmd = newWindow.register(func=limitar_tamanho)
            newWindow.geometry('700x455')
            center(newWindow)
            newWindow.resizable(width=False, height=False)
            newWindow.configure(background='#404040')
            NomePessoa = Label(newWindow, text=f'Olá, {nomeAA}', background='#c1c1c3', fg='#383837', font='Poppins 12').place(x=80, y=125)



            #---[ PARTE DA ESTILIZAÇÃO ]--------------------------------------------------------------------------------------------------------------------------------

            l1 = Label(newWindow, text='Finalizando', background='#151515', fg='white', font='poppins 25').place(x=30, y=22, width=400, height=98)

            l2 = Label(newWindow, text='', background='#151515', fg='white', font='poppins 25').place(x=30, y=160, width=400, height=270)

            #-----------------------------------------------------------------------------------------------------------------------------------------------------------

            # --|
            # --|
            # --|

            #---[ PARTE DOS CAMPOS DE ENTRADA DE DADOS ]----------------------------------------------------------------------------------------------------------------

            Label(newWindow, text='Nome:', background='#151515', fg='white', font='poppins 16').place(x=50, y=190)

            nomeCliente = Entry(newWindow, foreground='#151515', background='#c1c2c3', font='Poppins 14', borderwidth=0)
            nomeCliente.place(x=50, y=230, width=360)


            Label(newWindow, text='CPF:', background='#151515', fg='white', font='poppins 16').place(x=50, y=300)

            cpfCliente = Entry(newWindow, foreground='#151515', background='#c1c2c3', font='Poppins 14', borderwidth=0,validate='key', validatecommand=(vcmd, '%P'))
            cpfCliente.place(x=50, y=340, width=360)

            #-----------------------------------------------------------------------------------------------------------------------------------------------------------

            # --|
            # --|
            # --|

            #---[ PARTE DOS BOTÕES COM FUNÇÕES ]------------------------------------------------------------------------------------------------------------------------

            btnEnviar = Button(newWindow, text='Enviar', background='#c1c2c3', fg='black', font='poppins 25', command=VerificarDados, borderwidth=0, cursor='tcross')
            btnEnviar.place(x=490, y=330, width=190)

            btnFechar = Button(newWindow, text='╳', background='#c1c2c3', fg='black', font='poppins 25 bold', command=FecharJanela, borderwidth=0, cursor='tcross')
            btnFechar.place(x=490, y=22, width=190)

            btnReset = Button(newWindow, text='↺', background='#c1c2c3', fg='black', font='poppins 13 bold', command=resetPesq, borderwidth=0, cursor='tcross')
            btnReset.place(x=620, y=260, width=57)

            #-----------------------------------------------------------------------------------------------------------------------------------------------------------



        def atualizarJanela():
            outro2 = Label(compra, text=f"Total de {(len(n.get_children()))} itens.", background='#c1c1c3', fg='#383837', font='Poppins 24').place(x=1220, y=200, width=396, height=80)
            compra.update()
            generar()


        def editarLinha():
            codigo20.delete(0, END)
            unidades.delete(0, END)

            selecionado1 = n.focus()

            values = n.item(selecionado1, 'values')

            codigo20.insert(0, values[0])
            unidades.insert(0, values[3])


        def salvarEdicao():

            selecionado1 = n.focus()

            n.item(selecionado1, text="", values=selecionado1[3])

            codigo20.delete(0, END)
            unidades.delete(0, END)


        #Objetos para Estilização

        caixa1compra = Label(compra, text='', background='#c1c1c3').place(x=0, y=0, width=1700, height=170)
        titulocompra = Label(compra, text='SuperMercado Alvorada', background='#c1c1c3', fg='#383837', font='Poppins 44 bold').place(x=-400, y=0, width=1700, height=170)
        titulocompra = Label(compra, text='Compra', background='#c1c1c3', fg='#383837', font='Poppins 12').place(x=750, y=105)

        NomePessoa = Label(compra, text=f'Olá, {nomeAA}', background='#c1c1c3', fg='#383837', font='Poppins 12').place(x=80, y=125)

        titulo_mcompra = Label(compra, text='Painel com items da compra', background='#c1c1c3', fg='#383837', font='Poppins 24').place(x=50, y=200, width=1092, height=80)



        outro22 = Label(compra, text='Total de 0 itens.', background='#c1c1c3', fg='#383837',font='Poppins 24').place(x=1220, y=200, width=396, height=80)

        painel = Label(compra, text='R$ 00.00', background='#c1c1c3', fg='#383837', font='Poppins 62', borderwidth=0)
        painel.place(x=1220, y=260, width=396, height=130)

        add2 = Button(compra, text="Remover Produto", command=selecionado, font='Poppins 14 normal', background='#252525', fg='white', borderwidth=0)
        add2.place(x=1230, y=420, width=180)

        add3 = Button(compra, text="Remover Todos", command=remove_all, font='Poppins 14 normal', background='#252525', fg='white', borderwidth=0)
        add3.place(x=1427, y=420, width=180)

        add6 = Button(compra, text="Salvar Edição", command=salvarEdicao, font='Poppins 11 normal', background='#252525', fg='white', borderwidth=0)
        add6.place(x=1360, y=490, width=128)

        add4 = Button(compra, text="Editar Produto", command=editarLinha, font='Poppins 11 normal', background='#252525', fg='white', borderwidth=0)
        add4.place(x=1218, y=490, width=128)

        add5 = Button(compra, text="Atualizar", command=atualizarJanela, font='Poppins 11 normal', background='#252525', fg='white', borderwidth=0)
        add5.place(x=1500, y=490, width=128)


        n = ttk.Treeview(compra, columns=('id', 'Nome', 'valorItem', 'qtdProdutos', 'valorTotal'), show='headings')

        style = ttk.Style()
        style.configure("Treeview", font='Poppins 15', rowheight=35)
        style.configure("Treeview.Heading", font='Poppins 15')

        n.tag_configure('oddrow', background="white")
        n.tag_configure('evenrow', background="lightblue")

        n.column('id', minwidth=0, width=70, anchor=CENTER)
        n.column('Nome', minwidth=0, width=300)
        n.column('valorItem', minwidth=0, width=100, anchor=CENTER)
        n.column('qtdProdutos', minwidth=0, width=100, anchor=CENTER)
        n.column('valorTotal', minwidth=0, width=130, anchor=CENTER)

        n.heading('id', text='ID', anchor=CENTER)
        n.heading('Nome', text='Nome',)
        n.heading('valorItem', text='Valor Item', anchor=CENTER)
        n.heading('qtdProdutos', text='Quantidade', anchor=CENTER)
        n.heading('valorTotal', text='Valor Total', anchor=CENTER)

        n.place(x=50, y=273, width=1092, height=600)


        Label(compra, background='#505050').place(x=1218, y=592, width=400, height=280)

        Label(compra, background='#606060', text='Adicionar', font='poppins 17 bold', fg='white').place(x=1230, y=572, width=180)

        txt1 = Label(compra, text='Código do item:', fg='white', background='#505050', font='poppins 16')
        txt1.place(x=1273, y=640)

        codigo20 = Entry(compra, validate="key", fg='black', background='#c1c2c3', font='poppins 20 bold')
        codigo20['validatecommand'] = (codigo20.register(testVal), '%P', '%d')
        codigo20.place(x=1273, y=680, width=290)


        txt2 = Label(compra, text='Quantidade:', fg='white', background='#505050', font='poppins 16')
        txt2.place(x=1273, y=750)

        unidades = Entry(compra, validate="key", fg='black', background='#c1c2c3', font='poppins 20 bold')
        unidades['validatecommand'] = (unidades.register(testVal), '%P', '%d')
        unidades.place(x=1273, y=790, width=190)


        addBtn = Button(compra, text='╋', command=details, fg='black', background='#c1c2c3', font='poppins 20 bold', borderwidth=0)
        addBtn.place(x=1483, y=790, width=80, height=51)


        enviarBtn = Button(compra, text='Finalizar compra', command=enviar, background='#252525', fg='white', font='poppins 20', borderwidth=0, cursor='tcross')
        enviarBtn.place(x=1270, y=45, width=300)

#----------------------------------------------------------------------------------------------------------------------

    login = Frame(tela)
    tela.add(login, text='Cadastros')

    def atualizaCadastro():

        m2 = ttk.Treeview(login, columns=('nome', 'id', 'senha', 'cargo'), show='headings')

        style2 = ttk.Style()
        style2.configure("Treeview", font='Poppins 15', rowheight=35)
        style2.configure("Treeview.Heading", font='Poppins 15')

        m2.column('nome', minwidth=0, width=300)
        m2.column('id', minwidth=0, width=100, anchor=CENTER)
        m2.column('senha', minwidth=0, width=100, anchor=CENTER)
        m2.column('cargo', minwidth=0, width=100, anchor=CENTER)
        m2.heading('nome', text='Nome')
        m2.heading('id', text='ID', anchor=CENTER)
        m2.heading('senha', text='Senha', anchor=CENTER)
        m2.heading('cargo', text='Cargo', anchor=CENTER)
        m2.place(x=50, y=273, width=1092, height=600)

        banco3 = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="infoCaixa"
        )

        cursor3 = banco3.cursor()

        cursor3.execute("SELECT * FROM cadastros ORDER BY id")
        recordes1 = cursor3.fetchall()

        global count2
        count2 = 0

        for record3 in recordes1:
            m2.insert(parent='', index='end', iid=count2, text='', values=(record3[0], record3[1], record3[2], record3[3]))

            count2 += 1


        banco3.commit()

        banco3.close()

        totalLinhas()

#----------------------------------------------------------------------------------------------------------------------

    atualizaCadastro()

#----------------------------------------------------------------------------------------------------------------------

    #Objetos para Estilização


    caixa1 = Label(login, text='', background='#c1c1c3').place(x=0, y=0, width=1700, height=170)

    titulo = Label(login, text='SuperMercado Alvorada', background='#c1c1c3', fg='#383837', font='Poppins 44 bold').place(x=-400, y=0, width=1700, height=170)

    titulo_m = Label(login, text='Usuarios Cadastrados', background='#c1c1c3', fg='#383837', font='Poppins 24').place(x=50, y=200, width=1092, height=80)

    NomePessoa = Label(login, text=f'Olá, {nomeAA}', background='#c1c1c3', fg='#383837', font='Poppins 12').place(x=80, y=125)

    hora = Label(login, background='#c1c1c3', fg='#383837', font='Arial 50 normal')
    hora.place(x=1245, y=0, height=170)
    time()

    caixa1 = Label(login, text='', background='#c1c1c3').place(x=1220, y=303, width=400, height=470)

    bt1 = Button(login, text="Adicionar Cadastro", command=addProduto2, font='Poppins 18 normal', background='#252525', fg='white', borderwidth=0, cursor='tcross')
    bt1.place(x=1270, y=353, width=300)

    bt2 = Button(login, text="Remover Cadastro", command=removerCadastro, font='Poppins 18 normal', background='#252525', fg='white', borderwidth=0, cursor='tcross')
    bt2.place(x=1270, y=453, width=300)

    bt3 = Button(login, text="Pesquisar Cadastro", command=pesqCadastro, font='Poppins 18 normal', background='#252525', fg='white', borderwidth=0, cursor='tcross')
    bt3.place(x=1270, y=553, width=300)

    bt4 = Button(login, text="Atualizar Cadastro", command=atualizaCadastro, font='Poppins 18 normal', background='#252525', fg='white', borderwidth=0, cursor='tcross')
    bt4.place(x=1270, y=653, width=300)

#----------------------------------------------------------------------------------------------------------------------

    def atualiza():

        m.destroy()

        m2 = ttk.Treeview(bd, columns=('Nome', 'Codigo', 'Preco', 'Estoque', 'Tipo'), show='headings')

        style2 = ttk.Style()
        style2.configure("Treeview", font='Poppins 15', rowheight=35)
        style2.configure("Treeview.Heading", font='Poppins 15')

        m2.column('Nome', minwidth=0, width=300)
        m2.column('Codigo', minwidth=0, width=100, anchor=CENTER)
        m2.column('Preco', minwidth=0, width=100, anchor=CENTER)
        m2.column('Estoque', minwidth=0, width=100, anchor=CENTER)
        m2.column('Tipo', minwidth=0, width=230)
        m2.heading('Nome', text='Nome')
        m2.heading('Codigo', text='Código', anchor=CENTER)
        m2.heading('Preco', text='Preço', anchor=CENTER)
        m2.heading('Estoque', text='Estoque', anchor=CENTER)
        m2.heading('Tipo', text='Tipo')
        m2.place(x=50, y=273, width=1092, height=600)

        banco3 = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="infoCaixa"
        )

        cursor3 = banco3.cursor()

        cursor3.execute("SELECT * FROM produtos ORDER BY codigo")
        recordes1 = cursor3.fetchall()

        global count2
        count2 = 0

        for record3 in recordes1:
            m2.insert(parent='', index='end', iid=count2, text='', values=(record3[0], record3[1], ("R$", record3[2]), record3[3], record3[4]))

            count2 += 1


        banco3.commit()

        banco3.close()

        totalLinhas()

#----------------------------------------------------------------------------------------------------------------------

    m = ttk.Treeview(bd, columns=('Nome', 'Codigo', 'Preco', 'Estoque', 'Tipo'), show='headings')

    style = ttk.Style()
    style.configure("Treeview", font='Poppins 15', rowheight=35)
    style.configure("Treeview.Heading", font='Poppins 15')

    m.column('Nome', minwidth=0, width=300)
    m.column('Codigo', minwidth=0, width=100, anchor=CENTER)
    m.column('Preco', minwidth=0, width=100, anchor=CENTER)
    m.column('Estoque', minwidth=0, width=100, anchor=CENTER)
    m.column('Tipo', minwidth=0, width=230)
    m.heading('Nome', text='Nome')
    m.heading('Codigo', text='Código', anchor=CENTER)
    m.heading('Preco', text='Preço', anchor=CENTER)
    m.heading('Estoque', text='Estoque', anchor=CENTER)
    m.heading('Tipo', text='Tipo')
    m.place(x=50, y=273, width=1092, height=600)

#----------------------------------------------------------------------------------------------------------------------

    def query_database():

        banco2 = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="infoCaixa"
        )

        cursor2 = banco2.cursor()

        cursor2.execute("SELECT * FROM produtos ORDER BY codigo")
        recordes = cursor2.fetchall()

        global count
        count = 0

        for record2 in recordes:
            m.insert(parent='', index='end', iid=count, text='', values=(record2[0], record2[1], ("R$", record2[2]), record2[3], record2[4]))

            count += 1


        banco2.commit()

        banco2.close()

#----------------------------------------------------------------------------------------------------------------------

    query_database()

#----------------------------------------------------------------------------------------------------------------------

    caixa1 = Label(bd, text='', background='#c1c1c3').place(x=1220, y=303, width=400, height=570)

    add = Button(bd, text="Adicionar Produto", command=addProduto, font='Poppins 18 normal', background='#252525', fg='white', borderwidth=0, cursor='tcross')
    add.place(x=1270, y=353, width=300)

    add2 = Button(bd, text="Remover Produto", command=removerProduto, font='Poppins 18 normal', background='#252525', fg='white', borderwidth=0, cursor='tcross')
    add2.place(x=1270, y=453, width=300)

    add3 = Button(bd, text="Pesquisar Produto", command=pesqProduto, font='Poppins 18 normal', background='#252525', fg='white', borderwidth=0, cursor='tcross')
    add3.place(x=1270, y=553, width=300)

    add4 = Button(bd, text="Atualizar Produtos", command=atualiza, font='Poppins 18 normal', background='#252525', fg='white', borderwidth=0, cursor='tcross')
    add4.place(x=1270, y=653, width=300)

    add5 = Button(bd, text="Editar Produto", command=editarProduto, font='Poppins 18 normal', background='#252525', fg='white', borderwidth=0, cursor='tcross')
    add5.place(x=1270, y=753, width=300)

    totalLinhas()

    totalLinhas2()

    TelaCompra()

    root.mainloop()

#----------------------------------------------------------------------------------------------------------------------










def app2():


#-----------------------------------------------------------------------------------------------------------------------

    #CONEXÃO COM BANCO DE DADOS

    banco = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="infoCaixa"
    )

    cursor = banco.cursor()

#-----------------------------------------------------------------------------------------------------------------------

    #Função para tornar Entry apenas numeros

    def testVal(inStr,acttyp):
        if acttyp == '1': #insert
            if not inStr.isdigit():
                return False
        return True

#-----------------------------------------------------------------------------------------------------------------------

    #Botão de editar

    def editarProduto():

        opc_menu = [
            'Outros',
            'Padaria',
            'Alimentos (cereais e grãos)',
            'Congelados e frios',
            'Hortifruti',
            'Produtos de limpeza',
            'Higiene pessoal',
            'Bebidas',
            'Papelaria'
        ]

        def FecharJanela():
            newWindow2.destroy()

        def resetPesq():
            newWindow2.destroy()
            editarProduto()

        def my_details():
            codigo1 = codigo.get()

            if codigo1 == '':
                Msg = tk.messagebox.showinfo(title="Alerta", message="Campo do nome está vazio! Formule-o novamente.")
                return addProduto()

            comando_SQL = "SELECT * from produtos WHERE codigo LIKE '%"+codigo1+"%'"
            cursor.execute(comando_SQL)
            records = cursor.fetchall()

            for i in records:
                m.insert("", "end", values=i)

        def select_item():
            name_box.delete(0, END)
            codigo_box.delete(0, END)
            preco_box.delete(0, END)
            estoque_box.delete(0, END)

            selected = m.focus()
            values = m.item(selected, 'values')

            name_box.insert(0, values[0])
            codigo_box.insert(0, values[1])
            preco_box.insert(0, values[2])
            estoque_box.insert(0, values[3])

        def update_item():
            selected = m.focus()

            m.item(selected, text='', values=(name_box.get(), codigo_box.get(), preco_box.get(), estoque_box.get(), variable.get()))

            sql_add = "UPDATE produtos SET nome = %s, codigo = %s, preco = %s, estoque = %s, tipo = %s WHERE codigo = %s"
            val = (f"{name_box.get()}", f"{codigo_box.get()}", f"{preco_box.get()}", f"{estoque_box.get()}", f"{variable.get()}", f"{codigo_box.get()}")

            cursor.execute(sql_add, val)
            banco.commit()


    #-----------------------------------------------------------------------------------------------------------------------

        #JANELA PARA ALGUMA FUNÇÃO

        newWindow2 = tk.Toplevel()

        newWindow2.geometry('800x455')
        center(newWindow2)
        newWindow2.resizable(width=False, height=False)

    #-----------------------------------------------------------------------------------------------------------------------

        txt1 = Label(newWindow2, text='Código do item:', fg='black', font='poppins 16')
        txt1.place(x=40, y=50)

        codigo = Entry(newWindow2, validate="key", background='#c1c1c3', fg='black', font='poppins 20 bold')
        codigo['validatecommand'] = (codigo.register(testVal),'%P','%d')
        codigo.place(x=40, y=100, width=290)

    #-----------------------------------------------------------------------------------------------------------------------

        btnFechar = Button(newWindow2, text='╳', background='#252525', fg='white', font='poppins 25', command=FecharJanela, borderwidth=0, cursor='tcross')
        btnFechar.place(x=590, y=22, width=190)

        btnPesq = Button(newWindow2, text='🔍', background='#252525', fg='white', font='poppins 13', command=my_details, borderwidth=0, cursor='tcross')
        btnPesq.place(x=340, y=99, width=60)

        btnReset = Button(newWindow2, text='↺', background='#252525', fg='white', font='poppins 13 bold', command=resetPesq, borderwidth=0, cursor='tcross')
        btnReset.place(x=720, y=380, width=60)

        comando_SQL = "SELECT * from produtos"
        cursor.execute(comando_SQL)
        records = cursor.fetchall()



        name_box = Entry(newWindow2, background='gray', fg='white', font='poppins 13 normal')
        name_box.place(x=40, y=300, width=200)

        codigo_box = Entry(newWindow2, background='gray', fg='white', font='poppins 13 normal')

        preco_box = Entry(newWindow2, background='gray', fg='white', font='poppins 13 normal')
        preco_box.place(x=245, y=300, width=100)

        estoque_box = Entry(newWindow2, background='gray', fg='white', font='poppins 13 normal')
        estoque_box.place(x=350, y=300, width=100)

        variable = tk.StringVar(newWindow2)
        variable.set(opc_menu[0])

        opt = tk.OptionMenu(newWindow2, variable, *opc_menu)
        opt.config(width=90, font='poppins 14', background='gray', foreground='white', borderwidth=3)
        opt.place(x=452, y=297, width=333, height=39)




        select_button = Button(newWindow2, text='Selecione o item', background='#252525', fg='white', font='poppins 13 normal', command=select_item, borderwidth=0, cursor='tcross')
        select_button.place(x=40, y=370)

        update_button = Button(newWindow2, text='Salve a alteração', background='#252525', fg='white', font='poppins 13 normal',  command=update_item, borderwidth=0, cursor='tcross')
        update_button.place(x=220, y=370)



        m = ttk.Treeview(newWindow2, columns=('Nome', 'Codigo', 'Preco', 'Estoque', 'Tipo'), show='headings')

        style = ttk.Style()
        style.configure("Treeview", font='Poppins 15', rowheight=35)
        style.configure("Treeview.Heading", font='Poppins 15')

        m.column('Nome', minwidth=0, width=250)
        m.column('Codigo', minwidth=0, width=100)
        m.column('Preco', minwidth=0, width=100)
        m.column('Estoque', minwidth=0, width=100)
        m.column('Tipo', minwidth=0, width=190)
        m.heading('Nome', text='Nome')
        m.heading('Codigo', text='Código')
        m.heading('Preco', text='Preço')
        m.heading('Estoque', text='Estoque')
        m.heading('Tipo', text='Tipo')
        m.place(x=40, y=180, height=80)


    #-----------------------------------------------------------------------------------------------------------------------

        atualiza()

        newWindow2.mainloop()

#-----------------------------------------------------------------------------------------------------------------------

    #Botão de adicionar produto

    def pesqCadastro():

        def FecharJanela():
            newWindow.destroy()

        def resetPesq():
            id.delete(0, END)

        def my_details():
            id1 = id.get()

            if id1 == '':
                Msg = tk.messagebox.showinfo(title="Alerta", message="Campo do ID está vazio! Formule-o novamente.")
                return addProduto()

            comando_SQL = "SELECT * from cadastros WHERE id LIKE '%"+id1+"%'"
            cursor.execute(comando_SQL)
            records = cursor.fetchall()

            for i in records:
                m.insert("", "end", values=i)


    #-----------------------------------------------------------------------------------------------------------------------

        #JANELA PARA ALGUMA FUNÇÃO

        newWindow = tk.Toplevel()

        newWindow.geometry('700x455')
        center(newWindow)
        newWindow.resizable(width=False, height=False)


    #-----------------------------------------------------------------------------------------------------------------------

        txt1 = Label(newWindow, text='ID do item:', fg='black', font='poppins 16')
        txt1.place(x=40, y=50)

        id = Entry(newWindow, validate="key", background='#c1c1c3', fg='black', font='poppins 20 bold')
        id['validatecommand'] = (id.register(testVal),'%P','%d')
        id.place(x=40, y=100, width=290)

    #-----------------------------------------------------------------------------------------------------------------------

        btnFechar = Button(newWindow, text='╳', background='#252525', fg='white', font='poppins 25', command=FecharJanela, borderwidth=0, cursor='tcross')
        btnFechar.place(x=490, y=22, width=190)

        btnPesq = Button(newWindow, text='🔍', background='#252525', fg='white', font='poppins 13', command=my_details, borderwidth=0, cursor='tcross')
        btnPesq.place(x=340, y=99, width=60)

        btnReset = Button(newWindow, text='↺', background='#252525', fg='white', font='poppins 13 bold', command=resetPesq, borderwidth=0, cursor='tcross')
        btnReset.place(x=620, y=380, width=60)

        m = ttk.Treeview(newWindow, columns=('Nome', 'id', 'senha'), show='headings')

        style = ttk.Style()
        style.configure("Treeview", font='Poppins 15', rowheight=35)
        style.configure("Treeview.Heading", font='Poppins 15')

        m.column('Nome', minwidth=0, width=250)
        m.column('id', minwidth=0, width=100)
        m.column('senha', minwidth=0, width=100)
        m.heading('Nome', text='Nome')
        m.heading('id', text='ID')
        m.heading('senha', text='Senha')
        m.place(x=40, y=180, height=80)

    #-----------------------------------------------------------------------------------------------------------------------

        atualiza()

        newWindow.mainloop()

#-----------------------------------------------------------------------------------------------------------------------

    #Botão de adicionar produto

    def pesqProduto():

        def FecharJanela():
            newWindow.destroy()

        def resetPesq():
            codigo.delete(0, END)

        def my_details():
            codigo1 = codigo.get()

            if codigo1 == '':
                Msg = tk.messagebox.showinfo(title="Alerta", message="Campo do nome está vazio! Formule-o novamente.")
                return addProduto()

            comando_SQL = "SELECT * from produtos WHERE codigo LIKE '%"+codigo1+"%'"
            cursor.execute(comando_SQL)
            records = cursor.fetchall()

            for i in records:
                m.insert("", "end", values=i)


    #-----------------------------------------------------------------------------------------------------------------------

        #JANELA PARA ALGUMA FUNÇÃO

        newWindow = tk.Toplevel()

        newWindow.geometry('700x455')
        center(newWindow)
        newWindow.resizable(width=False, height=False)

    #-----------------------------------------------------------------------------------------------------------------------

        txt1 = Label(newWindow, text='Código do item:', fg='black', font='poppins 16')
        txt1.place(x=40, y=50)

        codigo = Entry(newWindow, validate="key", background='#c1c1c3', fg='black', font='poppins 20 bold')
        codigo['validatecommand'] = (codigo.register(testVal),'%P','%d')
        codigo.place(x=40, y=100, width=290)

    #-----------------------------------------------------------------------------------------------------------------------

        btnFechar = Button(newWindow, text='╳', background='#252525', fg='white', font='poppins 25', command=FecharJanela, borderwidth=0, cursor='tcross')
        btnFechar.place(x=490, y=22, width=190)

        btnPesq = Button(newWindow, text='🔍', background='#252525', fg='white', font='poppins 13', command=my_details, borderwidth=0, cursor='tcross')
        btnPesq.place(x=340, y=99, width=60)

        btnReset = Button(newWindow, text='↺', background='#252525', fg='white', font='poppins 13 bold', command=resetPesq, borderwidth=0, cursor='tcross')
        btnReset.place(x=620, y=380, width=60)

        m = ttk.Treeview(newWindow, columns=('Nome', 'Codigo', 'Preco', 'Estoque'), show='headings')

        style = ttk.Style()
        style.configure("Treeview", font='Poppins 15', rowheight=35)
        style.configure("Treeview.Heading", font='Poppins 15')

        m.column('Nome', minwidth=0, width=250)
        m.column('Codigo', minwidth=0, width=100)
        m.column('Preco', minwidth=0, width=100)
        m.column('Estoque', minwidth=0, width=100)
        m.heading('Nome', text='Nome')
        m.heading('Codigo', text='Código')
        m.heading('Preco', text='Preço')
        m.heading('Estoque', text='Estoque')
        m.place(x=40, y=180, height=80)

    #-----------------------------------------------------------------------------------------------------------------------

        atualiza()

        newWindow.mainloop()

#-----------------------------------------------------------------------------------------------------------------------

    #Botão de adicionar produto

    def removerCadastro():

        def FecharJanela():
            newWindow.destroy()

        def resetPesq():
            id.delete(0, END)

        def confirmarRem():

            if id.get() == "":
                tk.messagebox.showinfo(title="Alerta", message="Insira algo no campo de remoção!")
                return False

            else:
                id1 = id.get()

                if id1 == '':
                    Msg = tk.messagebox.showinfo(title="Alerta", message="Campo do id está vazio! Formule-o novamente.")
                    return addProduto()

                comando_SQL = "DELETE FROM cadastros WHERE id = "+ id1 +""

                cursor.execute(comando_SQL)
                banco.commit()

                Msg = tk.messagebox.askquestion(title="Alerta", message="Removido com sucesso! Deseja remover mais um cadastro?")

                if Msg == 'yes':
                    removerCadastro()
                else:
                    return False

    #-----------------------------------------------------------------------------------------------------------------------

        #JANELA PARA ALGUMA FUNÇÃO

        newWindow = tk.Toplevel()

        newWindow.geometry('700x455')
        center(newWindow)
        newWindow.resizable(width=False, height=False)

    #-----------------------------------------------------------------------------------------------------------------------

        txt1 = Label(newWindow, text='ID do item:', fg='black', font='poppins 16')
        txt1.place(x=40, y=160)

        id = Entry(newWindow, validate="key", background='#c1c1c3', fg='black', font='poppins 20 bold')
        id['validatecommand'] = (id.register(testVal),'%P','%d')
        id.place(x=40, y=210, width=290)

    #-----------------------------------------------------------------------------------------------------------------------

        btnRem = Button(newWindow, text='Remover', background='#252525', fg='white', font='poppins 25', command=confirmarRem, borderwidth=0, cursor='tcross')
        btnRem.place(x=490, y=330, width=190)

        btnFechar = Button(newWindow, text='╳', background='#252525', fg='white', font='poppins 25', command=FecharJanela, borderwidth=0, cursor='tcross')
        btnFechar.place(x=490, y=22, width=190)

        btnReset = Button(newWindow, text='↺', background='#252525', fg='white', font='poppins 13 bold', command=resetPesq, borderwidth=0, cursor='tcross')
        btnReset.place(x=620, y=260, width=57)

    #-----------------------------------------------------------------------------------------------------------------------

        atualiza()

        newWindow.mainloop()

#-----------------------------------------------------------------------------------------------------------------------

    #Botão de adicionar produto

    def removerProduto():

        def FecharJanela():
            newWindow.destroy()

        def resetPesq():
            codigo.delete(0, END)

        def confirmarRem():

            if codigo.get() == "":
                tk.messagebox.showinfo(title="Alerta", message="Insira algo no campo de remoção!")
                return False

            else:
                codigo1 = codigo.get()

                if codigo1 == '':
                    Msg = tk.messagebox.showinfo(title="Alerta", message="Campo do nome está vazio! Formule-o novamente.")
                    return addProduto()

                comando_SQL = "DELETE FROM produtos WHERE codigo = "+ codigo1 +""

                cursor.execute(comando_SQL)
                banco.commit()

                Msg = tk.messagebox.askquestion(title="Alerta", message="Removido com sucesso! Deseja remover mais um produto?")

                if Msg == 'yes':
                    removerProduto()
                else:
                    return False

    #-----------------------------------------------------------------------------------------------------------------------

        #JANELA PARA ALGUMA FUNÇÃO

        newWindow = tk.Toplevel()

        newWindow.geometry('700x455')
        center(newWindow)
        newWindow.resizable(width=False, height=False)

    #-----------------------------------------------------------------------------------------------------------------------

        txt1 = Label(newWindow, text='Código do item:', fg='black', font='poppins 16')
        txt1.place(x=40, y=160)

        codigo = Entry(newWindow, validate="key", background='#c1c1c3', fg='black', font='poppins 20 bold')
        codigo['validatecommand'] = (codigo.register(testVal),'%P','%d')
        codigo.place(x=40, y=210, width=290)

    #-----------------------------------------------------------------------------------------------------------------------

        btnRem = Button(newWindow, text='Remover', background='#252525', fg='white', font='poppins 25', command=confirmarRem, borderwidth=0, cursor='tcross')
        btnRem.place(x=490, y=330, width=190)

        btnFechar = Button(newWindow, text='╳', background='#252525', fg='white', font='poppins 25', command=FecharJanela, borderwidth=0, cursor='tcross')
        btnFechar.place(x=490, y=22, width=190)

        btnReset = Button(newWindow, text='↺', background='#252525', fg='white', font='poppins 13 bold', command=resetPesq, borderwidth=0, cursor='tcross')
        btnReset.place(x=620, y=260, width=57)

    #-----------------------------------------------------------------------------------------------------------------------

        atualiza()

        newWindow.mainloop()

#-----------------------------------------------------------------------------------------------------------------------

    #Botão de adicionar produto

    def addProduto():

        opc_menu = [
            'Outros',
            'Padaria',
            'Alimentos (cereais e grãos)',
            'Congelados e frios',
            'Hortifruti',
            'Produtos de limpeza',
            'Higiene pessoal',
            'Bebidas',
            'Papelaria'
        ]

        def FecharJanela():
            newWindow.destroy()

        def resetPesq():
            nome.delete(0, END)
            custo.delete(0, END)
            estoque.delete(0, END)
            estoque.delete(0, END)


        def VerificarDados():

            codigo10 = "SELECT MAX(codigo) FROM produtos"

            cursor.execute(codigo10)

            res = cursor.fetchone()

            cdg = res[0] + 1

            codigo1 = str(cdg)


            nome1 = nome.get()
            preco = custo.get()
            estoque1 = estoque.get()
            menu1 = variable.get()



            if nome1 == '':
                Msg = tk.messagebox.showinfo(title="Alerta", message="Campo do nome está vazio! Formule-o novamente.")
                return addProduto()

            if preco == '':
                Msg = tk.messagebox.showinfo(title="Alerta", message="Campo do nome está vazio! Formule-o novamente.")
                return addProduto()

            if estoque1 == '':
                Msg = tk.messagebox.showinfo(title="Alerta", message="Campo do nome está vazio! Formule-o novamente.")
                return addProduto()


            comando_SQL = "INSERT INTO produtos(nome,codigo,preco,estoque,tipo) VALUES ('" + nome1 + "', '" + codigo1 + "', '" + preco + "', '" + estoque1 + "', '" + menu1 + "')"


            cursor.execute(comando_SQL)
            banco.commit()

            Msg = tk.messagebox.askquestion(title="Alerta",
                                            message="Enviado com sucesso! Deseja adicionar mais um produto?")

            if Msg == 'yes':
                newWindow.destroy()
                addProduto()
            else:
                newWindow.destroy()
                return False

    #-----------------------------------------------------------------------------------------------------------------------

        #JANELA PARA ALGUMA FUNÇÃO

        newWindow = tk.Toplevel()

        newWindow.geometry('700x455')
        center(newWindow)
        newWindow.resizable(width=False, height=False)

    #-----------------------------------------------------------------------------------------------------------------------

        txt2 = Label(newWindow, text='Nome do item:', fg='black', font='poppins 15')
        txt2.place(x=40, y=50)

        nome = Entry(newWindow, background='#c1c1c3', fg='black', font='poppins 20 bold')
        nome.place(x=40, y=90, width=290)

    #-----------------------------------------------------------------------------------------------------------------------

        txt4 = Label(newWindow, text='Preço do item:', fg='black', font='poppins 15')
        txt4.place(x=40, y=150)

        custo = Entry(newWindow, background='#c1c1c3', fg='black', font='poppins 20 bold')
        custo.place(x=40, y=190, width=290)

    #-----------------------------------------------------------------------------------------------------------------------

        txt5 = Label(newWindow, text='Estoque do item:', fg='black', font='poppins 15')
        txt5.place(x=40, y=250)

        estoque = Entry(newWindow, validate="key", background='#c1c1c3', fg='black', font='poppins 20 bold')
        estoque['validatecommand'] = (estoque.register(testVal),'%P','%d')
        estoque.place(x=40, y=290, width=290)

    #-----------------------------------------------------------------------------------------------------------------------

        btnEnviar = Button(newWindow, text='Enviar', background='#252525', fg='white', font='poppins 25', command=VerificarDados, borderwidth=0, cursor='tcross')
        btnEnviar.place(x=490, y=330, width=190)

        btnFechar = Button(newWindow, text='╳', background='#252525', fg='white', font='poppins 25', command=FecharJanela, borderwidth=0, cursor='tcross')
        btnFechar.place(x=490, y=22, width=190)

        btnReset = Button(newWindow, text='↺', background='#252525', fg='white', font='poppins 13 bold', command=resetPesq, borderwidth=0, cursor='tcross')
        btnReset.place(x=620, y=260, width=57)

        variable = tk.StringVar(newWindow)
        variable.set(opc_menu[0])

        opt = tk.OptionMenu(newWindow, variable, *opc_menu)
        opt.config(width=90, font='poppins 14', background='#252525', foreground='white', borderwidth=3)
        opt.place(x=40, y=377, width=400)

    #-----------------------------------------------------------------------------------------------------------------------

        atualiza()

        newWindow.mainloop()

#-----------------------------------------------------------------------------------------------------------------------

    #Centralizando janela

    def center(win):
        win.update_idletasks()

        width = win.winfo_width()
        frm_width = win.winfo_rootx() - win.winfo_x()
        win_width = width + 2 * frm_width

        height = win.winfo_height()
        titlebar_height = win.winfo_rooty() - win.winfo_y()
        win_height = height + titlebar_height + frm_width

        x = win.winfo_screenwidth() // 2 - win_width // 2
        y = win.winfo_screenheight() // 2 - win_height // 2

        win.geometry('{}x{}+{}+{}'.format(width, height, x, y))

        win.deiconify()

#-----------------------------------------------------------------------------------------------------------------------

    #Pegando a hora atual

    def time():
        string = strftime('%H:%M:%S %p')
        hora.config(text = string)
        hora.after(1000, time)

#-----------------------------------------------------------------------------------------------------------------------

    root = Tk()


    #Estilização

    root.title('SISTEMA CAIXA E ESTOQUE')
    root.configure(background="#D3D3D3")
    root.geometry('1700x930')
    center(root)
    root.resizable(width=False, height=False)


    NomePessoa = Label(root, text=f'Olá, {nomeAA}', background='#c1c1c3', fg='#383837', font='Poppins 12').place(x=80, y=125)

    tela = ttk.Notebook(root)
    tela.place(x=0, y=0, width=1700, height=930)

#----------------------------------------------------------------------------------------------------------------------

    compra = Frame(tela)
    tela.add(compra, text='Realizar Compra')

#----------------------------------------------------------------------------------------------------------------------

    def TelaCompra():

    #-----------------------------------------------------------------------------------------------------------------------

        def preco():
            banco = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="infoCaixa"
            )

            cursor = banco.cursor()

            codigo0 = codigo20.get()

            comando = "SELECT preco FROM produtos WHERE codigo = '" + codigo0 + "'"
            cursor.execute(comando)

            i2 = cursor.fetchone()


        def remove_all():
            for record in n.get_children():
                try:
                    n.delete(record)
                    atualizarJanela()
                except:
                    tk.messagebox.showinfo(title="Alerta", message="Não há linhas na tabela para deletar!")



        def selecionado():
            try:
                x = n.selection()[0]
                n.delete(x)
            except:
                tk.messagebox.showinfo(title="Alerta", message="Selecione uma linha da tabela, e, tente novamente!")


        def generar():

            total = 0.0

            for child in n.get_children():
                total += float(n.item(child, 'values')[4])

            painel['text'] = f'R$ {"%.2f" % (total)}'



        def details():

            def funcEnviar():
                codigo0 = codigo20.get()
                unidades0 = unidades.get()

                if codigo0 == '':
                    Msg = tk.messagebox.showinfo(title="Alerta", message="Campo do código está vazio! Formule-o novamente.")
                    return False

                if unidades0 == '':
                    Msg = tk.messagebox.showinfo(title="Alerta", message="Campo da quantidade está vazio! Formule-o novamente.")
                    return False

                elif unidades0 == '0':
                    Msg = tk.messagebox.showinfo(title="Alerta",message="Campo da quantidade não pode ser 0! Formule-o novamente.")
                    return False


                comando_SQL = "SELECT * FROM produtos WHERE codigo = '" + codigo0 + "'"
                cursor.execute(comando_SQL)
                records = cursor.fetchall()

                comando_SQL2 = "SELECT estoque FROM produtos WHERE codigo = '" + codigo0 + "'"
                cursor.execute(comando_SQL2)
                retorno = cursor.fetchone()

                estoque10 = (retorno[0] - float(unidades0))

                estoque1 = ("%.0f" % (estoque10))

                #comando_SQL3 = "UPDATE produtos SET estoque = '" + estoque1 + "' WHERE " -------------------------------------------------------------------------------------------------------------
                #comando_SQL3 = "UPDATE produtos SET estoque = '" + estoque1 + "' WHERE " -------------------------------------------------------------------------------------------------------------
                #comando_SQL3 = "UPDATE produtos SET estoque = '" + estoque1 + "' WHERE " -------------------------------------------------------------------------------------------------------------


                for i in records:
                    valorTotal0 = (i[2] * float(unidades0))


                for i in records:
                    n.insert("", "end", values=(i[1], i[0], i[2], unidades0, ("%.2f" % (valorTotal0))))


                for record in n.get_children():
                    valores = n.item(record, "values")
                    #print(valores[4])


                outro2 = Label(compra, text=f"Total de {(len(n.get_children()))} itens.", background='#c1c1c3', fg='#383837', font='Poppins 24').place(x=1220, y=200, width=396, height=80)


                codigo20.delete(0, END)
                unidades.delete(0, END)

                generar()
                n.update()
                compra.update()
                preco()


            funcEnviar()


        def enviar():
            res = (len(n.get_children()))
            if res == 0:
                Msgg = tk.messagebox.showinfo(title="Alerta", message="Você deve adicionar pelo menos 1 produto!")
                return False
            else:
                aaa = tk.messagebox.askquestion(title='Alerta', message='Você deseja finalizar a compra?')

                if aaa == 'yes':
                    enviar2()
                else:
                    return False


        def enviar2():

            def limitar_tamanho(p):
                if len(p) > 11:
                    return False
                return True

            def FecharJanela():
                newWindow.destroy()

            def resetPesq():
                nomeCliente.delete(0, END)
                cpfCliente.delete(0, END)

            string = strftime('%d/%m/%Y')
            hora.config(text=string)

            def VerificarDados():

                nome = nomeCliente.get()
                cpf = cpfCliente.get()

                if nome == '':
                    Msgg = tk.messagebox.showinfo(title="Alerta", message="Campo do nome está vazio! Formule-o novamente.")
                    return enviar()

                if cpf == '':
                    Msge = tk.messagebox.showinfo(title="Alerta", message="Campo do CPF está vazio! Formule-o novamente.")
                    return enviar()


                for record in n.get_children():
                    try:
                        n.delete(record)
                        atualizarJanela()
                    except:
                        tk.messagebox.showinfo(title="Alerta", message="Você não adicionou nenhum produto!")



                id = "SELECT MAX(idCompra) FROM vendas"

                cursor.execute(id)

                res = cursor.fetchone()

                cdg = res[0] + 1

                idCompra = str(cdg)


                comando_SQL = "INSERT INTO vendas (nome,cpf,idCompra,dataVenda) VALUES ('" + nome + "', '" + cpf + "', '" + str(idCompra) + "', '" + str(string) + "')"

                cursor.execute(comando_SQL)

                banco.commit()

                newWindow.destroy()




            newWindow = tk.Toplevel()

            vcmd = newWindow.register(func=limitar_tamanho)
            newWindow.geometry('700x455')
            center(newWindow)
            newWindow.resizable(width=False, height=False)
            newWindow.configure(background='#404040')



            #---[ PARTE DA ESTILIZAÇÃO ]--------------------------------------------------------------------------------------------------------------------------------

            l1 = Label(newWindow, text='Finalizando', background='#151515', fg='white', font='poppins 25').place(x=30, y=22, width=400, height=98)

            l2 = Label(newWindow, text='', background='#151515', fg='white', font='poppins 25').place(x=30, y=160, width=400, height=270)

            #-----------------------------------------------------------------------------------------------------------------------------------------------------------

            # --|
            # --|
            # --|

            #---[ PARTE DOS CAMPOS DE ENTRADA DE DADOS ]----------------------------------------------------------------------------------------------------------------

            Label(newWindow, text='Nome:', background='#151515', fg='white', font='poppins 16').place(x=50, y=190)

            nomeCliente = Entry(newWindow, foreground='#151515', background='#c1c2c3', font='Poppins 14', borderwidth=0)
            nomeCliente.place(x=50, y=230, width=360)


            Label(newWindow, text='CPF:', background='#151515', fg='white', font='poppins 16').place(x=50, y=300)

            cpfCliente = Entry(newWindow, foreground='#151515', background='#c1c2c3', font='Poppins 14', borderwidth=0,validate='key', validatecommand=(vcmd, '%P'))
            cpfCliente.place(x=50, y=340, width=360)

            #-----------------------------------------------------------------------------------------------------------------------------------------------------------

            # --|
            # --|
            # --|

            #---[ PARTE DOS BOTÕES COM FUNÇÕES ]------------------------------------------------------------------------------------------------------------------------

            btnEnviar = Button(newWindow, text='Enviar', background='#c1c2c3', fg='black', font='poppins 25', command=VerificarDados, borderwidth=0, cursor='tcross')
            btnEnviar.place(x=490, y=330, width=190)

            btnFechar = Button(newWindow, text='╳', background='#c1c2c3', fg='black', font='poppins 25 bold', command=FecharJanela, borderwidth=0, cursor='tcross')
            btnFechar.place(x=490, y=22, width=190)

            btnReset = Button(newWindow, text='↺', background='#c1c2c3', fg='black', font='poppins 13 bold', command=resetPesq, borderwidth=0, cursor='tcross')
            btnReset.place(x=620, y=260, width=57)

            #-----------------------------------------------------------------------------------------------------------------------------------------------------------



        def atualizarJanela():
            outro2 = Label(compra, text=f"Total de {(len(n.get_children()))} itens.", background='#c1c1c3', fg='#383837', font='Poppins 24').place(x=1220, y=200, width=396, height=80)
            compra.update()
            generar()


        def editarLinha():
            codigo20.delete(0, END)
            unidades.delete(0, END)

            selecionado1 = n.focus()

            values = n.item(selecionado1, 'values')

            codigo20.insert(0, values[0])
            unidades.insert(0, values[3])


        def salvarEdicao():

            selecionado1 = n.focus()

            n.item(selecionado1, text="", values=selecionado1[3])

            codigo20.delete(0, END)
            unidades.delete(0, END)



        #Parte da compra

        #Objetos para Estilização

        caixa1compra = Label(compra, text='', background='#c1c1c3').place(x=0, y=0, width=1700, height=170)
        titulocompra = Label(compra, text='SuperMercado Alvorada', background='#c1c1c3', fg='#383837', font='Poppins 44 bold').place(x=-400, y=0, width=1700, height=170)
        titulocompra = Label(compra, text='Compra', background='#c1c1c3', fg='#383837', font='Poppins 12').place(x=750, y=105)


        NomePessoa = Label(compra, text=f'Olá, {nomeAA}', background='#c1c1c3', fg='#383837', font='Poppins 12').place(x=80, y=125)


        titulo_mcompra = Label(compra, text='Painel com items da compra', background='#c1c1c3', fg='#383837', font='Poppins 24').place(x=50, y=200, width=1092, height=80)

        outro22 = Label(compra, text='Total de 0 itens.', background='#c1c1c3', fg='#383837',font='Poppins 24').place(x=1220, y=200, width=396, height=80)

        painel = Label(compra, text='R$ 00.00', background='#c1c1c3', fg='#383837', font='Poppins 62', borderwidth=0)
        painel.place(x=1220, y=260, width=396, height=130)

        add2 = Button(compra, text="Remover Produto", command=selecionado, font='Poppins 14 normal', background='#252525', fg='white', borderwidth=0)
        add2.place(x=1230, y=420, width=180)

        add3 = Button(compra, text="Remover Todos", command=remove_all, font='Poppins 14 normal', background='#252525', fg='white', borderwidth=0)
        add3.place(x=1427, y=420, width=180)

        add6 = Button(compra, text="Salvar Edição", command=salvarEdicao, font='Poppins 11 normal', background='#252525', fg='white', borderwidth=0)
        add6.place(x=1360, y=490, width=128)

        add4 = Button(compra, text="Editar Produto", command=editarLinha, font='Poppins 11 normal', background='#252525', fg='white', borderwidth=0)
        add4.place(x=1218, y=490, width=128)

        add5 = Button(compra, text="Atualizar", command=atualizarJanela, font='Poppins 11 normal', background='#252525', fg='white', borderwidth=0)
        add5.place(x=1500, y=490, width=128)


        n = ttk.Treeview(compra, columns=('id', 'Nome', 'valorItem', 'qtdProdutos', 'valorTotal'), show='headings')

        style = ttk.Style()
        style.configure("Treeview", font='Poppins 15', rowheight=35)
        style.configure("Treeview.Heading", font='Poppins 15')

        n.tag_configure('oddrow', background="white")
        n.tag_configure('evenrow', background="lightblue")

        n.column('id', minwidth=0, width=70, anchor=CENTER)
        n.column('Nome', minwidth=0, width=300)
        n.column('valorItem', minwidth=0, width=100, anchor=CENTER)
        n.column('qtdProdutos', minwidth=0, width=100, anchor=CENTER)
        n.column('valorTotal', minwidth=0, width=130, anchor=CENTER)

        n.heading('id', text='ID', anchor=CENTER)
        n.heading('Nome', text='Nome',)
        n.heading('valorItem', text='Valor Item', anchor=CENTER)
        n.heading('qtdProdutos', text='Quantidade', anchor=CENTER)
        n.heading('valorTotal', text='Valor Total', anchor=CENTER)

        n.place(x=50, y=273, width=1092, height=600)


        Label(compra, background='#505050').place(x=1218, y=592, width=400, height=280)

        Label(compra, background='#606060', text='Adicionar', font='poppins 17 bold', fg='white').place(x=1230, y=572, width=180)

        txt1 = Label(compra, text='Código do item:', fg='white', background='#505050', font='poppins 16')
        txt1.place(x=1273, y=640)

        codigo20 = Entry(compra, validate="key", fg='black', background='#c1c2c3', font='poppins 20 bold')
        codigo20['validatecommand'] = (codigo20.register(testVal), '%P', '%d')
        codigo20.place(x=1273, y=680, width=290)


        txt2 = Label(compra, text='Quantidade:', fg='white', background='#505050', font='poppins 16')
        txt2.place(x=1273, y=750)

        unidades = Entry(compra, validate="key", fg='black', background='#c1c2c3', font='poppins 20 bold')
        unidades['validatecommand'] = (unidades.register(testVal), '%P', '%d')
        unidades.place(x=1273, y=790, width=190)


        addBtn = Button(compra, text='╋', command=details, fg='black', background='#c1c2c3', font='poppins 20 bold', borderwidth=0)
        addBtn.place(x=1483, y=790, width=80, height=51)


        enviarBtn = Button(compra, text='Finalizar compra', command=enviar, background='#252525', fg='white', font='poppins 20', borderwidth=0, cursor='tcross')
        enviarBtn.place(x=1270, y=45, width=300)

#----------------------------------------------------------------------------------------------------------------------

    TelaCompra()

    root.mainloop()

#----------------------------------------------------------------------------------------------------------------------











#----------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------










#----------------------------------------------------------------------------------------------------------------------

#Centralizando janela

def center(win):
    win.update_idletasks()

    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width

    height = win.winfo_height()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width

    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2

    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    win.deiconify()

#----------------------------------------------------------------------------------------------------------------------

#Função para tornar Entry apenas numeros

def testVal(inStr,acttyp):
    if acttyp == '1': #insert
        if not inStr.isdigit():
            return False
    return True

#----------------------------------------------------------------------------------------------------------------------

def enviarLogin():

    id1 = id.get()
    senha1 = senha.get()

    if id1 == '' and senha1 == '':
        tk.messagebox.showerror(title="Alerta", message="Campo ID e SENHA vazio!")
        return False

    if id1 == '':
        tk.messagebox.showerror(title="Alerta", message="Campo ID vazio!")
        return False

    if senha1 == '':
        tk.messagebox.showerror(title="Alerta", message="Campo SENHA vazio!")
        return False




    banco = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="infoCaixa"
    )

    cursor = banco.cursor()

    sql = f"SELECT * FROM cadastros WHERE id = {id1} and senha = {senha1}"
    cursor.execute(sql)

    resultado = cursor.fetchall()

    if resultado:
        tk.messagebox.showinfo("Alerta", "Login realizado com sucesso!")
        verificarA()
        return True

    else:
        tk.messagebox.showinfo("Alerta", "ID ou senha incorretos!")
        id.delete(0, END)
        senha.delete(0, END)
        return False

#----------------------------------------------------------------------------------------------------------------------

def verificarA():
    banco = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="infoCaixa"
    )

    cursor = banco.cursor()

    comando1 = f"SELECT cargo FROM cadastros WHERE id = {id.get()}"
    cursor.execute(comando1)

    rr = cursor.fetchone()

    cargo = (rr[0])

    pegarNome()

    if cargo == "ADM":
        l.destroy()
        app()
        return True


    else:
        l.destroy()
        app2()
        return True

#----------------------------------------------------------------------------------------------------------------------

def atualizarSenha():

    def verificarDados():

        banco = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="infoCaixa"
        )

        cursor = banco.cursor()

        cursor.execute(f"UPDATE cadastros SET senha = {novaSenha.get()} WHERE id = {idAtual.get()}")

        banco.commit()

        tk.messagebox.showinfo("Alerta", "Senha alterada com sucesso!")



    def FecharJanela():
        newWindow.destroy()

    def resetPesq():
        novaSenha.delete(0, END)
        idAtual.delete(0, END)



    newWindow = tk.Toplevel()
    newWindow.geometry('700x455')
    center(newWindow)
    newWindow.resizable(width=False, height=False)
    newWindow.configure(background='#404040')

    # ---[ PARTE DA ESTILIZAÇÃO ]--------------------------------------------------------------------------------------------------------------------------------


    l1 = Label(newWindow, text='Redefinir Senha', background='#151515', fg='white', font='poppins 25').place(x=30, y=22, width=400, height=98)

    l2 = Label(newWindow, text='', background='#151515', fg='white', font='poppins 25').place(x=30, y=160, width=400, height=270)


    # ---[ PARTE DOS CAMPOS DE ENTRADA DE DADOS ]----------------------------------------------------------------------------------------------------------------

    Label(newWindow, text='ID:', background='#151515', fg='white', font='poppins 16').place(x=50, y=190)

    idAtual = Entry(newWindow, foreground='#151515', validate="key", background='#c1c2c3', font='Poppins 14', borderwidth=0)
    idAtual['validatecommand'] = (idAtual.register(testVal), '%P', '%d')
    idAtual.place(x=50, y=230, width=360)

    Label(newWindow, text='Nova Senha:', background='#151515', fg='white', font='poppins 16').place(x=50, y=300)

    novaSenha = Entry(newWindow, foreground='#151515', validate="key", background='#c1c2c3', font='Poppins 14', borderwidth=0)
    novaSenha['validatecommand'] = (novaSenha.register(testVal), '%P', '%d')
    novaSenha.place(x=50, y=340, width=360)


    # ---[ PARTE DOS BOTÕES COM FUNÇÕES ]------------------------------------------------------------------------------------------------------------------------

    btnEnviar = Button(newWindow, text='Enviar', background='#c1c2c3', fg='black', font='poppins 25', command=verificarDados, borderwidth=0, cursor='tcross')
    btnEnviar.place(x=490, y=330, width=190)

    btnFechar = Button(newWindow, text='╳', background='#c1c2c3', fg='black', font='poppins 25 bold', command=FecharJanela, borderwidth=0, cursor='tcross')
    btnFechar.place(x=490, y=22, width=190)

    btnReset = Button(newWindow, text='↺', background='#c1c2c3', fg='black', font='poppins 13 bold', command=resetPesq, borderwidth=0, cursor='tcross')
    btnReset.place(x=620, y=260, width=57)

    # -----------------------------------------------------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------------

#LOGIN


l = Tk()

l.title('Login')
l.configure(background="white")
l.geometry('800x700')
center(l)
l.resizable(width=False, height=False)

global id
global senha


label = Image.open("img/label.png")
photo = ImageTk.PhotoImage(label)


Label(l, image=photo).place(x=100, y=70, width=610, height=550)


Label(l, text='ID:', background='#c2c3c4', foreground='#151515', font='Poppins 20').place(x=130, y=240)

id = Entry(l, background='#a1a1a1', validate='key', foreground='#151515', font='Poppins 20', borderwidth=0)
id['validatecommand'] = (id.register(testVal), '%P', '%d')
id.place(x=130, y=290, width=550)


Label(l, text='Senha:', background='#c2c3c4', foreground='#151515', font='Poppins 20').place(x=130, y=380)

senha = Entry(l, background='#a1a1a1', validate='key', foreground='#151515', font='Poppins 20', borderwidth=0, show='*')
senha['validatecommand'] = (senha.register(testVal), '%P', '%d')
senha.place(x=130, y=430, width=550)


EnviarLogin = Button(l, text='Enviar', background='#252525', foreground='white', font='Poppins 18', command=enviarLogin)
EnviarLogin.place(x=580, y=540, width=100, height=50)

ResetarSenha = Button(l, text='Esqueceu a senha?', background='#252525', foreground='white', font='Poppins 12', command=atualizarSenha)
ResetarSenha.place(x=130, y=540, width=190, height=50)


versao = Label(l, text='v1.3', background='#252525', foreground='white', font='Poppins 12').place(x=760, y=670, width=50, anchor=CENTER)

l.mainloop()



#----------------------------------------------------------------------------------------------------------------------