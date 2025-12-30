class Rental:
    def __init__(self, rental_id, customer_id, created, note=None):
        self.id = rental_id
        self.customer_id = customer_id
        self.created = created
        self.note = note
        self.items = []
        