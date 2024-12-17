import tkinter as tk
from tkinter import messagebox

class BloodDonationSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Blood Donation Management System")
        self.root.geometry("400x300")

        # Create main frames
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill="both", expand=True)

        # Create menu bar
        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)

        # Create menu items
        self.menu_bar.add_command(label="Donor Registration", command=self.donor_registration)
        self.menu_bar.add_command(label="Schedule Appointment", command=self.schedule_appointment)
        self.menu_bar.add_command(label="View Donor Information", command=self.view_donor_info)
        self.menu_bar.add_command(label="View Donation History", command=self.view_donation_history)
        self.menu_bar.add_command(label="Search Donors", command=self.search_donors)
        self.menu_bar.add_command(label="View Blood Availability", command=self.view_blood_availability)
        self.menu_bar.add_command(label="System Settings", command=self.system_settings)

        # Create main widgets
        self.donor_label = tk.Label(self.main_frame, text="Donor Registration")
        self.donor_label.pack(fill="x")

        self.donor_entry = tk.Entry(self.main_frame, width=20)
        self.donor_entry.pack(fill="x")

        self.donor_button = tk.Button(self.main_frame, text="Register", command=self.donor_registration)
        self.donor_button.pack(fill="x")

    def donor_registration(self):
        # Create donor registration form
        self.donor_form = tk.Toplevel(self.root)
        self.donor_form.title("Donor Registration")

        # Create form widgets
        self.name_label = tk.Label(self.donor_form, text="Name:")
        self.name_label.pack(fill="x")

        self.name_entry = tk.Entry(self.donor_form, width=20)
        self.name_entry.pack(fill="x")

        self.email_label = tk.Label(self.donor_form, text="Email:")
        self.email_label.pack(fill="x")

        self.email_entry = tk.Entry(self.donor_form, width=20)
        self.email_entry.pack(fill="x")

        self.phone_label = tk.Label(self.donor_form, text="Phone Number:")
        self.phone_label.pack(fill="x")

        self.phone_entry = tk.Entry(self.donor_form, width=20)
        self.phone_entry.pack(fill="x")

        self.blood_type_label = tk.Label(self.donor_form, text="Blood Type:")
        self.blood_type_label.pack(fill="x")

        self.blood_type_entry = tk.Entry(self.donor_form, width=20)
        self.blood_type_entry.pack(fill="x")

        self.submit_button = tk.Button(self.donor_form, text="Submit", command=self.submit_donor_registration)
        self.submit_button.pack(fill="x")

    def submit_donor_registration(self):
        # Get form data
        name = self.name_entry.get()
        email = self.email_entry.get()
        phone = self.phone_entry.get()
        blood_type = self.blood_type_entry.get()

        # Validate form data
        if not name or not email or not phone or not blood_type:
            messagebox.showerror("Error", "Please fill out all fields")
            return

        # Register donor
        # TO DO: implement donor registration logic

        # Close form
        self.donor_form.destroy()

    def schedule_appointment(self):
        # Create appointment scheduling form
        self.appointment_form = tk.Toplevel(self.root)
        self.appointment_form.title("Schedule Appointment")

        # Create form widgets
        self.date_label = tk.Label(self.appointment_form, text="Date:")
        self.date_label.pack(fill="x")

        self.date_entry = tk.Entry(self.appointment_form, width=20)
        self.date_entry.pack(fill="x")

        self.time_label = tk.Label(self.appointment_form, text="Time:")
        self.time_label.pack(fill="x")

        self.time_entry = tk.Entry(self.appointment_form, width=20)
        self.time_entry.pack(fill="x")

        self.location_label = tk.Label(self.appointment_form, text="Location:")
        self.location_label.pack(fill="x")

        self.location_entry = tk.Entry(self.appointment_form, width=20)
        self.location_entry.pack(fill="x")

        self.submit_button = tk.Button(self.appointment_form, text="Submit", command=self.submit_appointment)
        self.submit_button.pack(fill="x")

    def submit_appointment(self):
        # Get form data
        date = self.date_entry.get()
        time = self.time_entry.get()
        location = self.location_entry.get()

        # Validate form data
        if not date or not time or not location:
            messagebox.showerror("Error", "Please fill out all fields")
            return

        # Schedule appointment
        # TO DO: implement appointment scheduling logic

        # Close form
        self.appointment_form.destroy()

    def view_donor_info(self):
        # Create donor information view
        self.donor_info_view = tk.Toplevel(self.root)
        self.donor_info_view.title("Donor Information")

        # Create view widgets
        self.name_label = tk.Label(self.donor_info_view, text="Name:")
        self.name_label.pack(fill="x")

        self.name_text = tk.Text(self.donor_info_view, width=20, height=5)
        self.name_text.pack(fill="x")

        self.email_label = tk.Label(self.donor_info_view, text="Email:")
        self.email_label.pack(fill="x")

        self.email_text = tk.Text(self.donor_info_view, width=20, height=5)
        self.email_text.pack(fill="x")

        self.phone_label = tk.Label(self.donor_info_view, text="Phone Number:")
        self.phone_label.pack(fill="x")

        self.phone_text = tk.Text(self.donor_info_view, width=20, height=5)
        self.phone_text.pack(fill="x")

    def view_donation_history(self):
        # Create donation history view
        self.donation_history_view = tk.Toplevel(self.root)
        self.donation_history_view.title("Donation History")

        # Create view widgets
        self.donation_list = tk.Listbox(self.donation_history_view, width=20, height=10)
        self.donation_list.pack(fill="x")

    def search_donors(self):
        # Create search form
        self.search_form = tk.Toplevel(self.root)
        self.search_form.title("Search Donors")

        # Create form widgets
        self.search_label = tk.Label(self.search_form, text="Search:")
        self.search_label.pack(fill="x")

        self.search_entry = tk.Entry(self.search_form, width=20)
        self.search_entry.pack(fill="x")

        self.search_button = tk.Button(self.search_form, text="Search", command=self.search_donors)
        self.search_button.pack(fill="x")

    def view_blood_availability(self):
        # Create blood availability view
        self.blood_availability_view = tk.Toplevel(self.root)
        self.blood_availability_view.title("Blood Availability")

        # Create view widgets
        self.blood_type_label = tk.Label(self.blood_availability_view, text="Blood Type:")
        self.blood_type_label.pack(fill="x")

        self.blood_type_text = tk.Text(self.blood_availability_view, width=20, height=5)
        self.blood_type_text.pack(fill="x")

    def system_settings(self):
        # Create system settings form
        self.system_settings_form = tk.Toplevel(self.root)
        self.system_settings_form.title("System Settings")

        # Create form widgets
        self.notification_label = tk.Label(self.system_settings_form, text="Notification Preferences:")
        self.notification_label.pack(fill="x")

        self.notification_entry = tk.Entry(self.system_settings_form, width=20)
        self.notification_entry.pack(fill="x")

        self.language_label = tk.Label(self.system_settings_form, text="Language:")
        self.language_label.pack(fill="x")

        self.language_entry = tk.Entry(self.system_settings_form, width=20)
        self.language_entry.pack(fill="x")

        self.submit_button = tk.Button(self.system_settings_form, text="Submit", command=self.submit_system_settings)
        self.submit_button.pack(fill="x")

    def submit_system_settings(self):
        # Get form data
        notification = self.notification_entry.get()
        language = self.language_entry.get()

        # Validate form data
        if not notification or not language:
            messagebox.showerror("Error", "Please fill out all fields")
            return

        # Save system settings
        # TO DO: implement system settings logic

        # Close form
        self.system_settings_form.destroy()

root = tk.Tk()
app = BloodDonationSystem(root)
root.mainloop()