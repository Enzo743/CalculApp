import customtkinter
from views.AdditionsL1View import *
from views.AdditionsL2View import *
from views.MultiplicationL1View import *
from views.MultiplicationL2View import *
from PIL import Image

class HomeView(customtkinter.CTk):
    """
        Classe contenant la logique de la page d'accueil
    """
    def __init__(self):
        """
            Initialise le visuel de la page d'accueil
        """
        super().__init__()

        self.Skranji_16 = customtkinter.CTkFont(family="Skranji", size=16)
        self.Skranji_24 = customtkinter.CTkFont(family="Skranji", size=24)
        self.Skranji_48 = customtkinter.CTkFont(family="Skranji", size=48)
        self.Skranji_128 = customtkinter.CTkFont(family="Skranji", size=128)

        self.geometry("1440x1080")
        self.title("CalculApp")

        self.label_1 = customtkinter.CTkLabel(master=self, text="CalculApp", font=self.Skranji_128)
        self.label_1.pack(pady=15, padx=10)

        self.frame_1 = customtkinter.CTkFrame(master=self, corner_radius=20, border_color="green", border_width=4)
        self.frame_1.pack(pady=75, padx=100)

        self.label_2 = customtkinter.CTkLabel(master=self.frame_1, text="Choissisez vos paramètres pour jouer :", font=self.Skranji_48)
        self.label_2.pack(pady=15, padx=20)

        self.label_3 = customtkinter.CTkLabel(master=self.frame_1, text="Opérations :", font=self.Skranji_24)
        self.label_3.pack(pady=15, padx=20)

        self.segmented_button_1 = customtkinter.CTkSegmentedButton(master=self.frame_1, values=["Additions", "Multiplications"], font=self.Skranji_16)
        self.segmented_button_1.pack(pady=15, padx=20)
        self.segmented_button_1.set("Additions")

        self.label_4 = customtkinter.CTkLabel(master=self.frame_1, text="Niveau choisi :", font=self.Skranji_24)
        self.label_4.pack(pady=15, padx=20)

        self.segmented_button_2 = customtkinter.CTkSegmentedButton(master=self.frame_1, values=["Niveau 1", "Niveau 2"], font=self.Skranji_16)
        self.segmented_button_2.pack(pady=15, padx=20)
        self.segmented_button_2.set("Niveau 1")

        self.button_2 = customtkinter.CTkButton(master=self.frame_1, text="Lancer le jeu", font=self.Skranji_24, width=400, height=50, command=self.start_button)
        self.button_2.pack(pady=30, padx=10)

        self.image_1 = customtkinter.CTkImage(light_image=Image.open("assets/icon.png"), dark_image=Image.open("assets/icon.png"), size=(100, 100))
        self.button_image = customtkinter.CTkButton(self, image=self.image_1, text="", fg_color="transparent")
        self.button_image.pack()

    def start_button(self):
        """
            Fonction permettant d'effectuer une action quand on clique sur le bouton pour lancer le jeu
            Récupére la position du bouton pour choisir l'opération et le niveau
        """
        operation = self.segmented_button_1.get()
        level = self.segmented_button_2.get()

        if operation == "Additions":
            if level == "Niveau 1":
                self.destroy()
                app = AdditionsL1View()
                app.mainloop()
            elif level == "Niveau 2":
                self.destroy()
                app = AdditionsL2View()
                app.mainloop()
        elif operation == "Multiplications":
            if level == "Niveau 1":
                self.destroy()
                app = MultiplicationL1View()
                app.mainloop()
            elif level == "Niveau 2":
                self.destroy()
                app = MultiplicationL2View()
                app.mainloop()


