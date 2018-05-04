# -*- coding: utf-8 -*-
# Copyright (c) 2018, libracore GmbH and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe

@frappe.whitelist()
def create_player(name):
	player = frappe.new_doc("Player")
	player.contact = name
	player.save()
	
	return player