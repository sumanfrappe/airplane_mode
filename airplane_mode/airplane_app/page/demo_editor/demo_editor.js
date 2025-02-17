frappe.pages['demo_editor'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'demo_editor',
		single_column: true
	});

	// page.set_title('My Page')

	// page.set_title_sub('Subtitle')

	// page.set_indicator('Pending', 'orange')

	// page.clear_indicator()

	// let $btn = page.set_primary_action('New', () => create_new(), 'octicon octicon-plus')
	// page.clear_primary_action()

	// let $btn = page.set_secondary_action('Refresh', () => refresh(), 'octicon octicon-sync')
	// page.clear_secondary_action()

	// add a normal menu item
	// page.add_menu_item('Send Email', () => open_email_dialog())

	// add a standard menu item
	// page.add_menu_item('Send Email', () => open_email_dialog(), true)

	// page.clear_menu()

	// add a normal menu item
	page.add_action_item('Delete', () => delete_items())

	// add a normal inner button
	page.add_inner_button('Update Posts', () => update_posts())

	// // add a dropdown button in a group
	// page.add_inner_button('New Post', () => new_post(), 'Make')

	// // change type of ungrouped button
	// page.change_inner_button_type('Update Posts', null, 'primary');

	// // change type of a button in a group
	// page.change_inner_button_type('Delete Posts', 'Actions', 'danger');

	let field = page.add_field({
		label: 'Document Type',
		fieldtype: 'Link',
		fieldname: 'document_type',
		options: 'DocType',  
		change() {
			console.log(field.get_value());
			doc = field.get_value()
			let field1 = page.add_field({
				label: 'Account doc',
				fieldtype: 'Link',
				fieldname: 'account_doc',
				options: doc,
				change() {
					console.log(field1.get_value())
				}
			})

		}
	});
	
	
	
	let values = page.get_form_values()
// { status: 'Open', priority: 'Low' }



}