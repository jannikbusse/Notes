import apihandler
import tkinter as tk
import parser
import text
import contentpanel

thread = "my thread"


def shift_return_pressed(event):
    channel, content = parser.parse_note(textInput.get("1.0","end-1c").strip())    
    textInput.delete('1.0', "end")
    print("send " + content +" in " + channel)
    apihandler.send_note(thread, content, channel)
    channelManager.update_views()
    





def esc_pressed(event):
    print("esc")
    exit()

root = tk.Tk()
root.attributes('-type', 'splash')


window = tk.Frame(root,background="black")
window.pack(fill=None, expand=False)


textInput = tk.Text(window, height=1, width=30, font=("Helvetica", 32))
textInput.bind("<Escape>", esc_pressed)
textInput.bind("<Return>", shift_return_pressed)

textInput.focus()
textInput.pack()

displayWindow = tk.Toplevel(window, width = 600, height = 600)
displayWindow.propagate(0)



channelManager = contentpanel.ContainerManager(displayWindow)
channelManager.update_views()

window.mainloop()

#apihandler.send_note("my thread", "my content", "my channel")
#notes = apihandler.get_notes("my thread")
#print(notes)