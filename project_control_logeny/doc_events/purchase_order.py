from project_control_logeny.data import validate_project_costing


def validate(order, method):
    if order.project:
        validate_project_costing(order.project, order.base_grand_total)

