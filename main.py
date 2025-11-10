#imports
from tkinter import * 
import tkinter as tk
import tkinter.messagebox as mb 
import tkinter.filedialog as filedialog
import os , sys 

""" 
    Functions 
""" 
def closeFile(): 
   
    #prompts the user with a meassagebox and checks the input 
    if mb.askyesno("Close without Saving", "Close Without Saving? ") == True: 
        #exit program 
        sys.exit()
    else: 
        #returns to code 
        pass 

def saveFile(): 
    
    # find the path to save file 
    path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    
    # saves all of the text area to the file 
    with open(path, "w" ) as file: 
        file.write(textArea.get(1.0, tk.END))
    

def openFile():
    #asks the user to open file 
    path = filedialog.askopenfilename(title="Select a Text File", filetypes=[("Text files", "*.txt"),  ("All Files", "*.*")])
    
    #if Selected it will open the file 
    if path:
        with open(path, 'r') as file:
            content = file.read()
            textArea.delete(1.0, tk.END)  # Clear previous content
            textArea.insert(tk.END, content)

#switch between light and dark mode 
def colourMode(): 
 #   if 
    global mode 
    if mode == "light": 
        mode = "dark"
        textArea.config(bg="#242528", fg="white", insertbackground="white")
        colourButton.config(text="dark")
    else:           
        mode = "light"
        textArea.config(bg="white", fg="black", insertbackground="black")
        colourButton.config(text="light")






#initialise the colout mode to be light mode 
mode = "light" 
"""
    GUI loop
""" 
# Create the main window
root = tk.Tk()
root.title("text editor") 

# Set the window size
root.geometry("700x600")
root.resizable(0, 0)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

#button frame 
buttonFrame = tk.Frame(root, height=50)
buttonFrame.pack(side=TOP, fill=X, pady=5)

#open file button 
openButton = tk.Button(buttonFrame,text="Open", command=openFile)
openButton.pack( side=LEFT, padx=10)

#save button 
saveButton = tk.Button(buttonFrame, text="Save", command=saveFile)
saveButton.pack(side =LEFT , padx=10)

#closeFile 
closeButton =tk.Button(buttonFrame, text="Close" , command=closeFile) 
closeButton.pack(side=LEFT , padx=10)

#colour button 
colourButton = tk.Button(buttonFrame, text=mode , command=colourMode)
colourButton.pack(side=LEFT, padx=10)

#scrollbar 
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT,fill=Y) 

#draws a textbox to screen 
textArea = Text(root, yscrollcommand=scrollbar.set, bg="white" , fg="black", insertbackground="black")
textArea.pack(fill=BOTH, expand= True)

# Run the application
root.mainloop()

