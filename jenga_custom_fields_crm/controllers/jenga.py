from werkzeug.exceptions import Forbidden
from werkzeug.urls import url_encode

from odoo import _
from odoo import http, tools
from odoo.http import Controller, request, route

class JengaController(http.Controller):
    @http.route('/jenga/create_lead', type='json', auth="none")
    def jenga_create_lead(self):
        return "hello world"