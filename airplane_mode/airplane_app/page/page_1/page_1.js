frappe.pages['page_1'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'page_1',
		single_column: true
	});
}