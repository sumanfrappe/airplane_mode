import frappe
from frappe import _

def execute(filters=None):
    # Define columns 
    columns = [
        {"fieldname": "airline", "label": "Airline", "fieldtype": "Link", "options": "Airline", "width": 200},
        {"fieldname": "revenue", "label": "Revenue", "fieldtype": "Currency", "width": 150}
    ]

    # Fetch revenue per airline 
    data = frappe.db.sql("""
        SELECT 
            airline.name AS airline,
            COALESCE(SUM(ticket.total_amount), 0) AS revenue
        FROM `tabAirline` AS airline
        LEFT JOIN `tabAirplane` AS airplane ON airline.name = airplane.airline
        LEFT JOIN `tabAirplane Flight` AS flight ON airplane.name = flight.airplane
        LEFT JOIN `tabAirplane Ticket` AS ticket ON flight.name = ticket.flight
        GROUP BY airline.name
        ORDER BY revenue DESC
    """, as_dict=True)

    # Calculate total revenue
    total_revenue = sum(row["revenue"] for row in data)

    # Add "Total" row 
    data.append({
        "airline": "Total",
        "revenue": total_revenue
    })

    # Add Summary Section
    summary = [
        {"label": _("Total Revenue"), "value": total_revenue, "indicator": "Green"}
    ]

    # Add Donut Chart
    chart = {
        "data": {
            "labels": [row["airline"] for row in data[:-1]],  # Exclude "Total" row from chart
            "datasets": [{"values": [row["revenue"] for row in data[:-1]]}]
        },
        "type": "donut"
    }

    return columns, data, None, chart, summary
