from odoo import api, fields, models
import requests
from requests.exceptions import HTTPError


class SlackIntegration(models.Model):
    _name = 'crm.lead'
    _description = 'Slack'
    _inherit = 'crm.lead'

    @api.model
    def create(self, vals):
        print(vals)
        try:
            response = requests.post(
                'https://hooks.slack.com/services/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',
                json={"text": "Hey Jenga\n You have a new applicant"})
            
        # If the response was successful, no Exception will be raised
            response.raise_for_status()
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')  # Python 3.6
        except Exception as err:
            print(f'Other error occurred: {err}')  # Python 3.6
        else:
            print('Success!')
        resp = super().create(vals)
        return resp
