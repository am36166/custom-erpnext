frappe.ready(function () {
    frappe.web_form.after_save = () => {
        let actual_doctype = 'Enseignant'; // Doctype lié au formulaire

        // Récupérer le dernier document créé par l'utilisateur
        frappe.call({
            method: 'frappe.client.get_list',
            args: {
                doctype: actual_doctype,
                filters: { owner: frappe.session.user }, // Documents créés par l'utilisateur actuel
                fields: ['name'],
                limit_page_length: 1,
                order_by: 'creation desc' // Récupérer le plus récent
            },
            callback: function (response) {
                if (response.message && response.message.length > 0) {
                    let docname = response.message[0].name;

                    // Générer l'URL pour le PDF
                    let pdf_url = `/api/method/frappe.utils.print_format.download_pdf?doctype=${actual_doctype}&name=${docname}&format=fiche enseignant`;

                    // Ouvrir le PDF dans un nouvel onglet
                    window.open(pdf_url, '_blank');
                } else {
                    frappe.msgprint('Aucun document récent trouvé.');
                }
            }
        });
    };
});
