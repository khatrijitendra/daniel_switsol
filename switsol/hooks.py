# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "switsol"
app_title = "Switsol"
app_publisher = "Switsol"
app_description = "Switsol"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "jitendra.k@indictranstech.com"
app_license = "MIT"
boot_session = "switsol.boot.boot_session"
# Includes in <head>
# ------------------

# include js, css files in header of desk.html
app_include_css = "/assets/js/switsol.desk.min.css"
app_include_js = "/assets/js/switsol.desk.min.js"



fixtures = ['Custom Field', 'Property Setter', "Print Format","Custom Script"]
# include js, css files in header of web template
# web_include_css = "/assets/switsol/css/switsol.css"
# web_include_js = "/assets/switsol/js/switsol.js"

doctype_js = {
    "Customer":["custom_script/customer.js"],
    "Contact":["custom_script/contact.js"],
    "Employee":["custom_script/employee.js"],
    "Sales Partner":["custom_script/sales_sartner"],
    "Supplier":["custom_script/supplier.js"],
    "Timesheet":["custom_script/timesheet.js"],
    "User":["custom_script/user.js"],
    "Quotation":["custom_script/quotation.js"],
    "Sales Order":["custom_script/sales_order.js"]
}
#"Project":["custom_script/project.js"],



# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "switsol.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "switsol.install.before_install"
# after_install = "switsol.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "switsol.notifications.get_notification_config"

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

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"switsol.tasks.all"
# 	],
# 	"daily": [
# 		"switsol.tasks.daily"
# 	],
# 	"hourly": [
# 		"switsol.tasks.hourly"
# 	],
# 	"weekly": [
# 		"switsol.tasks.weekly"
# 	]
# 	"monthly": [
# 		"switsol.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "switsol.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "switsol.event.get_events"
# }
override_whitelisted_methods = {
    "frappe.utils.print_format.download_pdf":"switsol.custom_script.project.download_pdf"
}
