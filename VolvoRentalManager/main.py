import tkinter as tk
from UI.MainMenu import MainMenu


#  Used for test runs.

def main():
    root = tk.Tk()
    root.title("Volvo Rental Manager")
    root.geometry("1100x900")

    app = MainMenu(root)

    root.mainloop()


if __name__ == "__main__":
    main()

