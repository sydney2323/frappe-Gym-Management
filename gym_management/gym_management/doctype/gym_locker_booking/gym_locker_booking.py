# Copyright (c) 2023, sydney and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from datetime import date

class GymLockerBooking(Document):
	def before_save(self):

		today_date = date.today()
		user = frappe.session.user

		# checking user membership well as activeness
		check_membership(user, today_date)

		# checking the has been boocked
		exists = frappe.db.exists(
		"Gym Locker Booking",
			{
			"locker": self.locker,
			},
		)
		if exists:
		    frappe.throw(f'{self.locker} is already boooked')

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

