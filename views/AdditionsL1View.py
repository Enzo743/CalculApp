import customtkinter
import tkinter as tk
import random
from PIL import Image

class AdditionsL1View(customtkinter.CTk):
    """
        Classe contenant la logique de la page pour l'addition de niveau 1
    """
    def __init__(self):
        """
            Initialise le visuel de la page d'addition
        """
        super().__init__()

        self.time_left = 25
        self.time_loop = None
        self.number_1 = random.randint(0, 9)
        self.number_2 = random.randint(0, 9)
        self.number_3 = random.randint(0, 9)
        self.number_4 = random.randint(0, 9)
        self.result_1 = self.number_2 + self.number_4
        self.result_2 = self.number_1 + self.number_3

        self.Skranji_24 = customtkinter.CTkFont(family="Skranji", size=24)
        self.Skranji_36 = customtkinter.CTkFont(family="Skranji", size=36)
        self.Skranji_48 = customtkinter.CTkFont(family="Skranji", size=48)
        self.Skranji_64 = customtkinter.CTkFont(family="Skranji", size=64)

        self.geometry("1440x1080")
        self.title("CalculApp - Addition")
        self.grid_rowconfigure(0, weight=6)
        self.grid_columnconfigure((0, 1), weight=3)

        self.label_1 = customtkinter.CTkLabel(master=self, text="Temps restant : " + str(self.time_left) + " secondes", font=self.Skranji_64)
        self.label_1.pack(pady=15, padx=20)

        self.frame_1 = customtkinter.CTkFrame(master=self, corner_radius=20, border_color="green", border_width=4)
        self.frame_1.pack(pady=85, padx=100)

        if self.result_1 > 9:
            self.entry_3 = customtkinter.CTkEntry(master=self.frame_1, placeholder_text="?", font=self.Skranji_36)
            self.entry_3.grid(row=0, column=1, pady=5, padx=50)

        self.label_2 = customtkinter.CTkLabel(master=self.frame_1, text=str(self.number_1), font=self.Skranji_48)
        self.label_2.grid(row=1, column=1, pady=5, padx=50)

        self.label_3 = customtkinter.CTkLabel(master=self.frame_1, text=str(self.number_2), font=self.Skranji_48)
        self.label_3.grid(row=1, column=2, pady=5, padx=50)

        self.label_4 = customtkinter.CTkLabel(master=self.frame_1, text="+", font=self.Skranji_48)
        self.label_4.grid(row=2, column=0, pady=25, padx=20)

        self.label_5 = customtkinter.CTkLabel(master=self.frame_1, text=str(self.number_3), font=self.Skranji_48)
        self.label_5.grid(row=2, column=1, pady=5, padx=50)

        self.label_6 = customtkinter.CTkLabel(master=self.frame_1, text=str(self.number_4), font=self.Skranji_48)
        self.label_6.grid(row=2, column=2, pady=5, padx=50)

        self.label_7 = customtkinter.CTkLabel(master=self.frame_1, text="-------------------------------------------------", font=self.Skranji_24)
        self.label_7.grid(row=3, column=0, columnspan=3, pady=2)

        self.label_8 = customtkinter.CTkLabel(master=self.frame_1, text="=", font=self.Skranji_48)
        self.label_8.grid(row=4, column=0, pady=25, padx=50)

        self.entry_1 = customtkinter.CTkEntry(master=self.frame_1, placeholder_text="?", font=self.Skranji_36)
        self.entry_1.grid(row=4, column=1, pady=5, padx=50)

        self.entry_2 = customtkinter.CTkEntry(master=self.frame_1, placeholder_text="?", font=self.Skranji_36)
        self.entry_2.grid(row=4, column=2, pady=5, padx=50)

        self.button_1 = customtkinter.CTkButton(master=self.frame_1, text="Vérifiez votre réponse", font=self.Skranji_48, command=self.control_button)
        self.button_1.grid(row=5, column=0, columnspan=3, pady=25, padx=30, ipady=10, ipadx=10)

        self.image_1 = customtkinter.CTkImage(light_image=Image.open("assets/icon.png"), dark_image=Image.open("assets/icon.png"), size=(100, 100))
        self.button_image = customtkinter.CTkButton(self, image=self.image_1, text="", fg_color="transparent")
        self.button_image.pack()

        self.countdown()

    def control_button(self):
        """
            Fonction qui vérifie les réponses entrées dans les cases attitrés
            Affiche une case verte si la réponse est juste et une case rouge si la réponse est fausse
        """
        response_1 = self.entry_1.get()
        response_2 = self.entry_2.get()

        if self.time_left == 0:
            self.button_1.configure(state="disabled")
            self.button_1.configure(fg_color="transparent")

        if self.result_1 > 9:
            carried_number = self.entry_3.get()
            if int(response_2) == int(self.result_1) - 10 and int(response_1) == int(self.result_2) + 1 and int(carried_number) == int(1):
                self.entry_2.configure(fg_color="green")
                self.entry_1.configure(fg_color="green")
                self.entry_3.configure(fg_color="green")

                self.destroy()
                app = AdditionsL1View()
                app.mainloop()
            elif int(response_2) != int(self.result_1) - 10 and int(response_1) == int(self.result_2) + 1 and int(carried_number) == int(1):
                self.entry_2.configure(fg_color="red")
                self.entry_1.configure(fg_color="green")
                self.entry_3.configure(fg_color="green")
            elif int(response_2) == int(self.result_1) - 10 and int(response_1) != int(self.result_2) + 1 and int(carried_number) == int(1):
                self.entry_2.configure(fg_color="green")
                self.entry_1.configure(fg_color="red")
                self.entry_3.configure(fg_color="green")
            elif int(response_2) == int(self.result_1) - 10 and int(response_1) == int(self.result_2) + 1 and int(carried_number) != int(1):
                self.entry_2.configure(fg_color="green")
                self.entry_1.configure(fg_color="green")
                self.entry_3.configure(fg_color="red")
            elif int(response_2) != int(self.result_1) - 10 and int(response_1) != int(self.result_2) + 1 and int(carried_number) == int(1):
                self.entry_2.configure(fg_color="red")
                self.entry_1.configure(fg_color="red")
                self.entry_3.configure(fg_color="green")
            elif int(response_2) != int(self.result_1) - 10 and int(response_1) == int(self.result_2) + 1 and int(carried_number) != int(1):
                self.entry_2.configure(fg_color="red")
                self.entry_1.configure(fg_color="green")
                self.entry_3.configure(fg_color="red")
            elif int(response_2) == int(self.result_1) - 10 and int(response_1) != int(self.result_2) + 1 and int(carried_number) != int(1):
                self.entry_2.configure(fg_color="green")
                self.entry_1.configure(fg_color="red")
                self.entry_3.configure(fg_color="red")
            elif int(response_2) != int(self.result_1) - 10 and int(response_1) != int(self.result_2) + 1 and int(carried_number) != int(1):
                self.entry_2.configure(fg_color="red")
                self.entry_1.configure(fg_color="red")
                self.entry_3.configure(fg_color="red")
        else:
            carried_number = 0
            if int(response_2) == int(self.result_1) and int(response_1) == int(self.result_2):
                self.entry_2.configure(fg_color="green")
                self.entry_1.configure(fg_color="green")

                self.destroy()
                app = AdditionsL1View()
                app.mainloop()
            elif int(response_2) == int(self.result_1) and int(response_1) != int(self.result_2):
                self.entry_2.configure(fg_color="green")
                self.entry_1.configure(fg_color="red")
            elif int(response_2) != int(self.result_1) and int(response_1) == int(self.result_2):
                self.entry_2.configure(fg_color="red")
                self.entry_1.configure(fg_color="green")
            elif int(response_2) != int(self.result_1) and int(response_1) != int(self.result_2):
                self.entry_2.configure(fg_color="red")
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
            tk.messagebox.showinfo(message="Le temps est écoulé. Appuyer sur OK pour continuer ! Et n'oubliez pas de fermer la page de jeu !", title="C'est fini !")