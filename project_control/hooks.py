# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "project_control"
app_title = "Project Control"
app_publisher = "9T9IT"
app_description = "An ERPNext app"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "info@9t9it.com"
app_license = "MIT"

fixtures = [
    {
        "doctype": "Custom Field",
        "filters": [
            [
                "name",
                "in",
                [
                    "Project-naming_series",
                    "Project-pc_budget_sb",
                    "Project-pc_budgets",
                    "Project-pc_budget_total",
                    "Project-pc_budget_cb",
                    "Project-pc_variations",
                    "Project-pc_variation_total",
                    "Project-pc_estimated_total",
                    "Project-pc_estimated_gross_margin",
                    "Purchase Order-project",
                    "Purchase Invoice-project",
                    "Project-pc_total_journal_entry",
                    "Project-pc_total_delivery_note",
                    "Project-pc_per_unbilled",
                    "Employee-pc_gratuity_paid_till_date",
                    "Employee-pc_gratuity_till_date",
                    "Project-pc_order_value",
                    "Project-pc_sales_person",
                    "Installation Note-project",
                    "Project-pc_sales_person_name",
                    "Project-pc_estimated_gross_margin_per",
                    "Stock Entry-pc_stock_item_issue"
                ]
            ]
        ]
    }
]

doctype_js = {
    "Project": "public/js/project.js",
    "Purchase Order": "public/js/purchase_order.js"
}

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
    "Project": {
        "validate": "project_control.doc_events.project.validate",
        "after_insert": "project_control.doc_events.project.after_insert"
    },
    "Purchase Invoice": {
        "validate": [
            "project_control.doc_events.purchase_invoice.validate",
            "project_control.doc_events.update_custom_status.update_custom_status_in_document"
        ]
    },
    "Purchase Order": {
        "validate": [
            "project_control.doc_events.purchase_order.validate",
            "project_control.doc_events.update_custom_status.update_custom_status_in_document"
        ]
    },
    "Stock Entry": {
        "validate": "project_control.doc_events.stock_entry.validate"
    },
    "Expense Claim": {
        "validate": "project_control.doc_events.expense_claim.validate"
    },
    "Delivery Note": {
        "validate": [
            "project_control.doc_events.delivery_note.validate",
            "project_control.doc_events.update_custom_status.update_custom_status_in_document"
        ]
    },
    "GL Entry": {
        "validate": "project_control.doc_events.gl_entry.validate"
    },
    "Sales Order": {
        "validate": "project_control.doc_events.update_custom_status.update_custom_status_in_document"
    },
    "Sales Invoice": {
        "validate": "project_control.doc_events.update_custom_status.update_custom_status_in_document"
    },
    "Purchase Receipt": {
        "validate": "project_control.doc_events.update_custom_status.update_custom_status_in_document"
    },
    "Payment Entry": {
        "validate": "project_control.doc_events.update_custom_status.update_custom_status_in_document"
    },
    "Payment Request": {
        "validate": "project_control.doc_events.update_custom_status.update_custom_status_in_document"
    }
}

# Scheduled Tasks
# ---------------

scheduler_events = {
    "hourly": [
        "project_control.scheduler_events.hourly.set_estimated_gross_margin",
        "project_control.scheduler_events.hourly.set_gross_gratuity"
    ],

    "all": [
        "project_control.doc_events.update_custom_status.update_status"
    ]
}
# scheduler_events = {
# 	"all": [
# 		"project_control.tasks.all"
# 	],
# 	"daily": [
# 		"project_control.tasks.daily"
# 	],
# 	"hourly": [
# 		"project_control.tasks.hourly"
# 	],
# 	"weekly": [
# 		"project_control.tasks.weekly"
# 	]
# 	"monthly": [
# 		"project_control.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "project_control.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "project_control.event.get_events"
# }
