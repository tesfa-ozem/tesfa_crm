from odoo import api, fields, models


class CustomCrm(models.Model):
    _name = 'crm.lead'
    _description = 'New Description'
    _inherit = 'crm.lead'

    gender = fields.Selection(
        [('male', 'Male'), ('female', 'Female'), ], 'Gender', default='male')
    # tag_ids = fields.Many2many(
    #     'crm.tag', 'crm_tag_rel', 'crm.custom.tag_ids', 'tag_id', string='Tags',
    #     help="Classify and analyze your lead/opportunity categories like: Training, Service")
