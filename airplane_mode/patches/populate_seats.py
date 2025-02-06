import random
import frappe

def execute():
    """
    Populate the Seat field for all existing Airplane Ticket documents.
    """
    tickets = frappe.get_all('Airplane Ticket', fields=['name', 'seat'])

    for ticket in tickets:
        if not ticket.seat:  # Only update tickets where the Seat field is empty
            # Generate random seat value
            random_number = random.randint(1, 99)
            random_letter = random.choice(['A', 'B', 'C', 'D', 'E'])
            seat_value = f"{random_number}{random_letter}"

            # Update the Seat field
            frappe.db.set_value('Airplane Ticket', ticket.name, 'seat', seat_value)

    # Commit changes to the database
    frappe.db.commit()
