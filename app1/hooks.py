# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "app1"
app_title = "Meeting App"
app_publisher = "justine"
app_description = "App for Meeting"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "jjaycaneza@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/school_app/css/school_app.css"
# app_include_js = "/assets/school_app/js/school_app.js"

# include js, css files in header of web template
# web_include_css = "/assets/school_app/css/school_app.css"
# web_include_js = "/assets/school_app/js/school_app.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "school_app.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "school_app.install.before_install"
# after_install = "school_app.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "school_app.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	# "*": {
	# 	"on_update": "method",
	# 	"on_cancel": "method",
	# 	"on_trash": "method"
	# },

	# "Sales Invoice":{
	# 	"before_insert": "app1.hooks_method.calcAge"
	# }
}

# Scheduled Tasks
# ---------------

scheduler_events = {
	# "all": [
	# 	"school_app.tasks.all"
	# ],
	# "daily": [
	# 	"school_app.tasks.daily"
	# ],
	# "hourly": [
	# 	"school_app.tasks.hourly"
	# ],
	# "weekly": [
	# 	"school_app.tasks.weekly"
	# ]
	# "monthly": [
	# 	"school_app.tasks.monthly"
	# ]

	# "cron":{
	# 	"*/1 * * * *": [
     #        "app1.meeting_app.doctype.student_information.student_information.sayhi"
     #    ]
	# }

}

# Testing
# -------

# before_tests = "school_app.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "school_app.event.get_events"
# }



