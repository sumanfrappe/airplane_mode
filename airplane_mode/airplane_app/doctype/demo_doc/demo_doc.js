// Copyright (c) 2025, suman and contributors
// For license information, please see license.txt

frappe.ui.form.on('demo_doc', {
    refresh: function(frm) {
        //----------------- add pre defined fileds in form 
        // frm.add_custom_button('Create Invoice', function() {
        //     frappe.new_doc('demo_doc', {
        //         'first_name': 'suman',
        //         'last_name': 'Makwana',
        //         'gate_number': '50'
        //     });
        // });

        //------------------------- prompt dialog api
        // frappe.prompt([
        //     {'fieldname': 'name', 'fieldtype': 'Data', 'label': 'Name', 'reqd': 1}, 
        //     {'fieldname': 'age', 'fieldtype': 'Int', 'label': 'Age'}
        // ],
        // function(values){
        //     frappe.msgprint('Hello ' + values.name + ', Age: ' + values.age);
        // },
        // 'Enter Details',
        // 'Submit');
        

        //----------------------confirm dialogg api
        // frappe.confirm(
        //     'Are you sure you want to proceed?',
        //     function(){
        //         frappe.msgprint('You confirmed!');
        //     },
        //     function(){
        //         frappe.msgprint('You cancelled.');
        //     }
        // );
        
        // frm.add_custom_button('Add Multiple People', function() {
        //     new frappe.ui.form.MultiSelectDialog({
        //         doctype: 'demo_doc',
        //         target: frm,
        //         setters: {
        //             'last_name': ''
        //         },
        //         get_query() {
        //             return {
        //                 filters: {
        //                     'last_name': frm.doc.last_name  // Filter by current form's gate_number
        //                 }
        //             };
        //         },
        //         primary_action_label: 'Add Selected',
        //         action(selections) {
        //             console.log(selections)
        //         }
        //     });
        // });
    
        //  frm.add_custom_button('Add People', function() {
        //     // Create the dialog
        //     let dialog = new frappe.ui.Dialog({
        //         title: 'Add Multiple People',
        //         fields: [
        //             {
        //                 fieldname: 'people_table',
        //                 fieldtype: 'Table',
        //                 label: 'People',
        //                 fields: [
        //                     {
        //                         fieldtype: 'Data',
        //                         fieldname: 'first_name',
        //                         label: 'First Name',
        //                         in_list_view: 1
        //                     },
        //                     {
        //                         fieldtype: 'Data',
        //                         fieldname: 'last_name',
        //                         label: 'Last Name',
        //                         in_list_view: 1
        //                     },
        //                     {
        //                         fieldtype: 'Data',
        //                         fieldname: 'gate_number',
        //                         label: 'Gate Number',
        //                         in_list_view: 1
        //                     }
        //                 ],
        //                 data: [],
        //                 get_data: function() {
        //                     return this.data;
        //                 }
        //             }
        //         ],
        //         primary_action_label: 'Add to Gate Pass',
        //         primary_action: function() {
        //             let data = dialog.get_values().people_table;
        //             if (data && data.length > 0) {
        //                 data.forEach(row => {
        //                     let child = frm.add_child('people');
        //                     child.first_name = row.first_name;
        //                     child.last_name = row.last_name;
        //                     child.gate_number = row.gate_number;
        //                 });
        //                 frm.refresh_field('people');
        //             }
        //             dialog.hide();
        //         }
        //     });

        //     // Show the dialog
        //     dialog.show();
        // });    
        
    }
});
