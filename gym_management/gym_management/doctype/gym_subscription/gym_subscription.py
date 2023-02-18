# Copyright (c) 2023, sydney and contributors
# For license information, please see license.txt

import frappe
from datetime import date
from frappe.model.document import Document

class GymSubscription(Document):
	def before_save(self):

		today_date = date.today()
		user = frappe.session.user

		# checking user membership well as activeness
		check_membership(user, today_date)

@frappe.whitelist()
def get_subscription_plan_fee(plan, doctype):
	fee = frappe.db.get_value(doctype, plan, 'fee')
	return fee

def check_membership(user, today_date):
	member_exist = frappe.db.exists(
	"Gym Membership",
		{
		"gym_member": user,
		},
	)
	
	if member_exist:
		member_is_not_active = frappe.db.exists(
						"Gym Membership",
							{
							"to_date": ('<', today_date),
							},
						)
		if member_is_not_active:			
			frappe.throw('Your Membership expired.')
	else:
		frappe.throw('Please contact the admin to give you Membership')		