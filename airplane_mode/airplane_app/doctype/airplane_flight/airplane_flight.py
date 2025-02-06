from frappe.model.document import Document
import frappe
from frappe.utils import formatdate


class AirplaneFlight(Document):
    def autoname(self):
        """
        Generate name in the format: {Airplane}-{MM-YYYY}-{#####}.
        """
        if not self.airplane or not self.date_of_departure:
            frappe.throw("Airplane and Date of Departure are mandatory for naming.")

        # Format the date as MM-YYYY
        formatted_date = formatdate(self.date_of_departure, "MM-YYYY")

        # Fetch the airplane name
        airplane_name = frappe.get_value("Airplane", self.airplane, "name")

        # Get the current count for this Airplane + Date combination
        count = frappe.db.count(
            "Airplane Flight",
            filters={
                "airplane": self.airplane,
                "date_of_departure": self.date_of_departure,
            },
        )

        # Increment the count for a unique serial number
        serial_number = f"{count + 1:05d}"

        # Combine all parts to create the document name
        self.name = f"{airplane_name}-{formatted_date}-{serial_number}"

    def on_submit(self):
        """
        Update status to 'Completed' upon submission.
        """
        if self.status != "Cancelled":
            self.status = "Completed"

    def on_submit(self):
        """
        Set the Status field to 'Completed' upon document submission.
        """
        self.status = "Completed"