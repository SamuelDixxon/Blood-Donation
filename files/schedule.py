class Schedule:
    def __init__(self):
        self.availabilities = []

    def add_availability(self, donor, date, time, blood_type):
        for availability in self.availabilities:
            if availability['donor'] == donor and availability['date'] == date and availability['time'] == time:
                # Update the existing availability
                availability['blood_type'] = blood_type
                return
        # Add a new availability
        self.availabilities.append({'donor': donor, 'date': date, 'time': time, 'blood_type': blood_type})

    def get_available_donors(self, date, blood_type):
        available_donors = []
        for availability in self.availabilities:
            if availability['date'] == date and availability['blood_type'] == blood_type:
                available_donors.append(availability['donor'])
        return available_donors