import main
from SectionsAlgorithms.AlgoSec8 import *
import tkinter as tk
import tkinter.messagebox
import customtkinter
from functools import partial

# Modes: "System" (standard), "Dark", "Light"
customtkinter.set_appearance_mode("Dark")
# Themes: "blue" (standard), "green", "dark-blue"
customtkinter.set_default_color_theme("blue")


class section8GUI(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        def back_to_home():
            print("hello")
            self.destroy()
            app = main.App()
            app.mainloop()

        # configure window
        self.title("Bio Computing Algorithms GUI")
        self.geometry(f"{700}x{500}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(0, weight=1)
        # self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2, 3, 4), weight=1)
        frame = customtkinter.CTkFrame(master=self)
        frame.pack(pady=20, padx=60, fill="both", expand=True)
        label = customtkinter.CTkLabel(
            master=frame, text="Section 8:", font=("Roboto", 24))
        label.pack(pady=12, padx=10)

        seqVar1 = tk.StringVar()
        seqVar2 = tk.StringVar()
        resultLabel = customtkinter.CTkLabel(master=frame, font=(
            "Roboto", 16), text="Your Result WIll Be Printed Here!")

        enterSeqLabel = customtkinter.CTkLabel(
            master=frame, text="Enter Sequence 1:", font=("Roboto", 16)).pack()
        SeqEntry = customtkinter.CTkEntry(
            master=frame, textvariable=seqVar1, placeholder_text="Sequence").pack(padx=12, pady=12)
        subseqLabel = customtkinter.CTkLabel(
            master=frame, text="Enter Sequence 2:", font=("Roboto", 16)).pack()
        subseqEntry = customtkinter.CTkEntry(
            master=frame, textvariable=seqVar2, placeholder_text="len").pack(padx=12, pady=12)

        distPartial = partial(dist, seqVar1, seqVar2, resultLabel)
        overlapbtn = customtkinter.CTkButton(
            master=frame, text="Get Distance!", command=distPartial).pack(padx=12, pady=12)

        resultLabel.pack()

        back_btn = customtkinter.CTkButton(
            master=frame, text="Back to Home!", font=("Roboto", 20), command=back_to_home)
        back_btn.pack(pady=12, padx=10)
        # back_btn.grid(row=3 , column =0 , pady=12, padx=10)
