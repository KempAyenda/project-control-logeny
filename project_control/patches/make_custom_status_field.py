import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields

def execute():
	custom_fields = {}

	for doctype in ['Sales Order', 'Sales Invoice', 'Purchase Order',
		'Purchase Invoice', 'Purchase Receipt', 'Delivery Note', 'Payment Entry', 'Payment Request']:
		custom_fields[doctype] = [
			dict(fieldname='form_status', label='Document Status', in_list_view=1,
				fieldtype='Data', hidden=1, read_only=1, insert_after='company', allow_on_submit=1)
		]

	create_custom_fields(custom_fields, update=True)