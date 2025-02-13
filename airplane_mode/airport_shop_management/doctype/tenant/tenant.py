# Copyright (c) 2025, suman and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
from frappe.utils import today


class Tenant(Document):
	pass


def update_expired_tenants():
	# Get all tenants whose lease end date is today or earlier and are still active
	tenants = frappe.get_all("Tenant", 
							filters={"status": "Active", "lease_end": ["<=", today()]}, 
							fields=["name", "shop"])

	for tenant in tenants:
		# Update tenant status to Expired
		frappe.db.set_value("Tenant", tenant.name, "status", "Expired")

		# Update the shop status to Available
		if tenant.shop:
			frappe.db.set_value("Shop", tenant.shop, "status", "Available")

	frappe.db.commit()  # Ensure changes are saved
