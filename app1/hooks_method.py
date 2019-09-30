import frappe
import json
import datetime
@frappe.whitelist()
def calcAge():

    self = frappe.form_dict

    cust_data_json = json.loads(self.self)
    print(cust_data_json)
    print((cust_data_json['customer']))
    customerData = frappe.db.sql("""select * from `tabCustomer` where `tabCustomer`.`customer_name` = %s""",
                                 (cust_data_json['customer']), as_dict=True)

    date = datetime.datetime.now()

    currentYear = date.strftime("%Y")

    birthdate_array = str((customerData[0].birthdate)).split("-")

    birthdate = datetime.datetime(int(birthdate_array[0]), int(birthdate_array[1]), int(birthdate_array[2]))
    age = int(currentYear) - int((birthdate).strftime("%Y"))
    print(int((birthdate).strftime("%Y")))

    self.age = age

    print(int(currentYear))
    if (age == 0):

        return cust_data_json,age
    else:

        return cust_data_json,age
