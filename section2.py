import main
import tkinter as tk
import tkinter.messagebox
import customtkinter
from functools import partial




from SectionsAlgorithms.AlgoSec2 import *



# Modes: "System" (standard), "Dark", "Light"
customtkinter.set_appearance_mode("Dark")
# Themes: "blue" (standard), "green", "dark-blue"
customtkinter.set_default_color_theme("blue")


class section2GUI(customtkinter.CTk):
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
        self.grid_rowconfigure((0, 1, 2, 3, 4), weight=1)
        frame = customtkinter.CTkFrame(master=self)
        frame.pack(pady=20, padx=60, fill="both", expand=True)
        label = customtkinter.CTkLabel(
            master=frame, text="Section 2:", font=("Roboto", 24))
        label.pack(pady=12, padx=10)


        resultLabel = customtkinter.CTkLabel(master=frame,font=("Roboto",16) ,text="Your Result WIll Be Printed Here!")
        newSeq = tk.StringVar()
        EnterSeqLabel = customtkinter.CTkLabel(master=frame, text="Enter Sequence:", font=("Roboto", 16)).pack()
        sequenceEntry = customtkinter.CTkEntry(master=frame, textvariable=newSeq,placeholder_text="Sequence").pack()
        GC_Content_part = partial(GC_Content ,newSeq ,resultLabel)
        Complement_part = partial(Complement, newSeq,resultLabel)
        Reverse_part = partial(Reverse,newSeq, resultLabel)
        Reverse_Complement_part = partial(Reverse_Complement,newSeq, resultLabel)

        #function -> button -> label 
        GC_btn = customtkinter.CTkButton(master=frame, text="Get GC Content!",command=GC_Content_part).pack(padx=12,pady=12)
        Complement_btn = customtkinter.CTkButton(master=frame, text="Get Complement!",command=Complement_part).pack(padx=12,pady=12)
        Reverse_btn = customtkinter.CTkButton(master=frame, text="Get Reverse!", command=Reverse_part).pack(padx=12,pady=12)
        Reverse_Complement_btn = customtkinter.CTkButton(master=frame, text="Get Reverse Complement!", command=Reverse_Complement_part).pack(padx=12,pady=12)
        resultLabel.pack()



        back_btn = customtkinter.CTkButton(
            master=frame, text="Back to Home!", font=("Roboto", 20), command=back_to_home)
        back_btn.pack(pady=12, padx=10)


        
        # back_btn.grid(row=3 , column =0 , pady=12, padx=10)
        # dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog").pack()
        # enterSeqBtn = customtkinter.CTkButton(master=frame, text="Enter Seq!").pack(padx=12,pady=12)
