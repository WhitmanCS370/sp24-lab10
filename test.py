import tkinter as tk

# Function to retrieve the selected option from the dropdown
def retrieve_option():
    selected_option = dropdown.get()
    print("Selected option:", selected_option)

# Create the main window
root = tk.Tk()
root.title("Dropdown Menu")

# Define options for the dropdown
options = ["Option 1", "Option 2", "Option 3", "Option 4"]

# Create a dropdown menu
dropdown_var = tk.StringVar(root)
dropdown_var.set(options[0])  # Set default option
dropdown = tk.OptionMenu(root, dropdown_var, *options)
dropdown.pack(padx=10, pady=10)

# Create a button to retrieve the selected option
button = tk.Button(root, text="Retrieve Option", command=retrieve_option)
button.pack(pady=5)

# Run the Tkinter event loop
root.mainloop()
