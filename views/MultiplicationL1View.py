import customtkinter
import random
from PIL import Image

class MultiplicationL1View(customtkinter.CTk):
    """
        Classe contenant la logique de la page pour la multiplication
    """
    def __init__(self):
        """
            Initialise le visuel de la page pour la multiplication
        """
        super().__init__()

        self.time_left = 10
        self.time_loop = None
        self.number_1 = random.randint(0, 9)
        self.number_2 = random.randint(1, 9)
        self.result = self.number_1 * self.number_2

        self.Skranji_36 = customtkinter.CTkFont(family="Skranji", size=36)
        self.Skranji_48 = customtkinter.CTkFont(family="Skranji", size=48)
        self.Skranji_64 = customtkinter.CTkFont(family="Skranji", size=64)

        self.geometry("1440x1080")
        self.title("CalculApp - Multiplication")
        self.grid_rowconfigure(0, weight=3)
        self.grid_columnconfigure((0, 1), weight=5)

        self.label_1 = customtkinter.CTkLabel(master=self, text="Temps restant : " + str(self.time_left) + " secondes", font=self.Skranji_64)
        self.label_1.pack(pady=15, padx=20)

        self.frame_1 = customtkinter.CTkFrame(master=self, corner_radius=20, border_color="green", border_width=4)
        self.frame_1.pack(pady=75, padx=100)

        self.label_bidon = customtkinter.CTkLabel(master=self.frame_1, text="", font=self.Skranji_48)
        self.label_bidon.grid(row=0, column=0, pady=5, padx=50)

        self.label_2 = customtkinter.CTkLabel(master=self.frame_1, text=str(self.number_1), font=self.Skranji_48)
        self.label_2.grid(row=1, column=0, pady=5, padx=50)

        self.label_3 = customtkinter.CTkLabel(master=self.frame_1, text="x", font=self.Skranji_48)
        self.label_3.grid(row=1, column=1, pady=5, padx=50)

        self.label_4 = customtkinter.CTkLabel(master=self.frame_1, text=str(self.number_2), font=self.Skranji_48)
        self.label_4.grid(row=1, column=2, pady=5, padx=50)

        self.label_5 = customtkinter.CTkLabel(master=self.frame_1, text="=", font=self.Skranji_48)
        self.label_5.grid(row=1, column=3, pady=5, padx=50)

        self.entry_1 = customtkinter.CTkEntry(master=self.frame_1, placeholder_text="?", font=self.Skranji_36)
        self.entry_1.grid(row=1, column=4, pady=5, padx=50)

        self.label_bidon_2 = customtkinter.CTkLabel(master=self.frame_1, text="", font=self.Skranji_48)
        self.label_bidon_2.grid(row=2, column=0, pady=5, padx=50)

        self.button_1 = customtkinter.CTkButton(master=self.frame_1, text="Vérifiez votre réponse", font=self.Skranji_48, command=self.control_button)
        self.button_1.grid(row=3, column=0, columnspan=5, pady=20, padx=40, ipady=10, ipadx=10)

        self.image_1 = customtkinter.CTkImage(light_image=Image.open("assets/icon.png"), dark_image=Image.open("assets/icon.png"), size=(100, 100))
        self.button_image = customtkinter.CTkButton(self, image=self.image_1, text="", fg_color="transparent")
        self.button_image.pack()

        self.countdown()

    def control_button(self):
        """
            Fonction qui permet de vérifier si la réponse est correcte
        """

        if self.time_left == 0:
            self.button_1.configure(state="disabled")
            self.button_1.configure(fg_color="transparent")

        if self.entry_1.get() == str(self.result):
            self.entry_1.configure(fg_color="green")

            self.destroy()
            app = MultiplicationL1View()
            app.mainloop()
        else:
            self.entry_1.configure(fg_color="red")

    def countdown(self):
        """
            Fonction qui permet d'avoir un chronomètre pour le jeu
        """
        if self.time_left > 0:
            self.time_left -= 1

            if self.time_left <= 1:
                self.label_1.configure(text="Temps restant : " + str(self.time_left) + " seconde")
                self.time_loop = self.label_1.after(1000, self.countdown)
            else:
                self.label_1.configure(text="Temps restant : " + str(self.time_left) + " secondes")
                self.time_loop = self.label_1.after(1000, self.countdown)
        else:
            self.after_cancel(self.time_loop)
            customtkinter.CTkMessageBox(text="Le temps est écoulé. Appuyer sur OK pour continuer ! Et n'oubliez pas de fermer la page de jeu !", title="C'est fini !")