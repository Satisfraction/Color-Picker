import tkinter as tk
import tkinter.colorchooser as cc

class ColorPickerGUI:
    def __init__(self, master):
        self.master = master
        master.title("Farbwähler")

        self.color_label = tk.Label(master, text="Klicken Sie auf das Farbfeld, um eine Farbe auszuwählen")
        self.color_label.pack(pady=10)

        self.color_button = tk.Button(master, bg="#FFFFFF", width=10, height=5, command=self.choose_color)
        self.color_button.pack(pady=10)

        self.hex_label = tk.Label(master, text="")
        self.hex_label.pack(pady=10)

        self.copy_button = tk.Button(master, text="Kopieren", command=self.copy_hex)
        self.copy_button.pack(pady=10)

    def choose_color(self):
        color = cc.askcolor()[1]
        if color:
            self.color_button.config(bg=color)
            self.hex_label.config(text=color)

    def copy_hex(self):
        hex_code = self.hex_label.cget("text")
        if hex_code:
            self.master.clipboard_clear()
            self.master.clipboard_append(hex_code)

root = tk.Tk()
picker = ColorPickerGUI(root)
root.mainloop()
