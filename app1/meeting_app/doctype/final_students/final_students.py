# -*- coding: utf-8 -*-
# Copyright (c) 2019, justine and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class FinalStudents(Document):
	pass
@frappe.whitelist()
def get_final_students(row_data):

	studentData = frappe.db.sql("""select * from `tabStudent Information` where `tabStudent Information`.`course` = %s""", (row_data),as_dict=True)

	return studentData

