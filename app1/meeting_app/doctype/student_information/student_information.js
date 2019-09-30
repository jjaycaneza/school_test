// Copyright (c) 2019, justine and contributors
// For license information, please see license.txt

frappe.ui.form.on('Student Information', {
	refresh: function(frm) {
		cur_frm.call({
			method: "sayhi",
			doc: cur_frm.doc,
			callback: function(r) {

				console.log(r);
			}
		});
	}
});

// cur_frm.cscript.validate = function() {
//
//     cur_frm.set_value('fullname',cur_frm.doc.firstname +' ' + cur_frm.doc.middlename+' '  + cur_frm.doc.lastname);
//
// }
//
cur_frm.cscript.birthdate = function() {


   cur_frm.call({
		method: "calcAge",
		doc: cur_frm.doc,
		callback: function(r) {
		    cur_frm.set_value('age',r.message[1]);
		    console.log(r);
        }
	});


}

