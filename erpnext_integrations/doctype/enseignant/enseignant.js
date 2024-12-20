// Copyright (c) 2024, Frappe Technologies Pvt. Ltd. and contributors
// For license information, please see license.txt

frappe.ui.form.on('Enseignant', {
  refresh: function(frm) {
    frm.add_custom_button(__('upload PDF'), function() {
      frappe.call({
        method: "frappe.utils.print_format.download_pdf",
        args: {
          doctype: frm.doc.doctype,
          name: frm.doc.name,  // Assurez-vous que name est correctement défini
          print_format: "fiche enseignant",
        }
      });
    });
  }
});



