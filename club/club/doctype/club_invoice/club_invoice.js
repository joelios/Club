// Copyright (c) 2018, libracore GmbH and contributors
// For license information, please see license.txt

frappe.ui.form.on('Club Invoice', {
	refresh: function(frm) {
		if(frm.doc.address) {
			frappe.call({
				"method": "frappe.client.get",
				"args": {
					"doctype": "Address",
					"name": cur_frm.doc.address
				},
				"callback": function(response) {
					var address = response.message;
					if (address) {
						cur_frm.set_df_property('address_display','options','<p>'+address.address_line1+'<br>'+address.pincode+' '+address.city+'</p>');
					}
				}
			});
		}
	}
});