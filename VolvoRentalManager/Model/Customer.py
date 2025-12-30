class Customer:
    def __init__(self, customer_id, company_name, name, surname, email, registration_date):
        self.id = customer_id
        self.company_name = company_name
        self.full_name = f"{name} {surname}" if name else "Company"
        self.email = email
        self.registration_date = registration_date

    def __str__(self):
        return f"{self.company_name} : {self.full_name} ({self.email})"
