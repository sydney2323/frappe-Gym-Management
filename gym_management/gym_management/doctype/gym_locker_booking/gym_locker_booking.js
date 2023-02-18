// Copyright (c) 2023, sydney and contributors
// For license information, please see license.txt


frappe.ui.form.on("Gym Locker Booking", {
	onload(frm) {
        frm.set_value('full_name', frappe.user.name);
	},
});
