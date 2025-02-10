# Copyright (c) 2025, suman and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import today, add_days


class RentPayment(Document):
	pass

def send_rent_reminder():
	# Fetch tenants with 'Pending' or 'Overdue' payments
	tenants = frappe.get_all(
		"Rent Payment",
		filters={"status": ["in", ["Pending", "Overdue"]]},
		fields=["tenant", "payment_date", "status"],
	)

	for tenant_record in tenants:
		tenant = tenant_record["tenant"]
		due_date = tenant_record["payment_date"]
		status = tenant_record["status"]

		# Fetch tenant email and shop details from Tenant Doctype
		tenant_details = frappe.get_value("Tenant", tenant, ["email", "shop"], as_dict=True)

		if not tenant_details or not tenant_details.get("email"):
			continue  

		# Determine the subject and message based on status
		if status == "Pending":
			subject = "Reminder: Your Rent Payment is Due Soon"
			message = f"""
			Dear {tenant},<br><br>
			This is a friendly reminder that your rent for <b>Shop {tenant_details.get("shop")}</b> is due on <b>{due_date}</b>.<br>
			Please make the payment on time to avoid penalties.<br><br>
			Regards,<br>
			Management Team
			"""
		elif status == "Overdue":
			subject = "Urgent: Your Rent Payment is Overdue"
			message = f"""
			Dear {tenant},<br><br>
			Your rent for <b>Shop {tenant_details.get("shop")}</b> was due on <b>{due_date}</b> and is now overdue.<br>
			Please clear your dues immediately to avoid further penalties or legal action.<br><br>
			Regards,<br>
			Management Team
			"""

		# Send the email
		frappe.sendmail(
			recipients=tenant_details.get("email"),
			subject=subject,
			message=message
		)

	frappe.msgprint("Rent due reminder emails sent successfully!")

