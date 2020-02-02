# -*- coding: utf-8 -*-
# 1 : imports of python lib
import logging

# 2 :  imports of odoo
# noinspection PyUnresolvedReferences
from odoo import api, fields, models

# 3 :  imports of odoo modules

# 4 :  imports from custom modules

_logger = logging.getLogger(__name__)


class BaseModelMixin(models.Model):
    """ 
    Базовый моедль Миксин для моделей
    """

    _name = 'base_model.mixin'
    _description = u'Базовый моедль Миксин для моделей'

    # Default methods
    # ------------------------------------------------------------------------------------------------------------------

    # Fields declaration
    # ------------------------------------------------------------------------------------------------------------------

    active = fields.Boolean(
        string='Архивная запись',
        defaut=False,
    )
    """ Архивная запись """
