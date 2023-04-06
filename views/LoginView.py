import customtkinter
import tkinter as tk
import csv
from views.RegisterView import RegisterView
from views.HomeView import HomeView
from PIL import Image

class LoginView(customtkinter.CTk):
    """
        Classe contenant la logique de la page de connection
    """
    def __init__(self):
        """
            Initialise le visuel de la page de connection
        """
        super().__init__()

        self.Skranji_16 = customtkinter.CTkFont(family="Skranji", size=16)
        self.Skranji_24 = customtkinter.CTkFont(family="Skranji", size=24)
        self.Skranji_48 = customtkinter.CTkFont(family="Skranji", size=48)
        self.Skranji_128 = customtkinter.CTkFont(family="Skranji", size=128)

        self.geometry("1920x1080")
        self.title("CalculApp - Connexion")

        self.label_1 = customtkinter.CTkLabel(master=self, text="CalculApp", font=self.Skranji_128)
        self.label_1.pack(pady=15, padx=10)

        self.frame_1 = customtkinter.CTkFrame(master=self, corner_radius=20, border_color="green", border_width=4)
        self.frame_1.pack(pady=75, padx=100)

        self.label_2 = customtkinter.CTkLabel(master=self.frame_1, text="Identifiez-vous pour pouvoir jouer !", font=self.Skranji_48)
        self.label_2.pack(pady=30, padx=50)

        self.label_3 = customtkinter.CTkLabel(master=self.frame_1, text="Nom d'utilisateur", font=self.Skranji_24)
        self.label_3.pack(padx=50, anchor="w")

        self.entry_1 = customtkinter.CTkEntry(master=self.frame_1, width=400, height=50, placeholder_text="Entrez le ici...", font=self.Skranji_16)
        self.entry_1.pack(pady=10, padx=50, anchor="w")

        self.label_4 = customtkinter.CTkLabel(master=self.frame_1, text="Mot de passe", font=self.Skranji_24)
        self.label_4.pack(padx=50, anchor="w")

        self.entry_2 = customtkinter.CTkEntry(master=self.frame_1, width=400, height=50, placeholder_text="Entrez le ici...", font=self.Skranji_16)
        self.entry_2.pack(pady=10, padx=50, anchor="w")

        self.button_1 = customtkinter.CTkButton(master=self.frame_1, text="Se connecter", font=self.Skranji_24, width=400, height=50, command=self.login_button)
        self.button_1.pack(pady=30, padx=10)

        self.label_5 = customtkinter.CTkLabel(master=self.frame_1, text="Vous n'avez pas de compte ?", font=self.Skranji_24)
        self.label_5.pack()

        self.button_2 = customtkinter.CTkButton(master=self.frame_1, text="Inscrivez-vous !", font=self.Skranji_24, width=400, height=50, command=self.change_view_login)
        self.button_2.pack(pady=30, padx=10)

        self.image_1 = customtkinter.CTkImage(light_image=Image.open("assets/icon.png"), dark_image=Image.open("assets/icon.png"), size=(100, 100))
        self.button_image = customtkinter.CTkButton(self, image=self.image_1, text="", fg_color="transparent")
        self.button_image.pack()

    def login_button(self):
        """
            Fonction permettant d'effectuer une action quand on clique sur le bouton de connection
            Récupére l'entrée du nom d'utilisateur et du mot de passe et le met dans un fichier csv
        """
        username_list = []
        password_list = []

        username = self.entry_1.get()
        password = self.entry_2.get()

        file = open("./assets/data.csv", encoding="utf8")
        line = file.readline()

        for line in file:
            elements = line.strip().split(',')
            username_list.append(elements[0])
            password_list.append(elements[1])
        file.close()

        for username_unique in username_list:
            for password_unique in password_list:
                if username_unique == username and password_unique == password:
                    self.destroy()
                    app = HomeView()
                    app.mainloop()
                else:
                    self.entry_1.delete(tk.ANCHOR, tk.INSERT)
                    self.entry_2.delete(tk.ANCHOR, tk.INSERT)
                    return customtkinter.CTkMessageBox(text="Vos identifiants ne sont pas corrects !", title="Attention !")

    def change_view_login(self):
        """
            Fonction permettant de passer sur la page d'inscription
        """
        self.destroy()
        app = RegisterView()
        app.mainloop()