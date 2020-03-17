import tkinter as tk
import tkinter.font as font



class PlnView(tk.Frame):    
    
            
    textString = ""
    textUrl = ""
    
    def __init__(self, root, controller):        

        root.title("Procesamiento de lenguaje natural")
        # Gets the requested values of the height and widht.
        windowWidth = root.winfo_screenwidth()
        windowHeight = root.winfo_screenheight()
        print("Width",windowWidth,"Height",windowHeight)
        
        self.controller = controller
        root.resizable(False, False)
        # Gets both half the screen width/height and window width/height
        positionRight = int(root.winfo_screenwidth()/2 - windowWidth/2)
        positionDown = int(root.winfo_screenheight()/2 - windowHeight/2)
 
        # Positions the window in the center of the page.
        root.geometry("+{}+{}".format(positionRight, positionDown))
        #root.geometry("%sx%s" % (self.windowWidth, self.windowHeight))  
        self.barMenu = tk.Menu(root)
        self.barMenu.config(bg="#634900",activebackground="#B08100")
        root.config(menu= self.barMenu)  
        self.myFrame = tk.Frame(root)    
        self.myFrame.pack()
        self.myFrame.config(bg="#e4a900")    
        # Place frame into main window          
               
       
    def setup(self): # run first
        self.create_menu()
        self.create_widgets()
        
    def create_menu(self):
        self.fileMenu = tk.Menu(self.barMenu, tearoff=0)
        self.fileMenu.config(bg="#634900",fg="#FFFFFF")
        self.editMenu = tk.Menu(self.barMenu, tearoff=0)
        self.editMenu.config(bg="#634900",fg="#FFFFFF")
        self.helpMenu = tk.Menu(self.barMenu, tearoff=0)
        self.helpMenu.config(bg="#634900",fg="#FFFFFF")

        self.fileMenu.add_command(label = "Salir", command = self.controller.exitApp,activebackground="#B08100")
        

        self.editMenu.add_command(label = "Limpiar Todo", command = self.clear_text,activebackground="#002196")
        self.editMenu.add_command(label = "Pegar URL", command = self.controller.paste_url,activebackground="#B08100")
        self.editMenu.add_command(label = "Pegar Texto", command = self.controller.paste_text,activebackground="#B08100")

        self.helpMenu.add_command(label = "Acerca de", command = self.controller.show_info,activebackground="#B08100")


        self.barMenu.add_cascade(label = "Archivo", menu=self.fileMenu,activebackground="#B08100")
        self.barMenu.add_cascade(label = "Edición", menu=self.editMenu,activebackground="#B08100")
        self.barMenu.add_cascade(label = "Ayuda", menu=self.helpMenu,activebackground="#B08100")
        

    def create_widgets(self):
       

        #Label de inicio
        self.hello = tk.Label(self.myFrame, text="Procesameinto de lenguaje natural",bg="#e4a900",fg="#FFFFFF",font=font.Font(family='Helvetica', size=25))       
        self.hello.grid(row=0, column=0, sticky=tk.W,padx=10, pady=10)
        # Input entrada de url
        self.urlPageLabel = tk.Label(self.myFrame, text= "Ingrese Url de pagina en ingles para resumir",bg="#e4a900",fg="#FFFFFF", font=font.Font(family='Helvetica', size=15))
        self.urlPageLabel.grid(row=1, column=0,sticky=tk.W,padx=10, pady=10)
        self.urlPage = tk.Entry(self.myFrame)
        self.urlPage.grid(row=2, column=0,sticky=tk.N+tk.S+tk.E+tk.W,padx=10, pady=10)
        # Label de texto a resumir
        self.textLabel = tk.Label(self.myFrame, text= "Texto", bg="#634900",fg="#FFFFFF",font=font.Font(family='Helvetica', size=10))
        self.textLabel.grid(row=4, column=0, sticky=tk.N+tk.S+tk.E+tk.W,padx=10, pady=10)
        #Caja de texto a resumir
        self.textBox = tk.Text(self.myFrame)
        self.textBox.grid(row=5, column=0, padx=10, pady=10, sticky=tk.N+tk.S+tk.E+tk.W)
        self.scrollBox = tk.Scrollbar(self.myFrame, command=self.textBox.yview)
        self.scrollBox.grid(row=5, column=1, sticky="nsew")
        self.textBox.config(yscrollcommand=self.scrollBox.set) 
        # Label texto resumido
        self.resumLabel = tk.Label(self.myFrame, text= "Resumen", bg="#634900",fg="#FFFFFF",font=font.Font(family='Helvetica', size=10))
        self.resumLabel.grid(row=4, column=2,sticky=tk.N+tk.S+tk.E+tk.W,padx=10, pady=10)
        self.textBoxResum = tk.Text(self.myFrame)
        self.textBoxResum.grid(row=5, column=2, padx=10, pady=10,sticky=tk.N+tk.S+tk.E+tk.W)

        self.scrollBoxResum = tk.Scrollbar(self.myFrame, command=self.textBox.yview)
        self.scrollBoxResum.grid(row=5, column=3, sticky="nsew")
        self.textBoxResum.config(yscrollcommand=self.scrollBoxResum.set) 
        #Boton de resume
        self.buttonResum = tk.Button(self.myFrame, text = "Realizar resumen",command = self.controller.init_resum,bg="#449d44", fg="#FFFFFF",font=font.Font(family='Helvetica', size=15))
        self.buttonResum.grid(row=3, column=0, sticky=tk.N+tk.S+tk.E+tk.W, padx=10, pady=10)
        #Limpiar texto
        self.buttonResum = tk.Button(self.myFrame, text = "Limpiar texto",command = self.clear_text,bg="#0a2f54", fg="#FFFFFF",font=font.Font(family='Helvetica', size=15))
        self.buttonResum.grid(row=2, column=2, sticky=tk.W)

    def get_text(self):
        return  self.textBox.get("1.0",'end-1c')

    def set_text(self, text_set):
        print(text_set)
        self.textBox.delete('1.0',tk.END)
        self.textBox.insert(tk.INSERT,text_set)

    def set_text_url(self, text_set):
        print("Entro  a reemplazar")
        print(text_set)
        self.urlPage.delete(0,tk.END)
        self.urlPage.insert(0,text_set)
       

    def set_text_resum(self, text_set):
        print(text_set)
        self.textBoxResum.delete('1.0',tk.END)
        self.textBoxResum.insert(tk.INSERT,text_set)    

    def clear_text(self):
        self.textBox.delete('1.0',tk.END)
        self.textBoxResum.delete('1.0',tk.END)
        self.urlPage.delete(0,tk.END)

    def get_url(self):
        return  self.urlPage.get()      

