# Copyright (c) 2024, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Encadrement(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		annee_universitaire: DF.Data | None
		etudiants: DF.Data | None
		nom_encadrants: DF.Data | None
		parent: DF.Data
		parentfield: DF.Data
		parenttype: DF.Data
		titre_pfe: DF.Data | None
		type_licence: DF.Data | None
	# end: auto-generated types
	pass
