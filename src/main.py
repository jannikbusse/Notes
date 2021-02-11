from tkinter import *
import keyboard

class App(Tk()):

    showing = True

    def __init__(self, parent):
        super().__init__()
        self.geometry("800x600")
        self.title("Main frame")

        self.editor = TK.Text(self)
        self.editor.pack()
        self.editor.focus_set()

        keyboard.add_hotkey("ctrl+j", self.hotkey_pressed)

        def hotkey_pressed(self):
            self.update()
            
            if showing:
                self.withdraw()
            else:
                self.deiconify()

            showing = not showing

if __name__ == "__main__":
    print("starting....")
    App().mainloop()
