import frappe

def update_custom_status_in_document(doc, method):
	if doc.get('status'):
		doc.form_status = doc.status

def update_status():
	for doctype in ['Sales Order', 'Sales Invoice', 'Purchase Order',
		'Purchase Invoice', 'Purchase Receipt', 'Delivery Note', 'Payment Entry']:
		if frappe.db.has_column(doctype, "status"):
			frappe.db.sql(f''' Update `tab{doctype}`
				SET form_status = status
				WHERE
					(form_status is null or form_status != status)
			''')