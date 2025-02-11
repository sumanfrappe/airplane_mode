import frappe

def get_context(context):
    # Get the shop ID from URL parameter
    shop_id = frappe.form_dict.get("shop_id")

    if shop_id:
        # Fetch the shop details
        shop = frappe.get_doc("Shop", shop_id)
        context.shop = shop
    else:
        context.shop = None
