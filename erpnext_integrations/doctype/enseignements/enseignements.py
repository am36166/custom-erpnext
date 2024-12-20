# Copyright (c) 2024, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Enseignements(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		annee_universitaire: DF.Data | None
		cours: DF.Float
		filiere: DF.Data | None
		parent: DF.Data
		parentfield: DF.Data
		parenttype: DF.Data
		semestre: DF.Data | None
		td: DF.Float
		tp: DF.Float
		vh: DF.Float
	# end: auto-generated types
	pass
