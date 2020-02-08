# -*- coding: utf-8 -*-
# 1 : imports of python lib
import logging

# 2 :  imports of odoo
# noinspection PyUnresolvedReferences
from odoo import api, fields, models

# 3 :  imports of odoo modules

# 4 :  imports from custom modules

_logger = logging.getLogger(__name__)


class BookAuthor(models.Model):
    """ 
    Автор книги
    (у книги может быть несколько авторов)
    """

    # Private attributes
    # ------------------------------------------------------------------------------------------------------------------

    _name = 'book.author'
    _description = u'Автор книги'

    # Default methods
    # ------------------------------------------------------------------------------------------------------------------

    # Fields declaration
    # ------------------------------------------------------------------------------------------------------------------

    first_name = fields.Char(
        string='Имя',
        required=True,
    )
    """ Имя автора книги """

    surname = fields.Char(
        string='Фамилия',
        required=True,
    )
    """ Фамилия автора книги """

    name = fields.Char(
        string='Автор',
        compute='_compute_author_name',
    )

    # Compute and search fields, in the same order of fields declaration
    # ------------------------------------------------------------------------------------------------------------------

    @api.model
    def _compute_author_name(self):
        """
        Метод возвращает полное имя автора Фамилия + Имя
        :return: basestring --> полное имя автора книги
        """
        # noinspection PyUnresolvedReferences
        for record in self:
            record.name = record.first_name + ' ' + record.surname

    # Constraints and onchanges
    # ------------------------------------------------------------------------------------------------------------------

    # Action methods
    # ------------------------------------------------------------------------------------------------------------------

    # Business methods
    # ------------------------------------------------------------------------------------------------------------------

    # CRUD methods
    # ------------------------------------------------------------------------------------------------------------------

    # def create(self):
    #     return res
    #
    # def write(self, vals):
    #     res = super(BookAuthor, self).write(vals)
    #     return res
