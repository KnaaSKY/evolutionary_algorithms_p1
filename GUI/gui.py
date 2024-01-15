from tkinter import *
from tkinter import ttk, messagebox
from main import evolutionary_algorithm
import customtkinter



def submit():
    try:
        minimisation = False
        selection_type = variable.get()
        if selection_type == "Selection of the best":
            selection_type = 1
        elif selection_type == "Tournament selection":
            selection_type = 2
        elif selection_type == "Roulette selection":
            selection_type = 3
        mutation_type = variable1.get()
        if mutation_type == "One-point mutation":
            mutation_type = 1
        elif mutation_type == "Two-point mutation":
            mutation_type = 2
        elif mutation_type == "Edge mutation":
            mutation_type = 3
        crossover_type = variable3.get()
        if crossover_type == "one-point cross":
            crossover_type = 1
        if crossover_type == "two-point cross":
            crossover_type = 2
        if crossover_type == "homogeneous cross":
            crossover_type = 3
        optm = variable5.get()
        if optm == "minimisation":
            minimisation = True
        variable_amount = int(entrybox11.get())
        a = float(entrybox.get())
        b = float(entrybox2.get())
        power_number_intervals = int(entrybox3.get())
        individual_amount = int(entrybox4.get())
        individual_selection_amount = int(entrybox5.get())
        epochs_amount = int(entrybox6.get())
        crossover_probability = float(entrybox7.get())
        mutation_probability = float(entrybox8.get())
        inversion_probability = float(entrybox9.get())
        individual_elitism_amount = int(entrybox10.get())
        return variable_amount, a, b, power_number_intervals, individual_amount, individual_selection_amount, \
            individual_elitism_amount, epochs_amount, selection_type, mutation_type, crossover_type, \
            crossover_probability, mutation_probability, inversion_probability, minimisation
    except ValueError as e:
        messagebox.showerror("Error", f"Invalid input: {str(e)}")


def execute_evolutionary_algorithm():
    try:
        values = submit()
        if values is not None:
            variable_amount, a, b, power_number_intervals, individual_amount, individual_selection_amount, \
                individual_elitism_amount, epochs_amount, selection_type, mutation_type, crossover_type, \
                crossover_probability, mutation_probability, inversion_probability, minimisation = values
            the_best_individuals=evolutionary_algorithm(variable_amount, a, b, power_number_intervals, individual_amount,
                                   individual_selection_amount,
                                   individual_elitism_amount, epochs_amount, selection_type, mutation_type,
                                   crossover_type,
                                   crossover_probability, mutation_probability, inversion_probability, minimisation)
            display_result_window(the_best_individuals)
    except ValueError as e:
        messagebox.showerror("Error", f"Invalid input: {str(e)}")
    except TypeError as e:
        messagebox.showerror("Error", f"Error during execution: {str(e)}")

def display_result_window(the_best_individuals):
    new_window = Toplevel()
    new_window.geometry("300x300")
    new_window.config(background="#3b3c3d")
    new_window.title("Result")
    individuals = list(the_best_individuals.values())
    our_individual = individuals[-1]
    label1 = Label(new_window, background="#3b3c3d", fg="white", text="The result: ")
    label1.pack()
    for i in our_individual.chromosome_values:
        label = Label(new_window, background="#3b3c3d", fg = "white" ,text = str(i))
        label.pack()
    label2 = Label(new_window, background="#3b3c3d", fg="white", text="Fitness function: " +str(our_individual.fitness_function_value))
    label2.pack()
    new_window.mainloop()

window = customtkinter.CTk()
window.geometry("500x700")
window.title("Evolutionary Algorithms")
window.config(background="#3b3c3d")
# icon = PhotoImage(file='kwadrat.png')
# window.iconphoto(True, icon)

# Ustawienie stylu dla list rozwijanych
style = ttk.Style()
style.configure('TCombobox', padding=2, relief="flat", borderwidth=5, highlightthickness=0)
style.map('TCombobox', fieldbackground=[('readonly', '#2b2b2a')])

# Ustawienie stylu dla pól Entry
style.configure('TEntry', padding=2, relief="flat", borderwidth=5, highlightthickness=0)
style.map('TEntry', fieldbackground=[('readonly', '#2b2b2a')])


def create_entry_label_pair(description, row):
    label = Label(
        window,
        text=description,
        font=('Calibri', 14),
        bg="#3b3c3d",
        fg='#f6f7df',
    )
    label.grid(row=row, column=0, pady=5, padx=10, sticky=E)

    entry = Entry(
        window,
        font=('Calibri', 12, 'bold'),
        bg="#2b2b2a",
        fg='#f6f7df',
    )
    entry.grid(row=row, column=1, pady=5, padx=10, sticky=W)

    return entry


row_counter = 0
entrybox11 = create_entry_label_pair("amount of variables:", row_counter)
row_counter += 1
entrybox = create_entry_label_pair("start of the range:", row_counter)
row_counter += 1
entrybox2 = create_entry_label_pair("end of the range:", row_counter)
row_counter += 1
entrybox3 = create_entry_label_pair("precision:", row_counter)
row_counter += 1
entrybox4 = create_entry_label_pair("amount of individuals:", row_counter)
row_counter += 1
entrybox5 = create_entry_label_pair("amount of best individuals:", row_counter)
row_counter += 1
entrybox10 = create_entry_label_pair("elite individuals amount:", row_counter)
row_counter += 1
entrybox6 = create_entry_label_pair("amount of epochs:", row_counter)
row_counter += 1
entrybox7 = create_entry_label_pair("crossing probability:", row_counter)
row_counter += 1
entrybox8 = create_entry_label_pair("mutation probability:", row_counter)
row_counter += 1
entrybox9 = create_entry_label_pair("inversion probability:", row_counter)
row_counter += 1

label_description10 = Label(
    window,
    text="selection type:",
    font=('Calibri', 14),
    bg="#3b3c3d",
    fg='#f6f7df',
)
label_description10.grid(row=row_counter, column=0, pady=5, padx=10, sticky=E)
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
option_menu.grid(row=row_counter, column=1, pady=5, padx=10, sticky=W)

row_counter += 1
label_description12 = Label(
    window,
    text="crossing type:",
    font=('Calibri', 14),
    bg="#3b3c3d",
    fg='#f6f7df',
)
label_description12.grid(row=row_counter, column=0, pady=5, padx=10, sticky=E)
options = ["one-point cross", "two-point cross", "homogeneous cross"]
variable3 = StringVar(window)
variable3.set(options[0])
option_menu = OptionMenu(window, variable3, *options)
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
option_menu.grid(row=row_counter, column=1, pady=5, padx=10, sticky=W)

row_counter += 1
label_description11 = Label(
    window,
    text="mutation type:",
    font=('Calibri', 14),
    bg="#3b3c3d",
    fg='#f6f7df',
)
label_description11.grid(row=row_counter, column=0, pady=5, padx=10, sticky=E)
options1 = ["One-point mutation", "Two-point mutation", "Edge mutation"]
variable1 = StringVar(window)
variable1.set(options1[0])
option_menu1 = OptionMenu(window, variable1, *options1)
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
option_menu1.grid(row=row_counter, column=1, pady=5, padx=10, sticky=W)

row_counter += 1
label_description15 = Label(
    window,
    text="minimisation:",
    font=('Calibri', 14),
    bg="#3b3c3d",
    fg='#f6f7df',
)
label_description15.grid(row=row_counter, column=0, pady=5, padx=10, sticky=E)
options = ["minimisation", "maximisation"]
variable5 = StringVar(window)
variable5.set(options[0])
option_menu = OptionMenu(window, variable5, *options)
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
option_menu.grid(row=row_counter, column=1, pady=5, padx=10, sticky=E)
row_counter += 1
submit_button = Button(window,
                       text="Submit",
                       font=('Calibri', 10),
                       command=execute_evolutionary_algorithm,
                       width=12,
                       )
submit_button.grid(row=row_counter, column=1, columnspan=2, pady=10, padx=20)

x_offset = (window.winfo_screenwidth() - window.winfo_reqwidth()) // 2
y_offset = (window.winfo_screenheight() - window.winfo_reqheight()) // 2
window.geometry("+{}+{}".format(x_offset, y_offset))

window.mainloop()
