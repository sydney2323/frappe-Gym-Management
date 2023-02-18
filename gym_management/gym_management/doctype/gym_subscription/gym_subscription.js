// Copyright (c) 2023, sydney and contributors
// For license information, please see license.txt

frappe.ui.form.on("Gym Subscription", {
	refresh(frm) {

        frappe.call('gym_management.gym_management.doctype.gym_subscription_plan.gym_subscription_plan.my_method', {
            plan: frm.doc.plan
        }).then(r => {
            // console.log(r.message)
            if (frm.doc.plan == 'Daily') {

                frm.set_value('fee', r.message);

            } else if (frm.doc.plan == 'Weekly') {

                fee = r.message * 7
                frm.set_value('fee', fee);

            } else if (frm.doc.plan == 'Monthly') {
                
                fee = r.message * 30
                frm.set_value('fee', fee);

            } else{

                fee = r.message * 360
                frm.set_value('fee', fee);
                
            }
        });

	},

    

});

