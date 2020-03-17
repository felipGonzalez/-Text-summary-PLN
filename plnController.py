from plnView  import PlnView
from tkinter import *  
from tkinter import messagebox
from pubsub import pub
from plnModel import PlnModel
import re
import threading

class Controller:


    

    def __init__(self, root):
        print("Controllador")

        self.root = root
        self.view = PlnView(root,self)
        self.view.setup()
        self.model = PlnModel()
        self.root.protocol("WM_DELETE_WINDOW", self.exitApp)
        
       

               
    # Obtiene el texto a resumir
    def get_text(self):
        print("Obtiene el texto")
        self.text = self.view.get_text()
        print(self.text)
        self.set_text_View()

    
    def set_text_View(self):
        print("Setear texto")
        self.view.set_text("ESte es el texto")


    def init_resum(self):
        self.url = self.view.get_url()
        print("Url  :" +self.url)
        if self.url != "":
            print("Tiene URL")
            self.get_resum_url(self.url)
            pass
        else:
            print("No tiene URL")
            self.text = self.view.get_text()
            if self.text != "":
                print("Tiene Texto")
                self.get_resum(self.text)
                pass
            else:
                print("No tiene Texto")
                pass
            pass



    def get_resum_url(self, url):
        self.article = "No ha conexion"
        self.article = self.model.get_scraper_text(url)
        self.article = self.model.format_text(self.article)
        self.view.set_text(self.article)
        
        self.text_resum = self.model.get_resum(self.article)  
        self.view.set_text_resum(self.text_resum)
        

    def get_resum(self, text):
        self.article = self.model.format_text(text)
        self.text_resum = self.model.get_resum(self.article)  
        print(self.text_resum)
        self.view.set_text_resum(self.text_resum)


    def exitApp(self): 
        if messagebox.askokcancel("Salir", "Estas seguro que deseas salir?"):
            self.root.destroy()

   
    def paste_url(self):
        article = ""
        try:
            article = self.root.selection_get(selection= "CLIPBOARD")
            self.root.clipboard_clear
            print(article)
            print(article[0:8])
            print(article[0:8] == "https://")
            if article[0:8] == "https://":
                self.root.clipboard_clear
                self.view.set_text_url(article)
                pass
            else:
                messagebox.showwarning("Alerta","No hay una URL en el portapapeles")
        except:
            selection = None
            
    def show_info(self):
        messagebox.showinfo("Proyecto Inteligencia Artificial","Software Desarrollado por :\n- Andres Felipe Gonzalez Bonilla \n- Angel Nicolas Mendez Parra\n- Daniel Ricador Lopez \n\nInteligencia Artificial \n\n Escuela de Ingeniería de sistemas y computación \n\n Facutad de Ingenieria \n\n Universidad Pedagógica y Tecnológica de Colombia \n\n 2019")

    def paste_text(self):
        article = ""
        try:
            article = self.root.selection_get(selection= "CLIPBOARD")
            self.root.clipboard_clear
            article = self.model.format_text(article)
            self.view.set_text(article)            
        except:
            messagebox.showwarning("Alerta","No hay texto en el portapapeles")
        

    
if __name__ == "__main__":
    # Create main window object    
    root = Tk()
    
 

    # Instantiate HelloWorldFrame object    
    Controller(root)
    
    root.mainloop()