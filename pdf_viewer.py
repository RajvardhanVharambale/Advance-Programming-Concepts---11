
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import fitz
import os
import sys
import subprocess
import tempfile


class PDFViewer:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF Viewer")
        self.root.geometry("1000x700")

        self.pdf_document = None
        self.pdf_path = None
        self.page_number = 0
        self.zoom = 1.0
        self.page_image = None
        self.render_job = None

        # Menu bar
        menu_bar = tk.Menu(root)

        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(
            label="Open PDF", command=self.open_pdf, accelerator="Ctrl+O"
        )
        file_menu.add_command(
            label="Save a Copy", command=self.save_copy, accelerator="Ctrl+S"
        )
        file_menu.add_separator()
        file_menu.add_command(label="Print", command=self.print_pdf)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=root.destroy)
        menu_bar.add_cascade(label="File", menu=file_menu)

        view_menu = tk.Menu(menu_bar, tearoff=0)
        view_menu.add_command(label="Zoom In", command=self.zoom_in)
        view_menu.add_command(label="Zoom Out", command=self.zoom_out)
        view_menu.add_command(label="Actual Size", command=self.actual_size)
        view_menu.add_command(label="Fit Width", command=self.fit_width)
        menu_bar.add_cascade(label="View", menu=view_menu)

        help_menu = tk.Menu(menu_bar, tearoff=0)
        help_menu.add_command(label="About", command=self.about)
        menu_bar.add_cascade(label="Help", menu=help_menu)

        root.config(menu=menu_bar)

        # Toolbar
        toolbar = tk.Frame(root, bg="#eeeeee", padx=8, pady=8)
        toolbar.pack(fill="x")

        tk.Button(toolbar, text="Open PDF", command=self.open_pdf).pack(
            side="left", padx=3
        )
        tk.Button(toolbar, text="Save Copy", command=self.save_copy).pack(
            side="left", padx=3
        )
        tk.Button(toolbar, text="Print", command=self.print_pdf).pack(
            side="left", padx=3
        )

        tk.Button(toolbar, text="−", width=3, command=self.zoom_out).pack(
            side="left", padx=(15, 2)
        )
        tk.Button(toolbar, text="+", width=3, command=self.zoom_in).pack(
            side="left", padx=2
        )
        tk.Button(toolbar, text="Fit Width", command=self.fit_width).pack(
            side="left", padx=3
        )

        # PDF filename at the top
        self.filename_label = tk.Label(
            root, text="No PDF opened", anchor="w",
            padx=10, pady=6, bg="white"
        )
        self.filename_label.pack(fill="x")

        # Main viewing area with scrollbars
        viewer_frame = tk.Frame(root, bg="#d6d6d6")
        viewer_frame.pack(fill="both", expand=True)

        self.canvas = tk.Canvas(
            viewer_frame, bg="#d6d6d6", highlightthickness=0
        )
        vertical_scroll = tk.Scrollbar(
            viewer_frame, orient="vertical", command=self.canvas.yview
        )
        horizontal_scroll = tk.Scrollbar(
            viewer_frame, orient="horizontal", command=self.canvas.xview
        )

        self.canvas.configure(
            yscrollcommand=vertical_scroll.set,
            xscrollcommand=horizontal_scroll.set
        )

        vertical_scroll.pack(side="right", fill="y")
        horizontal_scroll.pack(side="bottom", fill="x")
        self.canvas.pack(side="left", fill="both", expand=True)

        # Bottom page navigation bar
        bottom = tk.Frame(root, padx=8, pady=8)
        bottom.pack(fill="x")

        tk.Button(
            bottom, text="◀ Previous", command=self.previous_page
        ).pack(side="left", padx=4)

        self.page_label = tk.Label(
            bottom, text="Page 0 of 0"
        )
        self.page_label.pack(side="left", padx=12)

        tk.Button(
            bottom, text="Next ▶", command=self.next_page
        ).pack(side="left", padx=4)

        self.zoom_label = tk.Label(bottom, text="Zoom: 100%")
        self.zoom_label.pack(side="right", padx=10)

        # Keyboard shortcuts
        root.bind("<Control-o>", lambda event: self.open_pdf())
        root.bind("<Control-s>", lambda event: self.save_copy())
        root.bind("<Control-plus>", lambda event: self.zoom_in())
        root.bind("<Control-minus>", lambda event: self.zoom_out())

        self.show_message("Open a PDF file to begin.")

    def show_message(self, message):
        self.canvas.delete("all")
        self.canvas.create_text(
            350, 150, text=message, fill="#555555",
            font=("Arial", 16)
        )
        self.canvas.configure(scrollregion=(0, 0, 700, 300))

    def open_pdf(self):
        path = filedialog.askopenfilename(
            title="Open PDF",
            filetypes=[("PDF files", "*.pdf")]
        )

        if not path:
            return

        try:
            new_document = fitz.open(path)

            if new_document.page_count == 0:
                new_document.close()
                messagebox.showerror("Error", "This PDF has no pages.")
                return

            if self.pdf_document:
                self.pdf_document.close()

            self.pdf_document = new_document
            self.pdf_path = path
            self.page_number = 0
            self.zoom = 1.0

            self.filename_label.config(text=os.path.basename(path))
            self.root.title(os.path.basename(path) + " - PDF Viewer")
            self.display_page()

        except Exception as error:
            messagebox.showerror(
                "PDF Error", f"Could not open this PDF:\n{error}"
            )

    def display_page(self):
        if not self.pdf_document:
            return

        try:
            page = self.pdf_document.load_page(self.page_number)
            pixmap = page.get_pixmap(
                matrix=fitz.Matrix(self.zoom, self.zoom),
                alpha=False
            )

            mode = "RGB"
            image = Image.frombytes(
                mode, [pixmap.width, pixmap.height], pixmap.samples
            )

            self.page_image = ImageTk.PhotoImage(image)

            self.canvas.delete("all")
            self.canvas.create_image(
                10, 10, anchor="nw", image=self.page_image
            )

            self.canvas.configure(
                scrollregion=(
                    0, 0, pixmap.width + 20, pixmap.height + 20
                )
            )
            self.canvas.xview_moveto(0)
            self.canvas.yview_moveto(0)

            total_pages = self.pdf_document.page_count
            self.page_label.config(
                text=f"Page {self.page_number + 1} of {total_pages}"
            )
            self.zoom_label.config(text=f"Zoom: {int(self.zoom * 100)}%")

        except Exception as error:
            messagebox.showerror(
                "Error", f"Could not display page:\n{error}"
            )

    def next_page(self):
        if self.pdf_document and self.page_number < self.pdf_document.page_count - 1:
            self.page_number += 1
            self.display_page()

    def previous_page(self):
        if self.pdf_document and self.page_number > 0:
            self.page_number -= 1
            self.display_page()

    def zoom_in(self):
        if self.pdf_document and self.zoom < 3.0:
            self.zoom = min(3.0, self.zoom + 0.2)
            self.display_page()

    def zoom_out(self):
        if self.pdf_document and self.zoom > 0.4:
            self.zoom = max(0.4, self.zoom - 0.2)
            self.display_page()

    def actual_size(self):
        if self.pdf_document:
            self.zoom = 1.0
            self.display_page()

    def fit_width(self):
        if not self.pdf_document:
            return

        page = self.pdf_document.load_page(self.page_number)
        available_width = max(self.canvas.winfo_width() - 30, 200)
        self.zoom = available_width / page.rect.width
        self.zoom = min(self.zoom, 3.0)
        self.zoom = max(self.zoom, 0.1)
        self.display_page()

    def save_copy(self):
        if not self.pdf_document or not self.pdf_path:
            messagebox.showwarning("Warning", "Open a PDF first.")
            return

        path = filedialog.asksaveasfilename(
            title="Save PDF Copy",
            defaultextension=".pdf",
            initialfile=os.path.basename(self.pdf_path),
            filetypes=[("PDF files", "*.pdf")]
        )

        if path:
            try:
                self.pdf_document.save(path)
                messagebox.showinfo(
                    "Saved", "PDF copy saved successfully."
                )
            except Exception as error:
                messagebox.showerror(
                    "Save Error", f"Could not save PDF:\n{error}"
                )

    def print_pdf(self):
        if not self.pdf_path:
            messagebox.showwarning("Warning", "Open a PDF first.")
            return

        try:
            if sys.platform == "win32":
                os.startfile(self.pdf_path, "print")
            elif sys.platform == "darwin":
                subprocess.Popen(["lp", self.pdf_path])
            else:
                subprocess.Popen(["lp", self.pdf_path])

            messagebox.showinfo(
                "Print", "The print request was sent to your system."
            )
        except Exception as error:
            messagebox.showerror(
                "Print Error",
                "Could not print the PDF. Check your printer settings.\n"
                + str(error)
            )

    def about(self):
        messagebox.showinfo(
            "About PDF Viewer",
            "Simple PDF Viewer\nCreated using Python, Tkinter, "
            "PyMuPDF and Pillow."
        )


# Start the application
root = tk.Tk()
app = PDFViewer(root)
root.mainloop()
