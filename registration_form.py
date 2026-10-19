import tkinter as tk
from tkinter import ttk, messagebox
import re

# District and taluka data for Maharashtra
district_talukas = {
    "Kolhapur": [
        "Karvir", "Panhala", "Hatkanangale", "Shirol",
        "Kagal", "Gadhinglaj", "Chandgad", "Radhanagari",
        "Bhudargad", "Ajra", "Gaganbawada", "Shahuwadi"
    ],
    "Pune": [
        "Haveli", "Pune City", "Mulshi", "Maval",
        "Bhor", "Velhe", "Baramati", "Indapur",
        "Daund", "Shirur", "Junnar", "Ambegaon",
        "Khed", "Purandar"
    ],
    "Sangli": [
        "Miraj", "Tasgaon", "Jat", "Walwa",
        "Palus", "Khanapur", "Atpadi", "Shirala"
    ],
    "Satara": [
        "Satara", "Karad", "Wai", "Mahabaleshwar",
        "Phaltan", "Koregaon", "Patan", "Jaoli"
    ],
    "Mumbai City": ["Mumbai City"],
    "Mumbai Suburban": ["Andheri", "Borivali", "Kurla"],
    "Nashik": [
        "Nashik", "Igatpuri", "Dindori", "Sinnar",
        "Niphad", "Yeola", "Chandwad", "Malegaon"
    ],
    "Nagpur": [
        "Nagpur Urban", "Nagpur Rural", "Kamptee",
        "Hingna", "Katol", "Ramtek", "Umred"
    ],
    "Solapur": [
        "Solapur North", "Solapur South", "Akkalkot",
        "Barshi", "Karmala", "Madha", "Pandharpur"
    ],
    "Ratnagiri": [
        "Ratnagiri", "Chiplun", "Dapoli", "Khed",
        "Guhagar", "Lanja", "Rajapur"
    ]
}


# Update taluka dropdown according to district
def update_taluka(event=None):
    selected_district = district_var.get()

    taluka_dropdown["values"] = district_talukas.get(
        selected_district, []
    )

    taluka_var.set("")


# Submit form and validate details
def submit_form():
    name = name_var.get().strip()
    mobile = mobile_var.get().strip()
    district = district_var.get()
    taluka = taluka_var.get()

    # Name validation
    if not name:
        messagebox.showerror("Error", "Please enter your name.")
        return

    if not re.fullmatch(r"[A-Za-z][A-Za-z .'-]*", name):
        messagebox.showerror(
            "Error",
            "Name should contain only letters, spaces, dots, "
            "apostrophes, or hyphens."
        )
        return

    # Indian mobile number validation
    if not re.fullmatch(r"[6-9][0-9]{9}", mobile):
        messagebox.showerror(
            "Error",
            "Enter a valid 10-digit Indian mobile number "
            "starting with 6, 7, 8, or 9."
        )
        return

    # District validation
    if not district:
        messagebox.showerror("Error", "Please select a district.")
        return

    # Taluka validation
    if not taluka:
        messagebox.showerror("Error", "Please select a taluka.")
        return

    # Display submitted information
    messagebox.showinfo(
        "Registration Successful",
        f"Name: {name}\n"
        f"Mobile Number: {mobile}\n"
        f"District: {district}\n"
        f"Taluka: {taluka}"
    )


# Clear all fields
def clear_form():
    name_var.set("")
    mobile_var.set("")
    district_var.set("")
    taluka_var.set("")

    taluka_dropdown["values"] = []
    name_entry.focus()


# Create main window
root = tk.Tk()
root.title("Registration Form")
root.geometry("450x350")
root.resizable(False, False)


# Variables
name_var = tk.StringVar()
mobile_var = tk.StringVar()
district_var = tk.StringVar()
taluka_var = tk.StringVar()


# Main frame
frame = ttk.Frame(root, padding=20)
frame.pack(fill="both", expand=True)


# Heading
ttk.Label(
    frame,
    text="REGISTRATION FORM",
    font=("Arial", 16, "bold")
).grid(row=0, column=0, columnspan=2, pady=15)


# Name field
ttk.Label(frame, text="Name:").grid(
    row=1, column=0, sticky="w", pady=8
)

name_entry = ttk.Entry(
    frame, textvariable=name_var, width=30
)
name_entry.grid(row=1, column=1, pady=8)


# Mobile number field
ttk.Label(frame, text="Mobile Number:").grid(
    row=2, column=0, sticky="w", pady=8
)

mobile_entry = ttk.Entry(
    frame, textvariable=mobile_var, width=30
)
mobile_entry.grid(row=2, column=1, pady=8)


# District dropdown
ttk.Label(frame, text="District:").grid(
    row=3, column=0, sticky="w", pady=8
)

district_dropdown = ttk.Combobox(
    frame,
    textvariable=district_var,
    values=sorted(district_talukas.keys()),
    state="readonly",
    width=27
)

district_dropdown.grid(row=3, column=1, pady=8)
district_dropdown.bind("<<ComboboxSelected>>", update_taluka)


# Taluka dropdown
ttk.Label(frame, text="Taluka:").grid(
    row=4, column=0, sticky="w", pady=8
)

taluka_dropdown = ttk.Combobox(
    frame,
    textvariable=taluka_var,
    state="readonly",
    width=27
)

taluka_dropdown.grid(row=4, column=1, pady=8)


# Buttons
button_frame = ttk.Frame(frame)
button_frame.grid(
    row=5, column=0, columnspan=2, pady=20
)

ttk.Button(
    button_frame,
    text="Submit",
    command=submit_form
).pack(side="left", padx=10)

ttk.Button(
    button_frame,
    text="Clear",
    command=clear_form
).pack(side="left", padx=10)


# Start application
name_entry.focus()
root.mainloop()