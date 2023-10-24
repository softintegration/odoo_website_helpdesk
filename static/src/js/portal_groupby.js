odoo.define("odoo_website_helpdesk.portal_group_by", function (require) {
    "use strict";
    var ajax = require('web.ajax');
    var core = require('web.core');
    var QWeb = core.qweb;

    $("#group_select").on('change', function () {
    var search_value = $("#group_select").val();
    ajax.jsonRpc('/ticketgroupby', 'call', {
                'search_value': search_value,
            }).then(function(result) {
                $('.search_ticket').html(result);
                });
    })

    /*$("#ticket_type").on('change', function () {
    var selected_ticket_type = $("#ticket_type").val();
    ajax.jsonRpc('/ticket_type_description', 'call', {
                'selected_ticket_type': selected_ticket_type,
            }).then(function(result) {
                $('#detail_description').html(result.default_description);
                });
    })*/

})