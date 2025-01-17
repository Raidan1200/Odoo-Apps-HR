{
    "name": "HR Holidays Custom Hours",
    "summary": """
        Set a custom duration on time-off request.
    """,
    "author": "Mint System GmbH, Odoo Community Association (OCA)",
    "website": "https://www.mint-system.ch",
    "category": "Human Resources",
    "version": "16.0.1.0.0",
    "license": "AGPL-3",
    "depends": ["hr_holidays_attendance"],
    "data": [
        "views/hr_leave_type_views.xml",
        "views/hr_leave_views.xml",
    ],
    "installable": True,
    "application": False,
    "auto_install": False,
    "images": ["images/screen.png"],
}
