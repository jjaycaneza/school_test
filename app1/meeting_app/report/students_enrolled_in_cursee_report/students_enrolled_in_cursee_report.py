# Copyright (c) 2013, justine and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe


@frappe.whitelist()
def get_courses_information(course):
	print(course)
	if(course == None):

		coursesData = frappe.db.sql("""select * from `tabStudent Information`  """,as_dict=True)
	else:
		coursesData = frappe.db.sql("""select * from `tabStudent Information`  where `tabStudent Information`.`course`  =  %s""", (course),as_dict=True)
	print(coursesData)
	jsonData = []
	for i in range(len(coursesData)):
		print(coursesData[i])
		jsonData.append({
			'studentid': coursesData[i].name,
			'fullname': coursesData[i].fullname,
			'course': coursesData[i].course

		})
	return jsonData

def execute(filters=None):
	coursesData = get_courses_information(course=filters.course)



	columns = [
		{
			'fieldname': 'studentid',
			'label': ('Student ID'),
			'fieldtype': 'Data',
			'options': ''
		},
		{
			'fieldname': 'fullname',
			'label': ('Full Name'),
			'fieldtype': 'Data',
			'options': ''
		},
		{
			'fieldname': 'course',
			'label': ('Course'),
			'fieldtype': 'Link',
			'options': 'Courses'
		}
	]
	data = coursesData
	return columns, data
