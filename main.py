import tkinter as tk

from GUI.main_window_gui import GUI


def run():
    """
    Main function
    """
    main_window = tk.Tk()
    main_window.title("Pricing Models")
    main_window.minsize(400,300)
    GUI(main_window=main_window).create_principal_window()
    main_window.mainloop()


if __name__ == "__main__":
    run()
