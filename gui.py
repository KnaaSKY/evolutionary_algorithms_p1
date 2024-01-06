from tkinter import *
from tkinter import messagebox

def submit():
    try:
        start_range = float(entrybox.get())
        end_range = float(entrybox2.get())
        precision = float(entrybox3.get())
        num_individuals = int(entrybox4.get())
        num_epochs = int(entrybox5.get())

        print("Start Range:", start_range)
        print("End Range:", end_range)
        print("Precision:", precision)
        print("Number of Individuals:", num_individuals)
        print("Number of Epochs:", num_epochs)

    except ValueError as e:
        messagebox.showerror("Error", f"Invalid input: {str(e)}")

window = Tk()
window.geometry("600x900")
window.title("evolutionary algorithms")
window.config(background="#3b3c3d")
icon = PhotoImage(file='DNA-Icon-Graphics-4217002-1.png')
window.iconphoto(True, icon)




# Dodaj etykietę (Label) dla opisu
label_description = Label(
    window,
    text="Enter start of the range:",
    font=('Times New Roman', 14, 'bold'),  # Przykładowa ładniejsza czcionka
    bg="#3b3c3d",
    fg='#f6f7df',
)
label_description.pack()

# Dodaj pole Entry
entrybox = Entry(
    window,
    font=('Calibri', 16, 'bold'),
    bg="#2b2b2a",
    fg='#f6f7df',
)
entrybox.pack(pady=7)

label_description1 = Label(
    window,
    text="Enter end of the range:",
    font=('Times New Roman', 14, 'bold'),  # Przykładowa ładniejsza czcionka
    bg="#3b3c3d",
    fg='#f6f7df',
)
label_description1.pack()

# Dodaj pole Entry
entrybox2 = Entry(
    window,
    font=('Calibri', 16, 'bold'),
    bg="#2b2b2a",
    fg='#f6f7df',
)
entrybox2.pack(pady=10)
label_description3 = Label(
    window,
    text="Enter precission:",
    font=('Times New Roman', 14, 'bold'),  # Przykładowa ładniejsza czcionka
    bg="#3b3c3d",
    fg='#f6f7df',
)
label_description3.pack()

# Dodaj pole Entry
entrybox3 = Entry(
    window,
    font=('Calibri', 16, 'bold'),
    bg="#2b2b2a",
    fg='#f6f7df',
)
entrybox3.pack(pady=10)
label_description4 = Label(
    window,
    text="Enter amount of individuals:",
    font=('Times New Roman', 14, 'bold'),  # Przykładowa ładniejsza czcionka
    bg="#3b3c3d",
    fg='#f6f7df',
)
label_description4.pack()

# Dodaj pole Entry
entrybox4 = Entry(
    window,
    font=('Calibri', 16, 'bold'),
    bg="#2b2b2a",
    fg='#f6f7df',
)
entrybox4.pack(pady=10)
label_description5 = Label(
    window,
    text="Enter amount of epochs:",
    font=('Times New Roman', 14, 'bold'),  # Przykładowa ładniejsza czcionka
    bg="#3b3c3d",
    fg='#f6f7df',
)
label_description5.pack()

# Dodaj pole Entry
entrybox5 = Entry(
    window,
    font=('Calibri', 16, 'bold'),
    bg="#2b2b2a",
    fg='#f6f7df',
)
entrybox5.pack(pady=10)
submit_button = Button(window,
                       text="Submit",
                       font=('Times New Roman', 10, 'bold'),
                       command=submit,
                       width=12)
submit_button.pack(pady="10")

window.mainloop()
