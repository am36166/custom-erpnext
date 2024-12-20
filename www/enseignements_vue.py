from frappe import frappe

def get_context(context):
    query = """
    SELECT 
        e.nom AS nom,
        e.prenom AS prenom,
        e.departement AS departement,
        e.grade AS grade,
        e.etablissement AS etablissement,
        e.periode_avancement_consideree AS periode_avancement,
        ens.annee_universitaire AS annee_universitaire,
        ens.filiere AS filiere,
        ens.semestre AS semestre,
        ens.td AS td,
        ens.tp AS tp,
        ens.cours AS cours
    FROM 
        tabEnseignant AS e
    JOIN 
        tabEnseignements AS ens
    """

    res = frappe.db.sql(query, as_dict=True)

    # Organisation des données par enseignant
    enseignant_data = {}
    for row in res:
        nom = row['nom']  # Extraire le nom de l'enseignant
        if nom not in enseignant_data:
            enseignant_data[nom] = {
                "prenom": row["prenom"],
                "grade": row["grade"],
                "periode_avancement": row["periode_avancement"],
                "etablissement": row["etablissement"],
                "enseignements": []
            }
        enseignant_data[nom]["enseignements"].append({
            "annee_universitaire": row['annee_universitaire'],
            "filiere": row['filiere'],
            "semestre": row['semestre'],
            "td": row['td'],
            "tp": row['tp'],
            "cours": row['cours']
        })

    context.enseignant_data = enseignant_data