# Copyright (c) 2023, sydney and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class GymLockerBooking(Document):
	def before_save(self):
		exists = frappe.db.exists(
		"Gym Locker Booking",
			{
			"locker": self.locker,
			},
		)
		if exists:
		    frappe.throw(f'{self.locker} is already boooked')
