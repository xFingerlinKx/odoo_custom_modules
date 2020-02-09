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
    _description = u'Модель книги'

    # Default methods
    # ------------------------------------------------------------------------------------------------------------------

    # Fields declaration
    # ------------------------------------------------------------------------------------------------------------------

    name = fields.Char(
        string='Название книги',
        required=True,
        size=256,
    )
    """ Название книги """

    author_ids = fields.Many2many(
        comodel_name='book.author',
        string='Автор',
        required=True,
    )
    """ Автор книги """

    description = fields.Html(
        string='Описание книги',
    )
    """ Описание книги """

    date_publish = fields.Char(
        string='Год издания',
        size=4,
    )
    """ Год издания книги """

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

    category_ids = fields.Many2many(
        comodel_name='book.category',
        string='Категория',
    )
    """ Категория книги """
    # TODO: сделать категориями тэгами - many2many поле

    book_stage = fields.Selection(
        constants.BOOK_STAGES,
        string='Стадии',
        default=constants.BOOK_STAGE_WANTED,
    )
    """ Стадия - для выбора """

    active = fields.Boolean(
        string="Нет в архиве",
        default=True,
        track_visibility='onchange',
    )
    """ Нет в архиве """

    book_link = fields.Char(
        string='Ссылка на Oz.by',
    )
    """ Ссылка книги на Oz.by """

    # Compute and search fields, in the same order of fields declaration
    # ------------------------------------------------------------------------------------------------------------------

    # Constraints and onchanges
    # ------------------------------------------------------------------------------------------------------------------

    # Action methods
    # ------------------------------------------------------------------------------------------------------------------

    @api.multi
    def start_to_read(self):
        """
        Метод меняет стадию книги на - Читаю,
        проставляет дату начала чтения
        :return: True - результат записи - смены стадии
        """
        # noinspection PyUnresolvedReferences
        self.write({
            'book_stage': constants.BOOK_STAGE_IN_PROGRESS,
            'date_start': fields.Date.today(),
        })
        return True

    @api.multi
    def finish_to_read(self):
        """
        Метод меняет стадию книги на - Книга прочитана,
        проставляет дату окончания чтения
        :return: True - результат записи - смены стадии
        """
        # noinspection PyUnresolvedReferences
        self.write({
            'book_stage': constants.BOOK_STAGE_DONE,
            'date_finish': fields.Date.today(),
        })
        return True

    # Business methods
    # ------------------------------------------------------------------------------------------------------------------

    # CRUD methods
    # ------------------------------------------------------------------------------------------------------------------
