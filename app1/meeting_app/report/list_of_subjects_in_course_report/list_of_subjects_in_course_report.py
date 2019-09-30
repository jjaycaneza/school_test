# Copyright (c) 2013, justine and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe


@frappe.whitelist()
def get_subject_information(subjectid):
	print(subjectid)
	if(subjectid == None):
		subjectData = frappe.db.sql("""select * from `tabList of Subjects`""",as_dict=True)
	else:
		subjectData = frappe.db.sql("""select * from `tabList of Subjects`  where `tabList of Subjects`.subjectid  =  %s""",(subjectid),as_dict=True)

	jsonData = []
	for i in range(len(subjectData)):
		print(subjectData[i])
		jsonData.append({
			'subjectid': subjectData[i].subjectid,
			'subjectname': subjectData[i].subjectname

		})
	print(jsonData)
	return jsonData

def execute(filters=None):
	subjectData = get_subject_information(subjectid=filters.subjectid)



	columns = [
		{
			'fieldname': 'subjectid',
			'label': ('Subject ID'),
			'fieldtype': 'Link',
				"width": 300,
			'options': 'Subjects'
		},
		{
			'fieldname': 'subjectname',
			'label': ('Subject Name'),
			'fieldtype': 'Data',
			"width": 300,
			'options': ''
		},

	]
	data = subjectData
	return columns, data
