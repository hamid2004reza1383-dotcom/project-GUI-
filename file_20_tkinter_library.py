import tkinter as tk
from tkinter import messagebox


root = tk.Tk()
root.geometry('1366x768')
#root.attributes('-fullscreen' , True)

# function to read txt file
def read_file():
    file_name = entry_address.get()
    try:
        with open(file_name , 'r') as file:
            data = file.read()
    except FileNotFoundError:
        messagebox.showerror('ERROR' , 
                             'file not found or invalid file address')
    except Exception as e:
        messagebox.showerror('ERROR' , e)
    else:
        text.delete('1.0' , tk.END)
        text.insert('1.0' , data)
    finally:
        file.close()        
    
    
# input
label_address = tk.Label(
    root,
    text = 'txt  file address',
    font = ('Arial' , 20)
    )
label_address.pack(pady = 50)
entry_address = tk.Entry(
    root,
    font = ('arial' , 20)
    )
entry_address.pack(pady = 20)


# read file
button = tk.Button(
    root,
    font = ('Arial' , 20),
    text = 'read file',
    command = read_file
    )
button.pack(pady = 20)

# text
text = tk.Text(
    root,
    font = ('Arial' , 15),
    height = 50,
    width = 150
    )
text.pack(pady = 50)
root.mainloop()














































