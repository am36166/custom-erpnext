# Copyright (c) 2024, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Enseignant(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from erpnext.erpnext_integrations.doctype.encadrement.encadrement import Encadrement
		from erpnext.erpnext_integrations.doctype.enseignements.enseignements import Enseignements
		from frappe.types import DF

		cadre: DF.Data | None
		departement: DF.Data | None
		encadrement_licence: DF.Table[Encadrement]
		enseignements_cycle: DF.Table[Enseignements]
		etablissement: DF.Data | None
		grade: DF.Data | None
		is_published: DF.Check
		name: DF.Int | None
		nom: DF.Data | None
		periode_avancement_consideree: DF.Data | None
		prenom: DF.Data | None
		route: DF.Data | None
	# end: auto-generated types
	pass
