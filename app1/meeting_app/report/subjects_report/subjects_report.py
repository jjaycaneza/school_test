# Copyright (c) 2013, justine and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
@frappe.whitelist()
def get_subjects_information():
	subjectsData = frappe.db.sql("""select * from `tabSubjects` """,as_dict=True)
	jsonData = []
	for i in range(len(subjectsData)):
		print(subjectsData[i])
		jsonData.append({
			'subjectid': subjectsData[i].name,
			'subjectname': subjectsData[i].subjectname

		})
	return jsonData

def execute(filters=None):
	subjectsData = get_subjects_information()
	columns = [
		{
			'fieldname': 'subjectid',
			'label': ('Subject ID'),
			'fieldtype': 'Data',
			'options': ''
		},
		{
			'fieldname': 'subjectname',
			'label': ('Subject Name'),
			'fieldtype': 'Data',
			'options': ''
		}
	]
	data = subjectsData
	return columns, data
