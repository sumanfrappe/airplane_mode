# Copyright (c) 2025, suman and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils.synchronization import filelock

import time

class demo_doc(Document):
	def update_gate_number_in_background(self, new_gate_number):
		linked_records = frappe.get_all(
			"testing backgroung job",
			filters={
				"first_name": self.first_name  # Assuming first_name is the link field
			},
			fields=["name"]
		)

		# Update gate_number for all linked records
		for record in linked_records:
			doc = frappe.get_doc("testing backgroung job", record.name)
			doc.gate_number = new_gate_number
			doc.save()
			frappe.db.commit()  # Commit changes to the database

		frappe.log_error("this process is time taking")

		frappe.publish_realtime("msgprint", f"process {linked_records} completed", user = frappe.session.user)
		

	# def before_save(self):
	# 	# Get the current value from the database
	# 	old_gate_number = frappe.db.get_value("demo_doc", self.name, "gate_number")

	# 	# If gate_number has changed, trigger background update
	# 	if old_gate_number != self.gate_number:
	# 		frappe.enqueue(
	# 			self.update_gate_number_in_background,
	# 			new_gate_number=self.gate_number,
	# 			queue='short',
	# 			timeout=200,
	# 			is_async=True
    #     	)
		
	# 	frappe.msgprint("request given to queue")

	