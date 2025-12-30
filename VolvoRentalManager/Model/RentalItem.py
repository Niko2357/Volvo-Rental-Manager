class RentalItem:
    def __init__(self, rental_id, machine_id, price_per_day, days_count):
        self.rental_id = rental_id
        self.machine_id = machine_id
        self.price_per_day = price_per_day
        self.days_count = days_count
        self.total_price = price_per_day * days_count
