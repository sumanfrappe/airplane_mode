frappe.ui.form.on("Airplane", {
    refresh: function(frm) {
        // Check if user has 'Airport Authority Personnel' role
        if (!frappe.user.has_role("Airport Authority Personnel")) {
            frm.set_df_property("initial_audit_completed", "hidden", 1);
            frm.set_df_property("initial_audit_completed", "read_only", 1);
        }
    }
});
