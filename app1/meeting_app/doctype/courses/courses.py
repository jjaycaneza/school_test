# -*- coding: utf-8 -*-
# Copyright (c) 2019, justine and contributors
# For license information, please see license.txt


from __future__ import unicode_literals
import frappe
from frappe.model.document import Document


class Courses(Document):
	# def getstudentsenrolled(self):
    #
    #
	# 	studentid = self.studentsenrolled[0].studentid
	# 	studentData = frappe.db.sql("""select * from `tabStudent Information` where name = %s""", (studentid),
	# 								as_dict=True)
    #
	# 	print(studentData)
	# 	return studentData, studentid
	def sayhi(self):
		return "hi"




@frappe.whitelist()
def get_student_information(row_data):
	print("teeestt")

	print(str(row_data))

	studentData = frappe.db.sql("""select * from `tabStudent Information` where name = %s""", (row_data),as_dict=True)

	return studentData

@frappe.whitelist()
def get_list_of_subject(row_data):

	print("hey")
	print(row_data)
	subjectData = frappe.db.sql("""select * from `tabSubjects` where name = %s""", (row_data),as_dict=True)

	return subjectData
@frappe.whitelist()
def doingValidation(s,f):
	print("validation")
	frappe.msgprint()
