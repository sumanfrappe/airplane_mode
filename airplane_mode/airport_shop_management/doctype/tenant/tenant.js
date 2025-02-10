frappe.ui.form.on('Tenant', {
    validate: function(frm) {
        // Check if Lease Start Date is greater than Lease End Date
        if (frm.doc.lease_start && frm.doc.lease_end) {
            if (frm.doc.lease_start > frm.doc.lease_end) {
                frappe.msgprint(__('Lease Start Date cannot be greater than Lease End Date'));
                frappe.validated = false;
                return;
            }
        }

        // Automatically set status to Expired if lease end date has passed
        if (frm.doc.lease_end && frappe.datetime.get_today() > frm.doc.lease_end) {
            frm.set_value('status', 'Expired');
        }
    },

    after_save: function(frm) {
        if (frm.doc.shop) {
            let shop_status = 'Available';

            // If tenant is Active, mark the shop as Occupied
            if (frm.doc.status === 'Active') {
                shop_status = 'Occupied';
            }

            // Update the shop's status
            frappe.db.set_value('Shop', frm.doc.shop, 'status', shop_status);
        }
    },

    onload: function(frm) {
        frm.set_query('shop', function() {
            return {
                filters: {
                    status: 'Available' // Only show available shops
                }
            }
        })
    }
});
