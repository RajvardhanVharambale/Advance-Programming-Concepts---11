
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
from tkinter import font

# Main window
root = tk.Tk()
root.title("Untitled - Notepad")
root.geometry("700x500")

current_file = None

# Text area
text_area = tk.Text(root, undo=True, wrap="word")
text_area.pack(side="left", fill="both", expand=True)

# Scrollbar
scrollbar = tk.Scrollbar(root, command=text_area.yview)
scrollbar.pack(side="right", fill="y")
text_area.config(yscrollcommand=scrollbar.set)


# Update window title
def update_title():
    if current_file:
        root.title(current_file + " - Notepad")
    else:
        root.title("Untitled - Notepad")


# New file
def new_file():
    global current_file

    if text_area.get("1.0", "end-1c"):
        answer = messagebox.askyesnocancel(
            "Notepad", "Do you want to save changes?"
        )

        if answer is None:
            return
        elif answer:
            if not save_file():
                return

    text_area.delete("1.0", tk.END)
    current_file = None
    update_title()


# Open file
def open_file():
    global current_file

    file_path = filedialog.askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )

    if file_path:
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()

            text_area.delete("1.0", tk.END)
            text_area.insert("1.0", content)
            current_file = file_path
            update_title()

        except (OSError, UnicodeError) as error:
            messagebox.showerror("Error", f"Cannot open file:\n{error}")


# Save file
def save_file():
    global current_file

    if current_file is None:
        return save_as_file()

    try:
        with open(current_file, "w", encoding="utf-8") as file:
            file.write(text_area.get("1.0", "end-1c"))

        update_title()
        return True

    except OSError as error:
        messagebox.showerror("Error", f"Cannot save file:\n{error}")
        return False


# Save As
def save_as_file():
    global current_file

    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )

    if not file_path:
        return False

    old_file = current_file
    current_file = file_path

    if save_file():
        return True

    current_file = old_file
    return False


# Cut, Copy, Paste and Select All
def cut_text():
    text_area.event_generate("<<Cut>>")

def copy_text():
    text_area.event_generate("<<Copy>>")

def paste_text():
    text_area.event_generate("<<Paste>>")

def select_all(event=None):
    text_area.tag_add("sel", "1.0", "end-1c")
    text_area.mark_set("insert", "1.0")
    text_area.see("insert")
    return "break"


# Word Wrap
def toggle_word_wrap():
    if word_wrap_var.get():
        text_area.config(wrap="word")
    else:
        text_area.config(wrap="none")


# Change font size
def change_font_size():
    size = simpledialog.askinteger(
        "Font Size",
        "Enter font size (8-48):",
        minvalue=8,
        maxvalue=48
    )

    if size:
        text_font.config(size=size)


# About
def about_notepad():
    messagebox.showinfo(
        "About Notepad",
        "Simple Notepad\nCreated using Python and Tkinter."
    )


# Menu bar
menu_bar = tk.Menu(root)

# File menu
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=new_file, accelerator="Ctrl+N")
file_menu.add_command(label="Open", command=open_file, accelerator="Ctrl+O")
file_menu.add_command(label="Save", command=save_file, accelerator="Ctrl+S")
file_menu.add_command(label="Save As", command=save_as_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.destroy)
menu_bar.add_cascade(label="File", menu=file_menu)

# Edit menu
edit_menu = tk.Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Cut", command=cut_text, accelerator="Ctrl+X")
edit_menu.add_command(label="Copy", command=copy_text, accelerator="Ctrl+C")
edit_menu.add_command(label="Paste", command=paste_text, accelerator="Ctrl+V")
edit_menu.add_command(label="Select All", command=select_all, accelerator="Ctrl+A")
menu_bar.add_cascade(label="Edit", menu=edit_menu)

# Format menu
format_menu = tk.Menu(menu_bar, tearoff=0)
word_wrap_var = tk.BooleanVar(value=True)
format_menu.add_checkbutton(
    label="Word Wrap",
    variable=word_wrap_var,
    command=toggle_word_wrap
)
format_menu.add_command(label="Font Size", command=change_font_size)
menu_bar.add_cascade(label="Format", menu=format_menu)

# Help menu
help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About Notepad", command=about_notepad)
menu_bar.add_cascade(label="Help", menu=help_menu)

root.config(menu=menu_bar)

# Font settings
text_font = font.Font(family="Consolas", size=12)
text_area.config(font=text_font)

# Keyboard shortcuts
root.bind("<Control-n>", lambda event: new_file())
root.bind("<Control-o>", lambda event: open_file())
root.bind("<Control-s>", lambda event: save_file())
root.bind("<Control-a>", select_all)

# Start application
text_area.focus_set()
root.mainloop()
