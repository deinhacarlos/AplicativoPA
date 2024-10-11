from tkinter import*
from tkinter import ttk

#Criando janela tk
root = Tk()
#Configuração títuo do app
root.title("Pés para Metros")
#Gerando loop para rederização iterminente

def calculate(*args):
    try:
        value = float(feet.get()) #Entrada
        result = int(0.3048 * value * 10000.0 + 0.5)/10000.0 #Processamento
        meters.set(result) #Saída
    except ValueError:
        pass

#Criando o nosso container <div></div>
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N,W,E,S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

feet = StringVar()
#<input>
feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=(W,E))

meters = StringVar()
ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W,E))

ttk.Button(mainframe, text="Calcular", command=calculate).grid(column=3, row=3, sticky=W)

#<p></p>
ttk.Label(mainframe, text="Pes").grid(column=3, row=1, sticky=W)
#<p></p>
ttk.Label(mainframe, text="é equivalente a").grid(column=1, row=2, sticky=E)
#<p></p>   
ttk.Label(mainframe, text="Metros").grid(column=3, row=2, sticky=W)

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)
feet_entry.focus()
root.bind("<Return>", calculate)

#Gerando loop para rederização iterminente
root.mainloop()