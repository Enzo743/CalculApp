import customtkinter
import csv
import tkinter as tk
from views.HomeView import HomeView
from PIL import Image

class RegisterView(customtkinter.CTk):
    """
        Classe contenant la logique de la page d'inscription
    """
    def __init__(self):
        """
            Initialise le visuel de la page d'inscription
        """
        super().__init__()

        self.Skranji_16 = customtkinter.CTkFont(family="Skranji", size=16)
        self.Skranji_24 = customtkinter.CTkFont(family="Skranji", size=24)
        self.Skranji_48 = customtkinter.CTkFont(family="Skranji", size=48)
        self.Skranji_128 = customtkinter.CTkFont(family="Skranji", size=128)

        self.geometry("1440x1080")
        self.title("CalculApp - Inscription")

        # self.image_1 = customtkinter.CTkImage(light_image=Image.open("assets/cloud-icon.png"), dark_image=Image.open("assets/cloud-icon.png"), size=(100, 100))

        self.label_1 = customtkinter.CTkLabel(master=self, text="CalculApp", font=self.Skranji_128)
        self.label_1.pack(pady=15, padx=10)

        self.frame_1 = customtkinter.CTkFrame(master=self, corner_radius=20, border_color="green", border_width=4)
        self.frame_1.pack(pady=75, padx=100)

        self.label_2 = customtkinter.CTkLabel(master=self.frame_1, text="Enregistrez-vous pour pouvoir jouer !", font=self.Skranji_48)
        self.label_2.pack(pady=30, padx=50)

        self.label_3 = customtkinter.CTkLabel(master=self.frame_1, text="Nom d'utilisateur", font=self.Skranji_24)
        self.label_3.pack(padx=50, anchor="w")

        self.entry_1 = customtkinter.CTkEntry(master=self.frame_1, width=400, height=50, placeholder_text="Entrez le ici...", font=self.Skranji_16)
        self.entry_1.pack(pady=10, padx=50, anchor="w")

        self.label_4 = customtkinter.CTkLabel(master=self.frame_1, text="Mot de passe", font=self.Skranji_24)
        self.label_4.pack(padx=50, anchor="w")

        self.entry_2 = customtkinter.CTkEntry(master=self.frame_1, width=400, height=50, placeholder_text="Entrez le ici...", font=self.Skranji_16)
        self.entry_2.pack(pady=10, padx=50, anchor="w")

        self.label_5 = customtkinter.CTkLabel(master=self.frame_1, text="Age", font=self.Skranji_24)
        self.label_5.pack(padx=50, anchor="w")

        self.combobox_1 = customtkinter.CTkOptionMenu(master=self.frame_1, values=["8-10 ans", "11-13 ans", "14-18 ans"])
        self.combobox_1.pack(pady=10, padx=50, anchor="w")
        self.combobox_1.set("8-10 ans")

        self.button_1 = customtkinter.CTkButton(master=self.frame_1, text="Créer mon compte", font=self.Skranji_24, width=400, height=50, command=self.register_button)
        self.button_1.pack(pady=30, padx=10)

        self.image_1 = customtkinter.CTkImage(light_image=Image.open("assets/icon.png"), dark_image=Image.open("assets/icon.png"), size=(100, 100))
        self.button_image = customtkinter.CTkButton(self, image=self.image_1, text="", fg_color="transparent")
        self.button_image.pack()

    def register_button(self):
        """
            Fonction permettant d'effectuer une action quand on clique sur le bouton d'inscription
            Récupére l'entrée du nom d'utilisateur et du mot de passe et vérifie dans le fichier csv la validité
        """
        username_list = []

        username = self.entry_1.get()
        password = self.entry_2.get()
        age = self.combobox_1.get()

        file = open("./assets/data.csv", encoding="utf8", mode="a+")
        writer = csv.writer(file)
        writer.writerow([username, password, age])
        file.close()

        self.destroy()
        app = HomeView()
        app.mainloop()