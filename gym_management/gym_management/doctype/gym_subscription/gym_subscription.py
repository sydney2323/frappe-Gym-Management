# Copyright (c) 2023, sydney and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class GymSubscription(Document):
	pass

@frappe.whitelist()
def get_subscription_plan_fee(plan, doctype):
	fee = frappe.db.get_value(doctype, plan, 'fee')
	return fee

