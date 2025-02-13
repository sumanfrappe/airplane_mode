import frappe

# @frappe.whitelist()
# def get_shop_details(shop_id=None):
#     return frappe.db.sql(f"""select shop_name from `tabShop` where status='Available';""", as_dict=True)


# def check_events(doc, event):
#     frappe.msgprint(f"validated this {doc.name} and {event}")