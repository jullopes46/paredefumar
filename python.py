import tkinter as tk

# função de botão

def fechar():
    janela.destroy()

# conficuração da tela
janela = tk.Tk()
janela.geometry("600x400")
janela.title("Calculadora de desperdicio")

# campo

campo1 = tk.Entry(janela)
campo2 = tk.Entry(janela)
campo3 = tk.Entry(janela)

#label 
text1 = tk.Label(janela, text="Valor: ")
text2 = tk.Label(janela, text="Quantia: ")
text3 = tk.Label(janela, text="tempo: ")

# botão

fechar_janela = tk.Button(janela, text="fechar", command=fechar)

# organização da tela
text1.pack()
campo1.pack()
text2.pack()
campo2.pack()
text3.pack()
campo3.pack()
fechar_janela.pack()

valor = 7 #float(input("Qual o valor do maço?: "))
quantia  = 1 #float(input("Qual a quantia em maço que vc fuma?: "))
tempo = 10 #float(input("Por quanto tempo vc fuma?: "))
custo = (valor/20*(quantia*20)*(tempo*365))
cigarro = valor/20
mes = 30
ano = mes*12

print(f'O valor de cada cigarro é R$ {cigarro:.2f}'.replace('.',','))
print(f'Se voce fumou {quantia} cigarro por dia vc fumou {(quantia/20)*100}%\n de um maço e gastou em um mes R$ {(cigarro*20)*mes:.2f}'.replace('.',','))
print(f'Em se um ano tem {ano} dia e cada cigarro tem o valor de R$ {cigarro:.2f}\n no fim das contas em um ano você fumou {quantia*ano}'.replace('.',','))
print(f'Ao total você acabou de gastar aproximadamente R$ {custo:.2f}'.replace('.',','))

if custo < 5000:
    print('Você fumou uma viagem para o nordeste')
elif custo < 9000:
    print('Você fumou uma entrada de um carro popular')
else:
    print('Você fumou a entrada da sua casa propria')
    
    
    

    
    
    
janela.mainloop()