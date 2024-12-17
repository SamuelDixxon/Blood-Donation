# donor.py
class Donor:
    def __init__(self, name, blood_type):
        self.name = name
        self.blood_type = blood_type
        self.availability = []
        self.donation_history = []

    def add_availability(self, date, time):
        self.availability.append((date, time))

    def add_donation(self, date, time):
        self.donation_history.append((date, time))

    def __str__(self):
        return f"{self.name} ({self.blood_type})"