# Copyright (c) 2013, justine and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
@frappe.whitelist()
def get_courses_information():
	coursesData = frappe.db.sql("""select * from `tabCourses` """,as_dict=True)
	jsonData = []
	for i in range(len(coursesData)):
		print(coursesData[i])
		jsonData.append({
			'courseid': coursesData[i].name,
			'coursename': coursesData[i].coursename

		})
	return jsonData

def execute(filters=None):
	coursesData = get_courses_information()
	columns = [
		{
			'fieldname': 'courseid',
			'label': ('Course ID'),
			'fieldtype': 'Data',
			'options': ''
		},
		{
			'fieldname': 'coursename',
			'label': ('Course Name'),
			'fieldtype': 'Data',
			'options': ''
		}
	]
	data = coursesData
	return columns, data
