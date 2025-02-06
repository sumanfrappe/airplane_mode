
frappe.ui.form.on('Airplane Ticket', {
    before_save: function(frm) {
        console.log("Before save triggered!");
    }
});


frappe.ui.form.on('Airplane Ticket', {
    before_submit: function (frm) {
        if (frm.doc.status !== 'Boarded') {
            frappe.throw(__('The ticket cannot be submitted unless the status is "Boarded".'));
        }
    }
});
