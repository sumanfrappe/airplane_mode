frappe.ui.form.on('Airplane Ticket', {
    before_save: function(frm) {
        console.log("Before save triggered!");
    },

    before_submit: function(frm) {
        if (frm.doc.status !== 'Boarded') {
            frappe.throw(__('The ticket cannot be submitted unless the status is "Boarded".'));
        }
    },

    refresh: function (frm) {
        frm.add_custom_button("Assign Seat", function() {
            // Create a new dialog
            let d = new frappe.ui.Dialog({
                title: 'Enter Seat Number',
                fields: [
                    {
                        label: 'Seat Number',
                        fieldname: 'seat_number',
                        fieldtype: 'Data'
                    }
                ],
                primary_action_label: 'Assign',
                primary_action(values) {
                    if (values.seat_number) {
                        frm.set_value('seat', values.seat_number); // Set the seat field
                        d.hide(); // Close the dialog
                    } else {
                        frappe.msgprint(__('Please enter a seat number.'));
                    }
                }
            });

            d.show(); // Show the dialog
        });
    }
});
