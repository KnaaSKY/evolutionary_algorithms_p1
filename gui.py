from tkinter import *
from tkinter import messagebox
from main import evolutionary_algorithm


def submit():
    try:
        a = float(entrybox.get())
        b = float(entrybox2.get())
        power_number_intervals = float(entrybox3.get())
        individual_amount = int(entrybox4.get())
        individuals_best_amount = int(entrybox5.get())
        epochs_amount = int(entrybox6.get())
        return a, b, power_number_intervals, individual_amount, individuals_best_amount, epochs_amount
    except ValueError as e:
        messagebox.showerror("Error", f"Invalid input: {str(e)}")


def execute_evolutionary_algorithm():
    try:
        values = submit()
        if values is not None:
            a, b, power_number_intervals, individual_amount, individuals_best_amount, epochs_amount = values
            evolutionary_algorithm(a, b, power_number_intervals, individual_amount, individuals_best_amount)
    except ValueError as e:
        messagebox.showerror("Error", f"Invalid input: {str(e)}")
    except TypeError as e:
        messagebox.showerror("Error", f"Error during execution: {str(e)}")


window = Tk()
window.geometry("600x900")
window.title("evolutionary algorithms")
window.config(background="#3b3c3d")
icon = PhotoImage(file='DNA-Icon-Graphics-4217002-1.png')
window.iconphoto(True, icon)


def create_entry_label_pair(description, row):
    label = Label(
        window,
        text=description,
        font=('Calibri', 14),
        bg="#3b3c3d",
        fg='#f6f7df',
    )
    label.grid(row=row, column=0, pady=5, padx=5, sticky=W)

    entry = Entry(
        window,
        font=('Calibri', 12, 'bold'),
        bg="#2b2b2a",
        fg='#f6f7df',
    )
    entry.grid(row=row, column=1, pady=5, padx=5, sticky=W)

    return entry


row_counter = 0
entrybox = create_entry_label_pair("Enter start of the range:", row_counter)
row_counter += 1
entrybox2 = create_entry_label_pair("Enter end of the range:", row_counter)
row_counter += 1
entrybox3 = create_entry_label_pair("Enter precission:", row_counter)
row_counter += 1
entrybox4 = create_entry_label_pair("Enter amount of individuals:", row_counter)
row_counter += 1
entrybox5 = create_entry_label_pair("Enter amount of best individuals:", row_counter)
row_counter += 1
entrybox6 = create_entry_label_pair("Enter amount of epochs:", row_counter)
row_counter += 1
entrybox7 = create_entry_label_pair("Enter Cross probability:", row_counter)
row_counter += 1
entrybox8 = create_entry_label_pair("Enter Mutation probability:", row_counter)
row_counter += 1
entrybox9 = create_entry_label_pair("Enter Inversion probability:", row_counter)
row_counter += 1

label_description10 = Label(
    window,
    text="Choose selection type:",
    font=('Calibri', 14),
    bg="#3b3c3d",
    fg='#f6f7df',
)
label_description10.grid(row=row_counter, column=0, pady=5, padx=5, sticky=W)
options = ["Selection of the best", "Tournament selection", "Roulette selection"]
variable = StringVar(window)
variable.set(options[0])
option_menu = OptionMenu(window, variable, *options)
option_menu.config(
    font=('Calibri', 12),
    bg="#2b2b2a",
    fg='#f6f7df',
    activebackground="#2b2b2a",
    activeforeground='#f6f7df',
    width=17,
    bd=0,
    highlightthickness=0
)
option_menu.grid(row=row_counter, column=1, pady=5, padx=1, sticky=W)
row_counter += 1

label_description11 = Label(
    window,
    text="Choose mutation type:",
    font=('Calibri', 14),
    bg="#3b3c3d",
    fg='#f6f7df',
)
label_description11.grid(row=row_counter, column=0, pady=5, padx=5, sticky=W)
options1 = ["Inversion", "Crossover", "Mutation", "Edge mutation", "One-point mutation", "Two-point mutation"]
variable = StringVar(window)
variable.set(options1[0])
option_menu1 = OptionMenu(window, variable, *options1)
option_menu1.config(
    font=('Calibri', 12),
    bg="#2b2b2a",
    fg='#f6f7df',
    activebackground="#2b2b2a",
    activeforeground='#f6f7df',
    width=17,
    bd=0,
    highlightthickness=0

)
option_menu1.grid(row=row_counter, column=1, pady=5, padx=1, sticky=W)
row_counter += 1

submit_button = Button(window,
                       text="Submit",
                       font=('Calibri', 10),
                       command=execute_evolutionary_algorithm,
                       width=12,
                       )
submit_button.grid(row=row_counter, column=0, columnspan=2, pady=10)

window.mainloop()
