from donor import Donor
from blood_type import BloodType
from schedule import Schedule

# blood_donation_system.py
class BloodDonorSchedulingSystem:
    def __init__(self):
        self.schedule = Schedule()
        self.donors = []

    def add_donor(self, donor):
        self.donors.append(donor)
        self.schedule.add_donor(donor)

    def add_blood_type(self, blood_type):
        self.schedule.add_blood_type(blood_type)

    def add_availability(self, date, donor, blood_type):
        self.schedule.add_availability(date, donor, blood_type)

    def get_available_donors(self, date, blood_type):
        return self.schedule.get_available_donors(date, blood_type)

    def __str__(self):
        return str(self.schedule)