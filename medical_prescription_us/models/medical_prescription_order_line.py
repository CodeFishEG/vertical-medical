# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import fields, models


class MedicalPrescriptionOrderLine(models.Model):
    _inherit = 'medical.prescription.order.line'
    refill_qty_original = fields.Float(
        string='Refill Qty',
        help='Amount of refills originally allowed in this prescription',
    )
    refill_qty_remain = fields.Float(
        string='Refill Remain',
        help='Amount of refills remaining in the prescription',
    )
