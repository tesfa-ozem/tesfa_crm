from odoo import api, fields, models
import requests
from requests.exceptions import HTTPError

class SlackIntegration(models.Model):
    _name = 'crm.lead'
    _description = 'Slack'
    _inherit = 'crm.lead'


    @api.model
    def create(self, vals):
        requests.post('https://hooks.slack.com/services/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', data={'key':'value'})
        resp = super().create(vals)
        
        return resp