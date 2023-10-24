from odoo import http
from odoo.http import request
import json

class TicketForm(http.Controller):

    @http.route(['/ticket_type_description'], type='json', auth="public", website=True)
    def ticket_type_description(self, **kwargs):
        context = []
        default_description = ""
        selected_ticket_type = kwargs.get("selected_ticket_type")
        ticket_type = request.env['helpdesk.types'].sudo().browse(int(selected_ticket_type))
        if ticket_type:
            default_description = ticket_type.default_description
        """if group_value == '0':
            context = []
            tickets = request.env["help.ticket"].search([('user_id', '=', request.env.user.id)])
            context.append(tickets)
        if group_value == '1':
            context = []
            stage_ids = request.env['ticket.stage'].search([])
            for stage in stage_ids:
                ticket_ids = request.env['help.ticket'].search([
                    ('stage_id', '=', stage.id), ('user_id', '=', request.env.user.id)
                ])
                if ticket_ids:
                    context.append({
                        'name': stage.name,
                        'data': ticket_ids
                    })
        if group_value == '2':
            context = []
            type_ids = request.env['helpdesk.types'].search([])
            for types in type_ids:
                ticket_ids_1 = request.env['help.ticket'].search([
                    ('ticket_type', '=', types.id), ('user_id', '=', request.env.user.id)
                ])
                if ticket_ids_1:
                    context.append({
                        'name': types.name,
                        'data': ticket_ids_1
                    })
"""
        values = {
            'default_description': default_description,
        }
        return values