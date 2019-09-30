// Copyright (c) 2016, justine and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["List of Subjects in Course Report"] = {
	filters: [
		 {
            fieldname: 'subjectid',
            label: __('Subject ID'),
            fieldtype: 'Link',
            options: 'Subjects',
            default: frappe.defaults.get_user_default('subjectid')
        }
	]
};
