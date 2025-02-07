
frappe.ui.form.on("Airline", {
    refresh: function (frm) {
        console.log("Airline form loaded");

        if (frm.doc.website) {
            frm.add_web_link(frm.doc.website, "Visit Website");
        }
    }
});

