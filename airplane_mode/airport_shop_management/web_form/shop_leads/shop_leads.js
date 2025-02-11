frappe.ready(function() {
	function getQueryParam(param) {
        let urlParams = new URLSearchParams(window.location.search);
        return urlParams.get(param);
    }

    let shop_name = getQueryParam('shop_id');
    console.log("shop_name:", shop_name);

    // Auto-fill the form fields with URL parameters
    frappe.web_form.set_value('shop', shop_name);
})