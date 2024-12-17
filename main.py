import schedule
from donor import Donor
from blood_type import BloodType

# Create a new blood donation scheduling system
system = BloodDonorSchedulingSystem()

# Create some donors
donor1 = Donor("John Doe", BloodType("A+"))
donor2 = Donor("Jane Smith", BloodType("B-"))
donor3 = Donor("Bob Johnson", BloodType("A-"))

# Add the donors to the system
system.add_donor(donor1)
system.add_donor(donor2)
system.add_donor(donor3)

# Add some availability for the donors
system.add_availability("2023-03-01", donor1, BloodType("A+"))
system.add_availability("2023-03-01", donor2, BloodType("B-"))
system.add_availability("2023-03-02", donor3, BloodType("A-"))

# Get the available donors for a specific date and blood type
available_donors = system.get_available_donors("2023-03-01", BloodType("A+"))
print(available_donors)  # Output: [John Doe]

# Print the schedule
print(system)  # Output: 2023-03-01:
                #   John Doe (A+)
                # 2023-03-01:
                #   Jane Smith (B-)
                # 2023-03-02:
                #   Bob Johnson (A-)