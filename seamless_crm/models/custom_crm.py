from odoo import api, fields, models


class CustomCrm(models.Model):
    _name = 'crm.lead'
    _description = 'New Description'
    _inherit = 'crm.lead'

    number_of_employees = fields.Char('Number of Employees')
    company_type = fields.Char('Company type')
    customer_timeline = fields.Char('Timeline')
    system_used = fields.Char('System used')
    pain_points = fields.Char('Pain point')
    next_step = fields.Char('Next step')
    contract_date = fields.Char('Contract')
    feedback = fields.Char('Feedback')
    # tag_ids = fields.Many2many(
    #     'crm.tag', 'crm_tag_rel', 'crm.custom.tag_ids', 'tag_id', string='Tags',
    #     help="Classify and analyze your lead/opportunity categories like: Training, Service")
    
