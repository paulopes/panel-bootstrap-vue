# -*- coding: utf-8 -*-

from panel_components.component import Component


def b_button(*children, **attributes):
    return Component(*children, tag_name="b-button", **attributes)
