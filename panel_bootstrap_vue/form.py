# -*- coding: utf-8 -*-

from panel_components.component import Component


def b_form_input(*children, **attributes):
    return Component(*children, tag_name="b-form-input", **attributes)
