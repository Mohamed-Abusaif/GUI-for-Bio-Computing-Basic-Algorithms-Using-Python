import main
from SectionsAlgorithms.AlgoSec5 import *
import tkinter as tk
import tkinter.messagebox
import customtkinter
from functools import partial

# Modes: "System" (standard), "Dark", "Light"
customtkinter.set_appearance_mode("Dark")
# Themes: "blue" (standard), "green", "dark-blue"
customtkinter.set_default_color_theme("blue")


class section5GUI(customtkinter.CTk):
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
            master=frame, text="Section 5:", font=("Roboto", 24))
        label.pack(pady=12, padx=10)

        seqVar = tk.StringVar()
        subseqVar = tk.StringVar()
        resultLabel = customtkinter.CTkLabel(master=frame, font=(
            "Roboto", 16), text="Your Result WIll Be Printed Here!")
        lenVar = tk.StringVar()

        enterSeqLabel = customtkinter.CTkLabel(
            master=frame, text="Enter Sequence:", font=("Roboto", 16)).pack()
        SeqEntry = customtkinter.CTkEntry(
            master=frame, textvariable=seqVar, placeholder_text="Sequence").pack(padx=12, pady=12)
        enterLenLabel = customtkinter.CTkLabel(
            master=frame, text="Enter len:", font=("Roboto", 16)).pack()
        LenEntry = customtkinter.CTkEntry(
            master=frame, textvariable=lenVar, placeholder_text="len").pack(padx=12, pady=12)
        subseqLabel = customtkinter.CTkLabel(
            master=frame, text="Enter sub sequence:", font=("Roboto", 16)).pack()
        subseqEntry = customtkinter.CTkEntry(
            master=frame, textvariable=subseqVar, placeholder_text="len").pack(padx=12, pady=12)

        queryFunc = partial(query, seqVar, subseqVar, lenVar, resultLabel)
        querybtn = customtkinter.CTkButton(
            master=frame, text="query using index!", command=queryFunc).pack(padx=12, pady=12)

        resultLabel.pack()

        back_btn = customtkinter.CTkButton(
            master=frame, text="Back to Home!", font=("Roboto", 20), command=back_to_home)
        back_btn.pack(pady=12, padx=10)
        # back_btn.grid(row=3 , column =0 , pady=12, padx=10)
