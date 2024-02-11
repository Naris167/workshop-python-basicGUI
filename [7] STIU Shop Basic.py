# Import necessary modules from tkinter library
from tkinter import *
from tkinter import ttk

# Initialize the main GUI window
GUI = Tk()
GUI.geometry('500x500')  # Set the size of the window
GUI.title('Stamford Shop')  # Set the title of the window

# Define fonts for use in the GUI
FONT1 = ('Angsana New', 15)
FONT2 = ('Angsana New', 20, 'bold')

# Define StringVar() variables to store user input and display results
v_expense = StringVar()  # Variable to store item name
v_price = StringVar()    # Variable to store item price
v_result_item = StringVar()  # Variable to display selected/sold item name
v_result_price = StringVar() # Variable to display item price

# Function to save the expense/item and its price
def SaveExpense():
    exp = v_expense.get()  # Get the item name from user input
    pc = float(v_price.get())  # Convert the price input to a float
    # Display the saved item and its price
    v_result_item.set(f'Saved the item: {exp}')
    v_result_price.set(f'Price: {pc:,.2f} THB')
    # Clear the input fields for the next entry
    v_expense.set('')
    v_price.set('')
    # Set focus back to the item name input field
    E1.focus()

# Functions to set the price for each item when its button is clicked
# Note: These functions have redundancy and can be improved using a single function with parameters.
def PriceRice():
    v_result_item.set(f'Selected item: Rice')
    v_result_price.set(f'Price: 25 THB per 1 kg')

def PriceCoffee():
    v_result_item.set(f'Selected item: Coffee')
    v_result_price.set(f'Price: 50 THB per 1 cup')

def PriceTaxi():
    v_result_item.set(f'Selected item: Apple')
    v_result_price.set(f'Price: 35 THB per 1 apple')

def PriceSoda():
    v_result_item.set(f'Selected item: Soda')
    v_result_price.set(f'Price: 10 THB per 1 can')

def PriceSnack():
    v_result_item.set(f'Selected item: Snack')
    v_result_price.set(f'Price: 57 THB per 1 bag')

def PriceBook():
    v_result_item.set(f'Selected item: Book')
    v_result_price.set(f'Price: 420 THB per 1 book')

# Create a frame to hold the GUI elements and center it in the main window
F1 = Frame(GUI, borderwidth=2, relief="groove")
F1.place(anchor="c", relx=.5, rely=.5)

# Create labels and input fields for item name and price
L1 = ttk.Label(F1, text='Please enter your item: ')
L1.grid(row=0, column=0, columnspan=2, sticky='E')
E1 = ttk.Entry(F1, textvariable=v_expense, font=FONT1, width=30)
E1.grid(row=0, column=2, columnspan=3)

L2 = ttk.Label(F1, text='Please enter the price (THB): ')
L2.grid(row=1, column=0, columnspan=2, sticky='E')
E2 = ttk.Entry(F1, textvariable=v_price, font=FONT1, width=30)
E2.grid(row=1, column=2, columnspan=3)

# Create the "Save" button
B1 = ttk.Button(F1, text='Save', command=SaveExpense)
B1.grid(row=2, column=1)

# Create labels to display the selected/sold item and its price
R1 = ttk.Label(F1, textvariable=v_result_item, font=FONT2, foreground='green')
R1.grid(row=3, column=0, columnspan=3)

R2 = ttk.Label(F1, textvariable=v_result_price, font=FONT2, foreground='green')
R2.grid(row=4, column=0, columnspan=3)

# Create buttons for each item. When clicked, they will display the item's price.
# Note: This section has redundancy and can be improved using a loop and a list of items and prices.
B1 = ttk.Button(F1, text='Rice', command=PriceRice)
B1.grid(row=5, column=0)

B2 = ttk.Button(F1, text='Coffee', command=PriceCoffee)
B2.grid(row=5, column=1)

B3 = ttk.Button(F1, text='Apple', command=PriceTaxi)
B3.grid(row=5, column=2)

B4 = ttk.Button(F1, text='Soda', command=PriceSoda)
B4.grid(row=6, column=0)

B5 = ttk.Button(F1, text='Snack', command=PriceSnack)
B5.grid(row=6, column=1)

B6 = ttk.Button(F1, text='Book', command=PriceBook)
B6.grid(row=6, column=2)

# Start the main GUI loop
GUI.mainloop()
