from tkinter import * 
import tkinter as tk
import tkinter.messagebox as mb 
import tkinter.filedialog as filedialog
import os , sys 

#name = 


""" 
    Functions 
""" 
def closeFile(): 
   
    #prompts the user with a meassagebox and checks the input 
    if mb.askyesno("Close without Saving", "Close Without Saving? ") == True: 
        #exit program 
        sys.exit()
    else: 
        pass 

def saveFile(): 
    
    # find the path to save file 
    path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    
    # saves all of the text area to the file 
    with open(path, "w" ) as file: 
        file.write(textArea.get(1.0, tk.END))
    

def openFile():
    path = filedialog.askopenfilename(title="Select a Text File", filetypes=[("Text files", "*.txt"),  ("All Files", "*.*")])
    if path:
        with open(path, 'r') as file:
            content = file.read()
            textArea.delete(1.0, tk.END)  # Clear previous content
            textArea.insert(tk.END, content)



"""
    GUI loop
""" 
# Create the main window
root = tk.Tk()
root.title("text editor") 

#open file button 
openButton = tk.Button(root, text="Open", command=openFile)
openButton.pack()

#save button 
saveButton = tk.Button(root, text="Save", command=saveFile)
saveButton.pack()

#closeFile 
closeButton =tk.Button(root, text="Close" , command=closeFile) 
closeButton.pack()

# Set the window size
root.geometry("700x600")
root.resizable(0, 0)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)


#scrollbar 
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT,fill=Y) 

textArea = Text(root,
                 yscrollcommand=scrollbar.set)
textArea.pack(fill=BOTH)

# Run the application
root.mainloop()

