import tkinter as tk
import os
from tkinter import ttk, messagebox
from Model.MachineDAO import MachineDAO
from Model.CustomerDAO import CustomerDAO
from Model.RentalDAO import RentalDAO


def set_icon(window):
    """
    Sets icon for specific window.
    :param window: window that takes the logo
    :return:
    """
    cur_dir = os.path.dirname(os.path.abspath(__file__))
    icon_path = os.path.join(cur_dir, "..", "machine_logo.ico")
    if os.path.exists(icon_path):
        window.iconbitmap(icon_path)


class MainMenu:
    def __init__(self, master):
        self.master = master
        self.master.configure(bg="#2b2b2b")
        self.setup_menu()

        self.title_label = tk.Label(master, text="VOLVO RENTAL MANAGER", font=("Helvetica", 28, "bold"), bg="#2b2b2b",
                                    fg="#f0f0f0", pady=30)
        self.title_label.pack()
        set_icon(master)

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TCombobox", font=("Arial", 12))
        self.master.option_add("*TCombobox*Listbox.font", ("Arial", 12))
        style.map('TCombobox', fieldbackground=[('readonly', '#3c3f41')])
        style.map('TCombobox', foreground=[('readonly', 'white')])
        style.configure("Treeview", background="#3c3f41", foreground="white", fieldbackground="#3c3f41", rowheight=25)
        style.map("Treeview", background=[("selected", "#4b6eaf")])
        style.configure("Treeview.Heading", background="#1e1e1e", foreground="white", relief="flat")
        style.map("Treeview.Heading", background=[('active', '#333333')])
        self.tree = ttk.Treeview(master, columns=("ID", "Model", "Weight", "Available", "Category"), show="headings")
        self.setup_treeview()
        self.tree.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)
        self.btn_refresh = tk.Button(self.master, text="Refresh list of Machines", command=self.load_machines,
                                     bg="#333333", fg="white", activebackground="#4b6eaf", activeforeground="white",
                                     relief="flat", pady=5, padx=15)
        self.btn_refresh.pack(pady=10)
        self.load_machines()

    def setup_menu(self):
        """
        Specifies main menu structure and styles it.
        :return: appearance properties
        """
        menubar = tk.Menu(self.master, bg="#1e1e1e", fg="white")
        self.master.config(menu=menubar)
        menu_style = {
            "bg": "#1e1e1e",
            "fg": "white",
            "activebackground": "#4b6eaf",
            "activeforeground": "white",
            "tearoff": 0
        }

        # Main Menu
        file_menu = tk.Menu(menubar, **menu_style)
        menubar.add_cascade(label="Main Menu", menu=file_menu)
        file_menu.add_command(label="End", command=self.master.quit)

        # Menu Administration
        manage_menu = tk.Menu(menubar, **menu_style)
        menubar.add_cascade(label="Administration", menu=manage_menu)
        manage_menu.add_command(label="Machines", command=self.load_machines)
        manage_menu.add_command(label="Customers", command=self.load_customers)
        manage_menu.add_command(label="Rentals", command=self.load_rented)

        # Menu Renting
        rental_menu = tk.Menu(menubar, **menu_style)
        menubar.add_cascade(label="Rentals", menu=rental_menu)
        rental_menu.add_command(label="New Lease", command=self.open_rental_window)

        # Menu Edits
        edit_menu = tk.Menu(menubar, **menu_style)
        menubar.add_cascade(label="Add", menu=edit_menu)
        edit_menu.add_command(label="Add Machine", command=self.add_machine)
        edit_menu.add_command(label="Add Customer", command=self.add_customer)

    def setup_treeview(self):
        """
        Sets structure of treeview table.
        :return: properties of treeview
        """
        self.tree["columns"] = ("c1", "c2", "c3", "c4", "c5")
        self.tree.column("#0", width=0, stretch=tk.NO)
        self.tree["show"] = "headings"

        self.tree.column("c1", width=50)
        self.tree.column("c2", width=150)
        self.tree.column("c3", width=100)
        self.tree.column("c4", width=150)
        self.tree.column("c5", width=150)

    def load_machines(self):
        """
        Edits header of treeview table and loads information about machines from database.
        :return:
        """
        self.tree.heading("c1", text="ID")
        self.tree.heading("c2", text="Model")
        self.tree.heading("c3", text="Weight (t)")
        self.tree.heading("c4", text="Available")
        self.tree.heading("c5", text="Category")

        for i in self.tree.get_children():
            self.tree.delete(i)

        dao = MachineDAO()
        machines = dao.get_all_machines()
        for m in machines:
            self.tree.insert("", tk.END, values=(m.id, m.model, m.weight, m.is_available, m.category_name))
        self.btn_refresh.config(text="Refresh Machines", command=self.load_machines)

    def load_customers(self):
        """
        Edits header of treeview table and loads information about machines from database.
        :return:
        """
        self.tree.heading("c1", text="ID")
        self.tree.heading("c2", text="Company")
        self.tree.heading("c3", text="Name")
        self.tree.heading("c4", text="Email")
        self.tree.heading("c5", text="Registration date")

        for i in self.tree.get_children():
            self.tree.delete(i)
        dao = CustomerDAO()
        customers = dao.get_all_customers()
        for c in customers:
            self.tree.insert("", tk.END, values=(c.id, c.company_name, c.full_name, c.email, c.registration_date))
        self.btn_refresh.config(text="Refresh Customers", command=self.load_customers)

    def load_rented(self):
        """
        Edits header of treeview table and loads information about machines from database.
        :return:
        """
        self.tree.heading("c1", text="ID")
        self.tree.heading("c2", text="Customer")
        self.tree.heading("c3", text="Machine")
        self.tree.heading("c4", text="Days")
        self.tree.heading("c5", text="Final Price")

        for i in self.tree.get_children():
            self.tree.delete(i)
        dao = RentalDAO()
        rentals = dao.get_all_rentals()
        for r in rentals:
            total = r[3] * r[4]
            self.tree.insert("", tk.END, values=(r[0], r[1], r[2], r[3], f"{total} CZK"))
        self.btn_refresh.config(text="Refresh Rentals", command=self.load_rented)

    def open_rental_window(self):
        """
        Builds a popup window with a form creating new Rental contract.
        :return: window
        """
        top = tk.Toplevel(self.master)
        top.title("New Rental")
        top.geometry("800x700")
        set_icon(top)
        top.configure(bg="#2b2b2b")

        entry_style = {
            "font": ("Arial", 12),
            "bg": "#3c3f41",
            "fg": "white",
            "insertbackground": "white",
            "relief": "flat",
        }

        style = ttk.Style()
        style.configure("TCombobox", font=("Arial", 12))
        top.option_add("*TCombobox*Listbox.font", ("Arial", 12))
        top.option_add("*TCombobox*Listbox.background", "#3c3f41")
        top.option_add("*TCombobox*Listbox.foreground", "white")

        # Customer
        tk.Label(top, text="Choose Customer:", bg="#2b2b2b", fg="#f0f0f0", font=("Arial", 10, "bold")).pack(pady=5)
        c_dao = CustomerDAO()
        customers = c_dao.get_all_customers()
        customer_list = [f"{c.id}: {c.company_name} - {c.full_name}" for c in customers]
        combo_customer = ttk.Combobox(top, values=customer_list, state="readonly", width=40)
        combo_customer.pack(pady=5, padx=50, ipady=4, fill=tk.X)

        # Machine
        tk.Label(top, text="Choose Available Machine", bg="#2b2b2b", fg="#f0f0f0", font=("Arial", 10, "bold")).pack(pady=5)
        m_dao = MachineDAO()
        available_machines = m_dao.get_available_machines()
        machine_list = [f"{m.id}: {m.model} ({m.weight}t)" for m in available_machines]
        combo_machine = ttk.Combobox(top, values=machine_list, state="readonly", width=40)
        combo_machine.pack(pady=5, padx=50, ipady=4, fill=tk.X)

        # Number of days
        tk.Label(top, text="Number of days:",bg="#2b2b2b", fg="#f0f0f0", font=("Arial", 10, "bold")).pack(pady=5)
        ent_days = tk.Entry(top, width=42, **entry_style)
        ent_days.insert(0, "1")
        ent_days.pack(pady=5, padx=50, ipady=5, fill=tk.X)
        # Price
        tk.Label(top, text="Price per day", bg="#2b2b2b", fg="#f0f0f0", font=("Arial", 10, "bold")).pack(pady=5)
        ent_price = tk.Entry(top, width=42, **entry_style)
        ent_price.pack(pady=5, padx=50, ipady=5, fill=tk.X)

        def confirm_rental():
            """
            Information message of success or failure of creating rental contract.
            :return:
            """
            try:
                customer_id = int(combo_customer.get().split(":")[0])
                machine_id = int(combo_machine.get().split(":")[0])
                days = int(ent_days.get())
                price = float(ent_price.get())

                r_dao = RentalDAO()
                if r_dao.create_rental(customer_id, machine_id, days, price):
                    messagebox.showinfo("Success", "Lease was successfully registered.")
                    top.destroy()
                    self.load_machines()
                else:
                    messagebox.showerror("Error", "Lease couldn't be registered.")
            except Exception as e:
                messagebox.showwarning("Warning", f"Fill in all the gaps. \n{e}")
        tk.Button(top, text="Confirm Rental", command=confirm_rental, bg="#FFD700", font=("Arial", 11, "bold"), pady=10).pack(pady=30)

    def add_machine(self):
        """
        Popup window with form that lets user create a new machine.
        :return:
        """
        top = tk.Toplevel(self.master)
        top.title("Create New Machine")
        top.geometry("800x600")
        top.configure(bg="#2b2b2b")
        set_icon(top)

        entry_style = {
            "font": ("Arial", 12),
            "bg": "#3c3f41",
            "fg": "white",
            "insertbackground": "white",
            "relief": "flat",
        }

        tk.Label(top, text="Machine Model:", bg="#2b2b2b", fg="#f0f0f0", font=("Arial", 10, "bold")).pack(pady=5)
        ent_model = tk.Entry(top, **entry_style)
        ent_model.pack(pady=5, padx=50, ipady=5, fill=tk.X)

        tk.Label(top, text="Weight:", bg="#2b2b2b", fg="#f0f0f0", font=("Arial", 10, "bold")).pack(pady=5)
        ent_weight = tk.Entry(top, **entry_style)
        ent_weight.pack(pady=5, padx=50, ipady=5, fill=tk.X)

        tk.Label(top, text="Category:", bg="#2b2b2b", fg="#f0f0f0", font=("Arial", 10, "bold")).pack(pady=5)
        dao_m = MachineDAO()
        categories = dao_m.get_categories()
        names = [c[1] for c in categories]
        combo = ttk.Combobox(top, values=names, state="readonly", width=40)
        combo.pack(pady=5, padx=50, ipady=4, fill=tk.X)

        def save():
            """
            Information message of success or failure of creating new machine record.
            Handles invalid inputs like blank lines.
            :return:
            """
            index = combo.current()
            if index == -1:
                tk.messagebox.showwarning("Warning", "Choose Category")
                return
            category_id = categories[index][0]
            model_val = ent_model.get()
            weight_val = ent_weight.get()

            if not model_val or not weight_val:
                tk.messagebox.showwarning("Warning", "Fill in the model and weight.")
                return

            dao = MachineDAO()
            success = dao.create_machine(model_val, weight_val, category_id)
            if success:
                tk.messagebox.showinfo("Success", "Machine successfully created.")
                top.destroy()
                self.load_machines()
            else:
                tk.messagebox.showerror("Error", "Machine couldn't be created.")

        tk.Button(top, text="Create Machine", command=save, bg="#FFD700", font=("Arial", 11, "bold"), pady=10).pack(pady=30)

    def add_customer(self):
        """
        Popup window with form that lets user create a new customer profile.
        :return:
        """
        top = tk.Toplevel(self.master)
        top.title("Add New Customer")
        top.geometry("800x600")
        top.configure(bg="#2b2b2b")
        set_icon(top)

        entry_style = {
            "font": ("Arial", 12),
            "bg": "#3c3f41",
            "fg": "white",
            "insertbackground": "white",
            "relief": "flat",
        }

        # Form
        tk.Label(top, text="Company name:", bg="#2b2b2b", fg="#f0f0f0", font=("Arial", 10, "bold")).pack(pady=10)
        ent_company = tk.Entry(top, **entry_style)
        ent_company.pack(pady=5, padx=50, ipady=4, fill=tk.X)

        tk.Label(top, text="Name:", bg="#2b2b2b", fg="#f0f0f0", font=("Arial", 10, "bold")).pack(pady=10)
        ent_name = tk.Entry(top, **entry_style)
        ent_name.pack(pady=5, padx=50, ipady=4, fill=tk.X)

        tk.Label(top, text="Surname:", bg="#2b2b2b", fg="#f0f0f0", font=("Arial", 10, "bold")).pack(pady=10)
        ent_surname = tk.Entry(top, **entry_style)
        ent_surname.pack(pady=5, padx=50, ipady=4, fill=tk.X)

        tk.Label(top, text="Email:", bg="#2b2b2b", fg="#f0f0f0", font=("Arial", 10, "bold")).pack(pady=10)
        ent_email = tk.Entry(top, **entry_style)
        ent_email.pack(pady=5, padx=50, ipady=4, fill=tk.X)

        def save():
            """
            Information message of success or failure of creating new customer record.
            :return:
            """
            dao = CustomerDAO()
            success = dao.create_customer(ent_company.get(), ent_name.get(), ent_surname.get(), ent_email.get())
            if success:
                tk.messagebox.showinfo("Success", "Customer successfully created.")
                top.destroy()
                self.load_customers()
            else:
                tk.messagebox.showerror("Error", "Customer couldn't be created.")

        tk.Button(top, text="Create Customer", command=save, bg="#FFD700", font=("Arial", 11, "bold"), pady=10).pack(pady=30)

