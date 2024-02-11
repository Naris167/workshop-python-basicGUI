from tkinter import *
from tkinter import ttk

def create_button(parent, text, command, row, col, alignment, colSpan):
    """
    Helper function to create a button.
    :param parent: The parent widget where the button will be placed.
    :param text: The text to be displayed on the button.
    :param command: The function to be executed when the button is clicked.
    :param row: The row position in the grid.
    :param col: The column position in the grid.
    :return: The created button.
    """
    btn = ttk.Button(parent, text=text, command=command)
    btn.grid(row=row, column=col, columnspan=colSpan, ipadx=20, ipady=10, padx=5, pady=10, sticky=alignment)
    return btn

def create_label_entry(parent, label_text, text_variable, font, row, column):
    """
    Helper function to create a label and an entry (textbox).
    :param parent: The parent widget where the label and entry will be placed.
    :param label_text: The text to be displayed on the label.
    :param text_variable: The variable to store the text input from the entry.
    :param font: The font style for the entry.
    :param row: The row position in the grid.
    :return: The created label and entry.
    """
    lbl = ttk.Label(parent, text=label_text)
    lbl.grid(row=row, column=0+column, columnspan=2, ipadx=0, ipady=10, padx=0, pady=10, sticky='E')
    entry = ttk.Entry(parent, textvariable=text_variable, font=font, width=30)
    entry.grid(row=row, column=2+column, columnspan=3, ipadx=5, ipady=0, padx=5, pady=0, sticky='W')
    return lbl, entry

# Initialize the main GUI window
GUI = Tk()
GUI.geometry('900x550')
GUI.title('Stamford Shop')

# Define fonts for text
FONT1 = ('Angsana New', 15)
FONT2 = ('Angsana New', 20, 'bold')

# Variables to store user input and results
v_expense = StringVar()  # Stores the name of the item the user wants to sell
v_price = StringVar()    # Stores the price of the item the user wants to sell
v_result_item = StringVar()  # Stores the result message about the item
v_result_price = StringVar() # Stores the result message about the price
v_money = IntVar(value=100)  # User starts with 100 THB
v_items_sold = IntVar(value=0)  # Number of items the user has sold
v_items_bought = IntVar(value=0)  # Number of items the user has bought

def SaveExpense():
    """
    Function to handle the selling of an item.
    Updates the money based on the item's price and updates the number of items sold.
    """
    exp = v_expense.get()  # Get the name of the item
    pc = float(v_price.get())  # Get the price of the item
    v_items_sold.set(v_items_sold.get() + 1)  # Increase items sold count
    v_money.set(v_money.get() + int(pc))  # Add price to user's money
    v_result_item.set(f'Sold item: {exp}')
    R1.config(foreground='black')
    v_result_price.set(f'Price: {pc:,.2f} THB')
    R2.config(foreground='green')
    v_expense.set('')  # Clear the item name input
    v_price.set('')    # Clear the price input

def buy_item(item, price, unit):
    """
    Function to handle the buying of an item.
    Checks if the user has enough money and updates the money and number of items bought accordingly.
    """
    v_result_item.set('')  # Clear previous messages
    v_result_price.set('')
    if v_money.get() >= price:
        v_money.set(v_money.get() - price)
        v_items_bought.set(v_items_bought.get() + 1)  # Increase items bought count
        v_result_item.set(f'Successfully bought {item} for {price} THB')
        R1.config(foreground='green')
    else:
        v_result_item.set(f"You don't have enough money to buy {item}")
        R1.config(foreground='red')

# Create the main frame inside the GUI window
F1 = Frame(GUI, borderwidth=2, relief="groove")
F1.place(anchor="c", relx=.5, rely=.5)

# Display user's money, items sold, and items bought with labels
money_label_text = ttk.Label(F1, text="Money: ", font=FONT2)
money_label_text.grid(row=0, column=0, ipadx=0, ipady=0, padx=0, pady=0, sticky="E")
money_label = ttk.Label(F1, textvariable=v_money, font=FONT2, foreground='blue')
money_label.grid(row=0, column=1, ipadx=0, ipady=0, padx=0, pady=0, sticky="W")
items_sold_label_text = ttk.Label(F1, text="Items Sold:", font=FONT2)
items_sold_label_text.grid(row=0, column=2, ipadx=0, ipady=0, padx=0, pady=0, sticky="E")
items_sold_label = ttk.Label(F1, textvariable=v_items_sold, font=FONT2, foreground='blue')
items_sold_label.grid(row=0, column=3, ipadx=0, ipady=0, padx=0, pady=0, sticky="W")
items_bought_label_text = ttk.Label(F1, text="Items Bought: ", font=FONT2)
items_bought_label_text.grid(row=0, column=4, columnspan=2, ipadx=20, ipady=0, padx=5, pady=0)
items_bought_label = ttk.Label(F1, textvariable=v_items_bought, font=FONT2, foreground='blue')
items_bought_label.grid(row=0, column=5, ipadx=20, ipady=0, padx=5, pady=0)

# Adding "Sell Item" label
sell_item_label = ttk.Label(F1, text="Sell Item", font=FONT2)
sell_item_label.grid(row=1, column=0, columnspan=6, ipadx=0, ipady=0, padx=0, pady=0)

# Create labels and text boxes for user to input item name and price
create_label_entry(F1, 'Please enter your item name: ', v_expense, FONT1, 2, 1)
create_label_entry(F1, 'Please enter the price (THB): ', v_price, FONT1, 3, 1)

# Create the "Sell" button
create_button(F1, 'Sell', SaveExpense, 4, 2, '', 2)

# Display result messages
R1 = ttk.Label(F1, textvariable=v_result_item, font=FONT2)
R1.grid(row=5, column=0, columnspan=6, ipadx=0, ipady=0, padx=0, pady=0)

R2 = ttk.Label(F1, textvariable=v_result_price, font=FONT2)
R2.grid(row=6, column=0, columnspan=6, ipadx=0, ipady=0, padx=0, pady=0)

# Adding "Buy Item" label
buy_item_label = ttk.Label(F1, text="Buy Item", font=FONT2)
buy_item_label.grid(row=7, column=0, columnspan=6, ipadx=0, ipady=0, padx=0, pady=0)

# Create buttons for different items to buy
items = [('Rice', 25, '1 kg'), ('Coffee', 50, '1 cup'), ('Apple', 35, '1 apple'), 
         ('Soda', 10, '1 can'), ('Snack', 57, '1 bag'), ('Book', 420, '1 book'),
         ('Sugar', 40, '1 kg'), ('Salt', 45, '1 kg'), ('Table', 4500, '1 table'),
         ('Cream', 570, '1 bottle'), ('Laptop', 42000, '1 laptop'), ('Chair', 3000, '1 Chair'), ('Candy',200,'1 Candy')]
for idx, (item, price, unit) in enumerate(items):
    create_button(F1, item, lambda item=item, price=price, unit=unit: buy_item(item, price, unit), 8 + idx//6, idx%6, "W", 1)

# Start the main GUI loop
GUI.mainloop()
