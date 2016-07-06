# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import _
from openerp import api, fields, models
from openerp.exceptions import ValidationError


class MedicalPatient(models.Model):
    _inherit = 'medical.patient'

    species_id = fields.Many2one(
        string='Species',
        required=True,
        comodel_name='medical.patient.species',
        default=lambda self: self.env.ref('medical_patient_species.human'),
        help='Select the species of the patient.',
    )
    is_person = fields.Boolean(
        related='species_id.is_person',
        help='Check if the party is a person.',
    )

    @api.multi
    @api.constrains('parent_id', 'species_id')
    def _check_parent_id(self):
        for record in self:
            if not record.is_person and not record.parent_id:
                raise ValidationError(
                    _('Must have a legal representative if not Human.')
                )

            elif record.parent_id and not record.parent_id.is_person:
                raise ValidationError(
                    _('Legal representative must be Human')
                )
