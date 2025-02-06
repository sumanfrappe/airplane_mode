
import frappe
from frappe.model.document import Document
import random

class AirplaneTicket(Document):
    def autoname(self):
        if not self.flight or not self.source_airport_code or not self.destination_airport_code:
            frappe.throw("Flight, Source Airport Code, and Destination Airport Code are required.")

        existing_count = frappe.db.count(
            "Airplane Ticket",
            filters={"flight": self.flight}
        )
        ticket_number = str(existing_count + 1).zfill(3)  # Pad ticket number to 3 digits
        self.name = f"{self.flight}-{self.source_airport_code}-to-{self.destination_airport_code}-{ticket_number}"


    def validate(self):
        # Ensure all add-ons are unique
        self.remove_duplicate_add_ons()

        # Calculate Total Amount
        self.calculate_total_amount()

    def remove_duplicate_add_ons(self):
        """Ensure each add-on is unique in the child table."""
        unique_items = {}
        cleaned_add_ons = []
        
        for add_on in self.add_ons:
            if add_on.item not in unique_items:
                unique_items[add_on.item] = True
                cleaned_add_ons.append(add_on)

        # Set the cleaned list back to the child table
        self.add_ons = cleaned_add_ons

    def calculate_total_amount(self):
        """Calculate the total amount for the ticket."""
        add_on_total = sum(add_on.amount for add_on in self.add_ons)
        self.total_amount = self.flight_price + add_on_total

    def before_insert(self):
        """
        Set the Seat field to a random combination of a number and a letter (A-E) before the document is inserted.
        """
        random_number = random.randint(1, 99)  # Generate a random integer between 1 and 99
        random_letter = random.choice(['A', 'B', 'C', 'D', 'E'])  # Choose a random letter from A to E
        self.seat = f"{random_number}{random_letter}"