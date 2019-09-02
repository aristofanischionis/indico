# This file is part of Indico.
# Copyright (C) 2002 - 2019 CERN
#
# Indico is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see the
# LICENSE file for more details.

from __future__ import unicode_literals

from indico.core.marshmallow import mm
from indico.modules.categories import Category
from indico.modules.events import Event
from indico.web.flask.util import url_for


def _get_category_path(chain):
    chain = chain[1:-1]  # strip root/self
    return [
        dict(c, url=url_for('categories.display', category_id=c['id']))
        for c in chain
    ]


class CategoryResultSchema(mm.ModelSchema):
    class Meta:
        model = Category
        fields = ('id', 'title', 'url', 'path')

    path = mm.Function(lambda cat: _get_category_path(cat.chain))


class EventResultSchema(mm.ModelSchema):
    class Meta:
        model = Event
        fields = ('id', 'title', 'url', 'type', 'start_dt', 'end_dt', 'category_path')

    category_path = mm.Function(lambda event: _get_category_path(event.detailed_category_chain))