// Copyright (c) 2019, justine and contributors
// For license information, please see license.txt

frappe.ui.form.on('Courses', {
	// refresh: function(frm) {

	// }
});



cur_frm.cscript.studentid = function (frm,cdt,cdn) {
	var d = locals[cdt][cdn]
	console.log(d.studentid);
 frappe.call({
        method: "app1.meeting_app.doctype.courses.courses.get_student_information",
	args: {
		row_data: d.studentid
	},
        callback: function(r){
            console.log(r.message);

            if(r.message.length > 0) {
            		d['fullname'] =r.message[0].fullname;
            		d['age'] =r.message[0].age;
            		d['birthdate'] =r.message[0].birthdate;

            		cur_frm.refresh_field("studentsenrolled");

            }
        }
    });
}
cur_frm.cscript.subjectid = function (frm,cdt,cdn) {
	console.log(cdt);
	console.log(cdn);
	var x = locals[cdt][cdn]
	console.log(x.subjectid);
 frappe.call({
        method: "app1.meeting_app.doctype.courses.courses.get_list_of_subject",
	args: {
		row_data: x.subjectid
	},
        callback: function(r){
            console.log(r.message);

            if(r.message.length > 0) {
            		x['subjectid'] =r.message[0].name;
            		x['subjectname'] =r.message[0].subjectname;


            		cur_frm.refresh_field("listofsubjects");

            }
        }
    });
}

