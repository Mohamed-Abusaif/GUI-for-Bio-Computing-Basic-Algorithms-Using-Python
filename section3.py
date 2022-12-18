import tkinter
import tkinter.messagebox
import customtkinter

# Modes: "System" (standard), "Dark", "Light"
customtkinter.set_appearance_mode("Dark")
# Themes: "blue" (standard), "green", "dark-blue"
customtkinter.set_default_color_theme("blue")

import main


class section3GUI(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        
        def back_to_home():
            print("hello")
            self.destroy()
            app = main.App()
            app.mainloop()

        # configure window
        self.title("Bio Computing Algorithms GUI")
        self.geometry(f"{500}x{500}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(0, weight=1)
        # self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2 , 3,4), weight=1)
        frame = customtkinter.CTkFrame(master=self)
        frame.pack(pady=20, padx=60, fill="both", expand=True)
        label = customtkinter.CTkLabel(master=frame, text="Section 3:", font=("Roboto", 24))
        label.pack(pady=12, padx=10)









        back_btn = customtkinter.CTkButton(master=frame, text="Back to Home!", font=("Roboto" , 20) , command=back_to_home)
        back_btn.pack(pady=12, padx=10)
        # back_btn.grid(row=3 , column =0 , pady=12, padx=10)




