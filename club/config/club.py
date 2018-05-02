from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("All about the Teams"),
			"icon": "fa fa-users",
			"items": [
				{
					"type": "doctype",
					"name": "Team",
					"label": _("Teams"),
					"description": _("Teams"),
				},
				{
					"type": "doctype",
					"name": "Player",
					"label": _("Players"),
					"description": _("Players"),
				},
				{
					"type": "doctype",
					"name": "Trainer",
					"label": _("Trainers"),
					"description": _("Trainers"),
				},
				{
					"type": "doctype",
					"name": "Team Carer",
					"label": _("Team Carers"),
					"description": _("Team Carers"),
				},
			]
		},
		{
			"label": _("All about the Trainings"),
			"icon": "fa fa-building",
			"items": [
				{
					"type": "doctype",
					"name": "Sports Hall",
					"label": _("Sports Hall"),
					"description": _("Sports Hall"),
				}
			]
		},
		{
			"label": _("Events"),
			"icon": "fa fa-building",
			"items": [
				{
					"type": "doctype",
					"name": "Club Event",
					"label": _("Event"),
					"description": _("Sport Events"),
				}
			]
		},
		{
			"label": _("Member and Sponsors"),
			"icon": "fa fa-hand-holding-usd",
			"items": [
				{
					"type": "doctype",
					"name": "Sponsor",
					"label": _("Sponsor"),
					"description": _("Sponsor"),
				},
				{
					"type": "doctype",
					"name": "Club Member",
					"label": _("Member"),
					"description": _("Member"),
				}
			]
		},
		{
			"label": _("Financial"),
			"icon": "fa fa-hand-holding-usd",
			"items": [
				{
					"type": "doctype",
					"name": "Club Invoice",
					"label": _("Invoice"),
					"description": _("Invoice"),
				}
			]
		},
		{
			"label": _("Reports"),
			"icon": "fa fa-hand-holding-usd",
			"items": [
				{
					"type": "report",
					"is_query_report": True,
					"name": "Players",
					"doctype": "Team"
				}
			]
		}
	]