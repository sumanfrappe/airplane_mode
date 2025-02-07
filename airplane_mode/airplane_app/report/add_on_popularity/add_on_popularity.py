import frappe

def execute(filters=None):
    columns = [
        {"fieldname": "add_on_type", "label": "Add-On Type", "fieldtype": "Link", "options": "Airplane Ticket Add-on Type", "width": 200},
        {"fieldname": "sold_count", "label": "Sold Count", "fieldtype": "Int", "width": 120}
    ]

    data = frappe.db.sql("""
        SELECT 
            add_on_item.item AS add_on_type,
            COUNT(add_on_item.name) AS sold_count
        FROM `tabAirplane Ticket Add-on Item` AS add_on_item
        JOIN `tabAirplane Ticket` AS ticket ON add_on_item.parent = ticket.name
        GROUP BY add_on_item.item
        ORDER BY sold_count DESC
    """, as_dict=True)

    return columns, data
