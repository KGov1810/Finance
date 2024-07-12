import tkinter as tk
import tkinter.font as tkfont
from abc import ABC, abstractmethod


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
