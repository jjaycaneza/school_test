# -*- coding: utf-8 -*-
# Copyright (c) 2019, justine and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
import datetime
class StudentInformation(Document):

	def validate(self):
		self.fullname = self.firstname + ' ' + self.middlename + ' ' + self.lastname
		self.studentid = self.name
	def calcAge(self):
		date = datetime.datetime.now()
		print("jsutine")
		print(self.birthdate)
		currentYear = date.strftime("%Y")
		birthdate_array = (self.birthdate).split("-")
		birthdate = datetime.datetime(int(birthdate_array[0]), int(birthdate_array[1]), int(birthdate_array[2]))
		age = int(currentYear) - int((birthdate).strftime("%Y"))
		print(int((birthdate).strftime("%Y")))
		print(int(currentYear))
		if(age == 0):


			return self,0
		else:

			return self,age

	def sayhi(self):
		import datetime
		date = '--2019'
		time = '13:07:09'

		date_time = date + "" + time
		x = datetime.datetime(2019,8,2,13,7,9)


		return x


@frappe.whitelist()
def student_information_validation(frm,mtd):
	import json

	print("age is "+str(frm.age))
	if(frm.age == 0):

		frappe.throw("You can't add a 0 year old human.")
	else:
		frappe.msgprint("Student Information Created")




