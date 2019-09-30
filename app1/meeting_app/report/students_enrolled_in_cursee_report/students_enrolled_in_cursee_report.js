// Copyright (c) 2016, justine and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Students Enrolled in Cursee Report"] = {
	filters: [
		 {
            fieldname: 'course',
            label: __('Course'),
            fieldtype: 'Link',
            options: 'Courses',
            default: frappe.defaults.get_user_default('course')
        }
	]
};
