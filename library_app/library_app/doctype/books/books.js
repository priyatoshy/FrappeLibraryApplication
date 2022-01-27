// Copyright (c) 2022, Priyatosh and contributors
// For license information, please see license.txt

frappe.ui.form.on('Books', {
	after_save: function(frm) {
		indictor:'green',
        msgprint('New Book Added');
    }
	
	

	 
	})
	