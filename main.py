import tkinter
import customtkinter

#wep1 = utils.Weapon(64, 64, True, ['overflow', 'rewind rounds'])
#print(wep1.magazine)
#print(wep1.reserves)
#print(wep1.overflow)
#print(wep1.perks)
#print(wep1.max_magazine)

# System Settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")

# App frame
calculator = customtkinter.CTk()
calculator.geometry("720x480")
calculator.title("Destiny 2 Ammo Perk Calculator")

# UI Elements
mag_capacity_title = customtkinter.CTkLabel(calculator, text="Magazine Capacity")
mag_capacity_title.pack(padx=10, pady=10)

mag_capacity_var = tkinter.StringVar()
mag_text = customtkinter.CTkEntry(calculator, width=350, height=40, textvariable=mag_capacity_var)
mag_text.pack(padx=10, pady=10)

#calculate = customtkinter.CTkButton(calculator, text="calculate", command=)

calculator.mainloop()
