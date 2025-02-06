# Copyright (c) 2025, suman and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class FlightPassenger(Document):
    def before_save(self):
        # Auto-set Full Name field
        self.full_name = f"{self.first_name} {self.last_name}".strip()
