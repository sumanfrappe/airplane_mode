import frappe

def execute(filters=None):
    columns = [
        {"label": "Receipt No", "fieldname": "receipt_no", "fieldtype": "Data", "width": 150},
        {"label": "Tenant", "fieldname": "tenant", "fieldtype": "Link", "options": "Tenant", "width": 200},
        {"label": "Shop", "fieldname": "shop", "fieldtype": "Link", "options": "Shop", "width": 150},
        {"label": "Payment Date", "fieldname": "payment_date", "fieldtype": "Date", "width": 120},
        {"label": "Payment Status", "fieldname": "payment_status", "fieldtype": "Select", "width": 120},
        {"label": "Payment Method", "fieldname": "payment_method", "fieldtype": "Data", "width": 150},
        {"label": "Rent Amount", "fieldname": "rent_amount", "fieldtype": "Currency", "width": 150},
    ]
    
    data = frappe.get_all(
        "Rent Payment",
        fields=["receipt_no", "tenant", "shop", "payment_date", "status", "payment_method", "rent_amount"],
        order_by="payment_date DESC"
    )

    return columns, data
