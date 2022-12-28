# Copyright 2022 Ecosoft Co., Ltd. (http://ecosoft.co.th)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "ThaiEV: Config",
    "version": "14.0.1.0.0",
    "license": "AGPL-3",
    "category": "Thai EV",
    "author": "Ecosoft",
    "installable": True,
    "depends": [
        "purchase",
        "purchase_request",
        "web_m2x_options",
    ],
    "data": [
        "security/ir.model.access.csv",
        "data/ir_actions_server_data.xml",
        "data/ir.config_parameter.csv",
        "data/tier_definition_data.xml",
        "views/account_views.xml",
    ],
}
