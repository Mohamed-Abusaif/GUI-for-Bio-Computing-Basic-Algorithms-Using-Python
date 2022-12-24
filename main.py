import section8
import section7
import section6
import section5
import section4
import section3
import section2
import section1
import suffix
import tkinter
import tkinter.messagebox
import customtkinter

# Modes: "System" (standard), "Dark", "Light"
customtkinter.set_appearance_mode("Dark")
# Themes: "blue" (standard), "green", "dark-blue"
customtkinter.set_default_color_theme("blue")


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("Bio Computing Algorithms GUI")
        self.geometry(f"{800}x{580}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(
            self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        # self.sidebar_frame.grid_rowconfigure(4, weight=1)

        self.logo_label = customtkinter.CTkLabel(
            self.sidebar_frame, text="Choose Section:", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.sidebar_button_1 = customtkinter.CTkButton(
            self.sidebar_frame, text="Section 1", font=("Roboto", 20), command=self.section1_scene_event)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = customtkinter.CTkButton(
            self.sidebar_frame, text="Section 2", font=("Roboto", 20), command=self.section2_scene_event)
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.sidebar_button_3 = customtkinter.CTkButton(
            self.sidebar_frame, text="Section 3", font=("Roboto", 20), command=self.section3_scene_event)
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)
        self.sidebar_button_4 = customtkinter.CTkButton(
            self.sidebar_frame, text="Section 4", font=("Roboto", 20), command=self.section4_scene_event)
        self.sidebar_button_4.grid(row=4, column=0, padx=20, pady=10)
        self.sidebar_button_5 = customtkinter.CTkButton(
            self.sidebar_frame, text="Section 5", font=("Roboto", 20), command=self.section5_scene_event)
        self.sidebar_button_5.grid(row=5, column=0, padx=20, pady=10)
        self.sidebar_button_6 = customtkinter.CTkButton(
            self.sidebar_frame, text="Section 6", font=("Roboto", 20), command=self.section6_scene_event)
        self.sidebar_button_6.grid(row=6, column=0, padx=20, pady=10)
        self.sidebar_button_7 = customtkinter.CTkButton(
            self.sidebar_frame, text="Section 7", font=("Roboto", 20), command=self.section7_scene_event)
        self.sidebar_button_7.grid(row=7, column=0, padx=20, pady=10)
        self.sidebar_button_8 = customtkinter.CTkButton(
            self.sidebar_frame, text="Section 8", font=("Roboto", 20), command=self.section8_scene_event)
        self.sidebar_button_8.grid(row=8, column=0, padx=20, pady=10)

        self.sidebar_button_9 = customtkinter.CTkButton(
            self.sidebar_frame, text="Suffix Additional Feature!", font=("Roboto", 20), command=self.suffixFeature)
        self.sidebar_button_9.grid(row=8, column=0, padx=20, pady=10)

        self.appearance_mode_label = customtkinter.CTkLabel(
            self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=9, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(
            row=10, column=0, padx=20, pady=(10, 10))

        self.scaling_label = customtkinter.CTkLabel(
            self.sidebar_frame, text="UI Scaling:", anchor="w")
        # self.scaling_label.grid(row=11, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        # self.scaling_optionemenu.grid(row=12, column=0, padx=20, pady=(10, 20))

        # self.homeLabel = customtkinter.CTkLabel(master=self , text="Welcome To Home Page" , font=("Roboto", 24)).pack()
        # # create tabview
        # self.tabview = customtkinter.CTkTabview(self, width=250)
        # self.tabview.grid(row=0, column=2, padx=(
        #     20, 0), pady=(20, 0), sticky="nsew")

        # set default values
        self.appearance_mode_optionemenu.set("Dark")
        self.scaling_optionemenu.set("100%")

    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(
            text="Type in a number:", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def sidebar_button_event(self):
        print("sidebar_button click")

    def section1_scene_event(self):
        try:
            print("section 1 event clicked")
            self.destroy()
            app = section1.section1GUI()
            app.mainloop()
        except:
            print("Scene Changed to Section 1!")

    def section2_scene_event(self):
        try:
            print("section 2 event clicked")
            self.destroy()
            app = section2.section2GUI()
            app.mainloop()
        except:
            print("Scene Changed to Section 2!")

    def section3_scene_event(self):
        try:
            print("section 3 event clicked")
            self.destroy()
            app = section3.section3GUI()
            app.mainloop()
        except:
            print("Scene Changed to Section 3!")

    def section4_scene_event(self):
        try:
            print("section 4 event clicked")
            self.destroy()
            app = section4.section4GUI()
            app.mainloop()
        except:
            print("Scene Changed to Section 4!")

    def section5_scene_event(self):
        try:
            print("section 5 event clicked")
            self.destroy()
            app = section5.section5GUI()
            app.mainloop()
        except:
            print("Scene Changed to Section 5!")

    def section6_scene_event(self):
        try:
            print("section 6 event clicked")
            self.destroy()
            app = section6.section6GUI()
            app.mainloop()
        except:
            print("Scene Changed to Section 6!")

    def section7_scene_event(self):
        try:
            print("section 7 event clicked")
            self.destroy()
            app = section7.section7GUI()
            app.mainloop()
        except:
            print("Scene Changed to Section 7!")

    def section8_scene_event(self):
        try:
            print("section 8 event clicked")
            self.destroy()
            app = section8.section8GUI()
            app.mainloop()
        except:
            print("Scene Changed to Section 8!")

    def suffixFeature(self):
        try:
            print("suffix button event clicked")
            self.destroy()
            app = suffix.suffixGUI()
            app.mainloop()
        except:
            print("Scene Changed to suffix scene!")


if __name__ == "__main__":
    app = App()
    app.mainloop()
