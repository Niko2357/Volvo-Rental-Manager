class Machine:
    def __init__(self, machine_id, model, weight, is_available, category_name=None):
        self.id = machine_id
        self.model = model
        self.weight = weight
        self.is_available = "Yes" if is_available == 1 else "No"
        self.category_name = category_name

    def __str__(self):
        return f"{self.model} ({self.weight}t) - Availability: {self.is_available}"
