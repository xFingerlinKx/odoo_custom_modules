# -*- coding: utf-8 -*-

##################################################################
# Стадии чтения книги
##################################################################

BOOK_STAGE_WANTED = 'wanted'
""" Стадия - Хочу прочитать """

BOOK_STAGE_IN_PROGRESS = 'in_progress'
""" Стадия - Читаю """

BOOK_STAGE_DONE = 'done'
""" Стадия - Книга прочитана """
# TODO: подумать еще над возможными стадиями - что-то типо отложено
#      (для книг, которые перестал читать)
BOOK_STAGES = [
    (BOOK_STAGE_WANTED, 'Хочу прочитать'),
    (BOOK_STAGE_IN_PROGRESS, 'Читаю'),
    (BOOK_STAGE_DONE, 'Книга прочитана'),
]

##################################################################
#
##################################################################
