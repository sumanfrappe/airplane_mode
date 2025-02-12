from frappe.website.website_generator import WebsiteGenerator
import frappe
from frappe.utils import formatdate
from frappe.model.document import Document
from frappe.utils.background_jobs import enqueue
import time

class AirplaneFlight(WebsiteGenerator, Document):
    def autoname(self):
        """
        Generate name in the format: {Airplane}-{MM-YYYY}-{#####}.
        """
        if not self.airplane or not self.date_of_departure:
            frappe.throw("Airplane and Date of Departure are mandatory for naming.")

        formatted_date = formatdate(self.date_of_departure, "MM-YYYY")

        airplane_name = frappe.get_value("Airplane", self.airplane, "name")

        # Get the current count for this Airplane + Date combination
        count = frappe.db.count(
            "Airplane Flight",
            filters={
                "airplane": self.airplane,
                "date_of_departure": self.date_of_departure,
            },
        )

        serial_number = f"{count + 1:05d}"

        self.name = f"{airplane_name}-{formatted_date}-{serial_number}"

    def on_submit(self):
        
        if self.status != "Cancelled":
            self.status = "Completed"

        """Submit all Airplane Tickets linked to this flight that are Boarded."""
        
        # Fetch all tickets related to this flight where status is 'Boarded'
        tickets = frappe.get_all("Airplane Ticket",
            filters={"flight": self.name, "status": "Boarded"},
            fields=["name"]
        )

        for ticket in tickets:
            ticket_doc = frappe.get_doc("Airplane Ticket", ticket["name"])
            if ticket_doc.docstatus == 0:  
                ticket_doc.submit()  
                frappe.msgprint(f"Ticket {ticket_doc.name} has been submitted.")

        frappe.msgprint("All boarded tickets have been submitted.")

    def update_gate_numbers(self, new_gate_number, flight):
        tickets = frappe.get_all(
            "Airplane Ticket",
            filters={"flight": flight},
            fields=["name", "gate_number"]
        )

        for ticket in tickets:
            if ticket["gate_number"] != new_gate_number:
                # Update the gate number in the ticket
                frappe.db.set_value("Airplane Ticket", ticket["name"], "gate_number", new_gate_number)
                frappe.db.commit()

        # frappe.publish_realtime("msgprint", f"process {tickets} completed", user=frappe.session.user)

    def before_save(self):
        # Get the current value from the database
        old_gate_number = frappe.db.get_value("Airplane Flight", self.name, "gate_number")

        # If gate_number has changed, trigger background update
        if old_gate_number != self.gate_number:
            frappe.enqueue(
                self.update_gate_numbers,
                new_gate_number=self.gate_number,
                flight = self.name,
                queue='short',
                timeout=200,
                is_async=True
            )

        # frappe.msgprint("request given to queue")

