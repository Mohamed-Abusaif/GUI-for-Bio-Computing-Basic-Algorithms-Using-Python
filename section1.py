import main
from tkinter import *
import tkinter.messagebox
import customtkinter
from tkinter import filedialog

# Modes: "System" (standard), "Dark", "Light"
customtkinter.set_appearance_mode("Dark")
# Themes: "blue" (standard), "green", "dark-blue"
customtkinter.set_default_color_theme("blue")



class section1GUI(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        def browseFiles():
            global filename
            filename = filedialog.askopenfilename(initialdir="/",
                                                  title="Select a File",
                                                  filetypes=(("Text files",
                                                              "*.txt*"),
                                                
                                                             ("all files",
                                                              "*.*")))
            fileLabel = customtkinter.CTkLabel(frame, text="File Name: "+filename).pack()

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
        self.grid_rowconfigure((0, 1, 2, 3, 4), weight=1)
        frame = customtkinter.CTkFrame(master=self)
        frame.pack(pady=20, padx=60, fill="both", expand=True)
        label = customtkinter.CTkLabel(
            master=frame, text="Section 1:", font=("Roboto", 24))
        label.pack(pady=12, padx=10)

        test_btn = customtkinter.CTkButton(
            master=frame, text="Open Dataset File!", font=("Roboto", 20), command=browseFiles)
        test_btn.pack(pady=12, padx=10)
        print("hello Here")
   
   
        back_btn = customtkinter.CTkButton(
            master=frame, text="Back to Home!", font=("Roboto", 20), command=back_to_home)
        back_btn.pack(pady=12, padx=10)
