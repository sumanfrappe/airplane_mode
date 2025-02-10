frappe.ui.form.on('Rent Payment', {
    before_save: function(frm) {
        if (!frm.doc.receipt_no) {
            let randomNumber = Math.floor(100000 + Math.random() * 900000); // Generate a 6-digit random number
            frm.set_value('receipt_no', "RENT-" + randomNumber);
        }
    },

    
    validate: function(frm) {
        if (frm.doc.tenant) {
            frappe.db.get_value('Tenant', frm.doc.tenant, ['lease_start', 'lease_end'], (r) => {
                if (r.lease_start && r.lease_end) {
                    if (frm.doc.payment_date < r.lease_start || frm.doc.payment_date > r.lease_end) {
                        frappe.msgprint(__('Payment Date must be within the lease period!'));
                        frappe.validated = false;
                    }
                }
            });
        }

        if (frm.doc.payment_date) {
            let today = frappe.datetime.get_today();
            
            if (frm.doc.payment_date <= today) {
                frm.set_value('status', 'Paid');
            } else {
                frm.set_value('status', 'Overdue');
            }
        }
        
    },

    refresh: function(frm) {

        frm.set_query('tenant', function() {
            return {
                filters: [
                    ['Tenant', 'name', 'not in',
                        frappe.db.get_list('Rent Payment', {
                            fields: ['tenant'],
                            pluck: 'tenant'
                        })
                    ]
                ]
            };
        });
        
        if (frm.doc.docstatus == 1 && frm.doc.status == "Paid") {
            frm.add_custom_button(__('Print Receipt'), function() {
                frappe.set_route('print', frm.doc.doctype, frm.doc.name, 'Rent Payment');
            });
        }


    },


    
});
