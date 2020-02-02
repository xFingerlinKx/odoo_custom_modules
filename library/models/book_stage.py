# -*- coding: utf-8 -*-
# 1 : imports of python lib
import logging

# 2 :  imports of odoo 
from odoo import api, fields, models, _

# 3 :  imports of odoo modules

# 4 :  imports from custom modules

_logger = logging.getLogger(__name__)


class BookStage(models.Model):
    """ 
    Стадия чтения книги

    Например:
    - хочу прочитать;
    - читаю;
    - прочтена.
    """

    # Private attributes
    # ------------------------------------------------------------------------------------------------------------------

    _name = 'book.stage'
    _description = u'Стадия чтения книги'

    # Default methods
    # ------------------------------------------------------------------------------------------------------------------

    # Fields declaration
    # ------------------------------------------------------------------------------------------------------------------

    name = fields.Char(
        string='Стадия',
    )
    """ Стадия чтения книги """
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
 