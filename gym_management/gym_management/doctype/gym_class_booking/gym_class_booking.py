# Copyright (c) 2023, sydney and contributors
# For license information, please see license.txt

import frappe
from datetime import date
from frappe.model.document import Document

class GymClassBooking(Document):
	def before_save(self):

		today_date = date.today()
		user = frappe.session.user

		# checking user membership well as activeness
		check_membership(user, today_date)


def check_membership(user, today_date):
	exists = frappe.db.exists(
	"Gym Membership",
		{
		"gym_member": user,
		"to_date": ('<', today_date),
		},
	)
	if exists:
		frappe.throw('Your not an active member in our Gym. Please contact the admin to give you Membership')