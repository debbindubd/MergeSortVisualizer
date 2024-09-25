import fitz
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog


class PDFViewer:
    def __init__(self, root):
        self.canvas = None
        self.root = root
        self.root.title("PDF Viewer")

        # Create a frame to hold the PDF viewer
        self.pdf_frame = ttk.Frame(self.root)
        self.pdf_frame.pack(fill=tk.BOTH, expand=True)

        # Create a toolbar with a button to open a file
        self.toolbar = ttk.Frame(self.root)
        self.toolbar.pack(side=tk.TOP, fill=tk.X)

        self.open_button = ttk.Button(self.toolbar, text="Open", command=self.open_file)
        self.open_button.pack(side=tk.LEFT)

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("PDF files", "img/MergeSortReport.pdf")])

        if file_path:
            # Open the PDF file with PyMuPDF
            self.doc = fitz.open(file_path)

            # Create a canvas to display the PDF
            self.canvas = tk.Canvas(self.pdf_frame)
            self.canvas.pack(fill=tk.BOTH, expand=True)

            # Display the first page of the PDF
            self.display_page(0)

    def display_page(self, page_num):
        # Get the page from the PyMuPDF document
        page = self.doc[page_num]

        # Render the page as an image
        pix = page.getPixmap(alpha=False)

        # Convert the image to a tkinter PhotoImage
        img = tk.PhotoImage(data=pix.getImageData("ppm"), master=self.root)

        # Display the image on the canvas
        self.canvas.create_image(0, 0, anchor=tk.NW, image=img)

        # Keep a reference to the image to prevent garbage collection
        self.canvas.image = img


# Create the root window
root = tk.Tk()

# Create the PDFViewer object
pdf_viewer = PDFViewer(root)

# Run the main event loop
root.mainloop()
