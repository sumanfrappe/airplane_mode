frappe.ready(function() {
    function getQueryParam(param) {
        let urlParams = new URLSearchParams(window.location.search);
        return urlParams.get(param);
    }

    let flight_name = getQueryParam('flight_name');
    console.log("flight_name:", flight_name);

    // Auto-fill the form fields with URL parameters
    frappe.web_form.set_value('flight', flight_name);

    // Add validation before form submission
    frappe.web_form.validate = () => {
        if (!frappe.web_form.get_value("flight_price")) {
            
            frappe.msgprint(__('Flight Price field is mandatory.'));
            return false; 
        }
    };
});
