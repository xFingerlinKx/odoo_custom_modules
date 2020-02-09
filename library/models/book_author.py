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
        readonly=True,
    )

    books_ids = fields.Many2many(
        comodel_name='book.book',
        string='Книги',
    )
    """ Книги """

    # Compute and search fields, in the same order of fields declaration
    # ------------------------------------------------------------------------------------------------------------------

    # Constraints and onchanges
    # ------------------------------------------------------------------------------------------------------------------

    # Action methods
    # ------------------------------------------------------------------------------------------------------------------

    # Business methods
    # ------------------------------------------------------------------------------------------------------------------

    @api.model
    def _get_author_name(self, vals):
        """
        Метод для получения полного имени автора - фамилия + имя
        :param vals: словарь создаваемых значений
        :return basestring: полное имя автора
        """
        # TODO: сделать методы для очистки от пробелов и цифр
        vals['name'] = vals.get('surname') + ' ' + vals.get('first_name')
        return vals['name']

    # CRUD methods
    # ------------------------------------------------------------------------------------------------------------------

    @api.model
    def create(self, vals):
        self._get_author_name(vals)
        res = super(BookAuthor, self).create(vals)
        return res

    def write(self, vals):
        self._get_author_name(vals)
        res = super(BookAuthor, self).write(vals)
        return res
