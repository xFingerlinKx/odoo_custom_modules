# -*- coding: utf-8 -*-
# 1 : imports of python lib
import logging

# 2 :  imports of odoo
# noinspection PyUnresolvedReferences
from odoo import api, fields, models

# 3 :  imports of odoo modules

# 4 :  imports from custom modules
from . import constants

_logger = logging.getLogger(__name__)


class BookBook(models.Model):
    """ 
    Модель книги
    """

    # Private attributes
    # ------------------------------------------------------------------------------------------------------------------

    _name = 'book.book'
    _inherit = 'base_model.mixin'
    _description = u'Модель книги'

    # Default methods
    # ------------------------------------------------------------------------------------------------------------------

    # Fields declaration
    # ------------------------------------------------------------------------------------------------------------------

    name = fields.Char(
        string='Название книги',
        required=True,
    )
    """ Название книги """

    author = fields.Char(
        string='Автор',
        required=True,
    )
    """ Автор книги """
    # TODO: сделать можель авторов - res.users

    description = fields.Html(
        string='Описание книги',
    )
    """ Описание книги """

    date_publish = fields.Char(
        string='Год издания',
        size=4,
    )
    """ Год издания книги """
    # TODO: подумать, чтобы выводить только год (возможно придеться сделать Char или Integer)

    date_start = fields.Date(
        string='Начал читать',
    )
    """ Дата, когда начал читать книгу """

    date_finish = fields.Date(
        string='Окончил читать',
    )
    """ Дата, когда окончил читать книгу """

    image = fields.Binary(
        string='Обложка',
    )
    """ Картинка с обложкой книги """

    book_file = fields.Binary(
        string='Файл книги',
    )
    """ Файл книги """

    pages = fields.Integer(
        string='Количество страниц',
    )
    """ Количество страниц """

    category_id = fields.Many2one(
        comodel_name='book.category',
        string='Категория',
    )
    """ Категория книги """

    book_stage = fields.Selection(
        constants.BOOK_STAGES,
        string='Стадии',
        default=constants.BOOK_STAGE_WANTED,
    )
    """ Стадия - для выбора """

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