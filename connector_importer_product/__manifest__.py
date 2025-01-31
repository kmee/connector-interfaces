# Copyright 2022 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)
{
    "name": "Connector Importer Product",
    "summary": "Ease definition of product imports using `connector_importer`.",
    "version": "14.0.2.3.0",
    "category": "Tools",
    "website": "https://github.com/OCA/connector-interfaces",
    "author": "Camptocamp, Odoo Community Association (OCA)",
    "maintainers": ["simahawk", "sebalix", "mmequignon"],
    "development_status": "Alpha",
    "license": "AGPL-3",
    "depends": [
        # oca
        "connector_importer",
        # src
        "product",
    ],
    "data": [
        "data/import_type.xml",
    ],
    "demo": [
        "demo/import_backend.xml",
        "demo/import_source.xml",
        "demo/import_recordset.xml",
    ],
    "installable": True,
}
