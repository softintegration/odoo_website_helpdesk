odoo.define("odoo_website_helpdesk.ticket_form", function (require) {
    "use strict";
    var ajax = require('web.ajax');
    var core = require('web.core');
    var QWeb = core.qweb;



    $("#ticket_type").on('change', function () {
    var selected_ticket_type = $("#ticket_type").val();
    ajax.jsonRpc('/ticket_type_description', 'call', {
                'selected_ticket_type': selected_ticket_type,
            }).then(function(result) {
                $('#detail_description').html(result.default_description);
                });
    })

})