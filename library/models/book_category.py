# -*- coding: utf-8 -*-
# 1 : imports of python lib
import logging

# 2 :  imports of odoo
# noinspection PyUnresolvedReferences
from odoo import api, fields, models

# 3 :  imports of odoo modules

# 4 :  imports from custom modules

_logger = logging.getLogger(__name__)


class BookCategory(models.Model):
    """ 
    Категория книги - жанр
    """

    # Private attributes
    # ------------------------------------------------------------------------------------------------------------------

    _name = 'book.category'
    _description = u'Категория книги - жанр'

    # Default methods
    # ------------------------------------------------------------------------------------------------------------------

    # Fields declaration
    # ------------------------------------------------------------------------------------------------------------------

    name = fields.Char(
        string='Категория',
    )
    """ Категория книги - жанр """

    books_ids = fields.Many2many(
        comodel_name='book.book',
        string='Книги',
    )
    """ Книги в категории """

    # Compute and search fields, in the same order of fields declaration
    # ------------------------------------------------------------------------------------------------------------------

    # Constraints and onchanges
    # ------------------------------------------------------------------------------------------------------------------

    # Action methods
    # ------------------------------------------------------------------------------------------------------------------

    # Business methods
    # ------------------------------------------------------------------------------------------------------------------

    # CRUD methods
    # ------------------------------------------------------------------------------------------------------------------
 