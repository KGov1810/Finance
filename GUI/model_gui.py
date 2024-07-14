import tkinter as tk
import tkinter.font as tkfont
from abc import ABC, abstractmethod
from tkinter import ttk

from PIL import ImageTk, Image


class ModelGUI(ABC):
    def __init__(self, **kwargs):
        self.size_letter = tkfont.Font(family="Verdana", size=9, weight="bold")

        self.entries = {}

        self.model_frame = None
        self.principal_window = None
        self.label_call_result = None
        self.label_put_result = None
        self.initial_frame = None

    @abstractmethod
    def create_model_window(self):
        """Abstract function to create the window of the specific model"""
        self.model_frame = tk.Frame(self.principal_window)
        self.model_frame.pack(fill='both', expand=True)

    def show_initial_frame(self):
        """Function to go back to the main menu"""
        self.model_frame.pack_forget()
        self.initial_frame.pack(fill='both', expand=True)

    def create_label(self, row: int, column: int, sticky: str, text: str = "", rowspan: int = 1,
                     columnspan: int = 1, padx: int = 10, pady: int = 10, image: ImageTk.PhotoImage = None):
        """
        Function to create a label
        Args:
            row: row position to display
            column: column position to display
            sticky: stickiness to other component (Nord, South, East, West)
            text: text to display on the label
            rowspan: size that the label should take on the row axis
            columnspan: size that the label should take on the column axis
            padx: size of the label on x-axis
            pady: size of the label on y-axis
            image: Image to display if the label should contain an image
        Return:
            label: return the created label
        """
        label = tk.Label(self.model_frame, text=text, font=self.size_letter, image=image)
        label.grid(row=row, column=column, rowspan=rowspan, columnspan=columnspan, padx=padx, pady=pady, sticky=sticky)
        return label

    def create_entry(self, default_value: str, row: int, column: int, sticky: str,
                     padx: int = 10, pady: int = 10, font: tuple = ('Verdana', 9)):
        """
        Function to create the entries
        Args:
            default_value: default value to insert as an entry
            row: row position to display
            column: column position to display
            sticky: stickiness to other component (Nord, South, East, West)
            padx: size of the label on x-axis
            pady: size of the label on y-axis
            font: design of the text written by the user
        Return:
            entry: return the created entry
        """
        entry = tk.Entry(self.model_frame, font=font)
        entry.insert(0, default_value)
        entry.grid(row=row, column=column, padx=padx, pady=pady, sticky=sticky)
        return entry

    def create_button(self, text: str, row: int, column: int, sticky: str, command,
                      columnspan: int = 1, padx: int = 10, pady: int = 10):
        """
        Function to create a button
        Args:
            row: row position to display
            column: column position to display
            sticky: stickiness to other component (Nord, South, East, West)
            command: function to execute when the button is clicked
            text: text to display on the label
            columnspan: size that the label should take on the column axis
            padx: size of the label on x-axis
            pady: size of the label on y-axis
        Return:
            button: return the created button
        """
        button = tk.Button(self.model_frame, text=text, command=command)
        button.grid(row=row, column=column, columnspan=columnspan, padx=padx, pady=pady, sticky=sticky)
        return button

    def create_combobox(self, row: int, column: int, values: list, sticky: str,
                        columnspan: int = 1, padx: int = 10, pady: int = 10, default_value: str = ""):
        """
        Function to create a combobox
        Args:
            row: row position to display
            column: column position to display
            values: values to display in the dropdown list
            sticky: stickiness to other component (Nord, South, East, West)
            columnspan: size that the label should take on the column axis
            padx: size of the label on x-axis
            pady: size of the label on y-axis
            default_value: default value to put in the dropdown list
        Return:
            combobox: return the created combobox
        """
        combobox = ttk.Combobox(self.model_frame, values=values)
        combobox.grid(row=row, column=column, columnspan=columnspan, padx=padx, pady=pady, sticky=sticky)
        combobox.set(default_value)
        return combobox

    @staticmethod
    def display_image(image_link: str, size_x: int, size_y: int):
        """
        Function to display an image
        Args:
            image_link: link to the image to display
            size_x: size of the image on the x-axis
            size_y: size of the image on the y-axis
        Return:
            formula_photo: return the created photo to display
        """
        formula_img = Image.open(image_link)
        formula_img = formula_img.resize((size_x, size_y))
        formula_photo = ImageTk.PhotoImage(formula_img)
        return formula_photo
