// Copyright (c) 2019, justine and contributors
// For license information, please see license.txt

frappe.ui.form.on('Final Students', {
	// refresh: function(frm) {

	// }
});

cur_frm.cscript.course = function (frm,cdt,cdn) {

    frappe.call({
        method: "app1.meeting_app.doctype.final_students.final_students.get_final_students",
    args: {
		row_data: cur_frm.doc.course
    },
        callback: function(r){
            console.log(r.message);
            console.log(cur_frm.doc.listoffinalstudents);
            cur_frm.doc.listoffinalstudents = [];

            cur_frm.refresh_field("listoffinalstudents")
            if(r.message.length > 0) {

                for(var i = 0;i < (r.message.length ) ;i++){
                    console.log("doing some iteration");
                    var child = cur_frm.add_child("listoffinalstudents");

                    // var d = locals['List of Final Students'][('New List of Final Students'+" "+(i+1))];
                    // if(d['studentid'] != undefined && d['fullname'] != undefined){
                    //     d['studentid'] =r.message[i].name;
                    //     d['fullname'] =r.message[i].fullname;
                    //     console.log("success");
                    // }
                    frappe.model.set_value(child.doctype,child.name,"studentid",r.message[i].name);
				    frappe.model.set_value(child.doctype,child.name,"fullname",r.message[i].fullname);



                }

                // cur_frm.refresh_field("listoffinalstudents");
				// frappe.model.set_value(child.doctype,child.name,"item_code","New Item Name");
				// frappe.model.set_value(child.doctype,child.name,"qty","New Item qty");
				cur_frm.refresh_field("listoffinalstudents");







            }else{

            }
        }
    });
}