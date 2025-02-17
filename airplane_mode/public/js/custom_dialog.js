// frappe.ui.form.on('demo_doc', {
//     refresh: function(frm) {
//         frm.add_custom_button('Show Prompt', function() {
//             frappe.prompt([
//                 {'fieldname': 'name', 'fieldtype': 'Data', 'label': 'Name', 'reqd': 1}
//             ],
//             function(values){
//                 frappe.msgprint('Hello ' + values.name);
//             },
//             'Enter Name',
//             'Submit');
//         });
//     }
// });

// frappe.ui.form.on('demo_doc', {
//     refresh: function(frm) {

//         frm.add_custom_button('Open Dialog', function() {
//             frappe.msgprint('This is a message from a custom script!');
//         });
//     }
// });
