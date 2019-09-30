# Copyright (c) 2013, justine and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
@frappe.whitelist()
def get_student_information():



	studentData = frappe.db.sql("""select * from `tabStudent Information` """,as_dict=True)
	jsonData = []
	for i in range(len(studentData)):
		print(studentData[i])
		jsonData.append({
			'studentid': studentData[i].name,
			'fullname': studentData[i].fullname,
			'age': studentData[i].age
		})
	return jsonData


def execute(filters=None):
	studentData = get_student_information()
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
			'fieldname': 'age',
			'label': ('Age'),
			'fieldtype': 'Int',
			'options': ''
		}
	]

	data = studentData

	return columns, data