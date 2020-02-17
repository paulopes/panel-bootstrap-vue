# -*- coding: utf-8 -*-

from panel_components.component import Component


def b_dropdown(*children, **attributes):
    return Component(*children, tag_name="b-dropdown", auto_id=True, **attributes)


def b_dropdown_item(*children, **attributes):
    return Component(*children, tag_name="b-dropdown-item", **attributes)


def b_dropdown_item_button(*children, **attributes):
    return Component(*children, tag_name="b-dropdown-item-button", **attributes)


def b_dropdown_divider(*children, **attributes):
    return Component(*children, tag_name="b-dropdown-divider", **attributes)


def b_dropdown_text(*children, **attributes):
    return Component(*children, tag_name="b-dropdown-text", **attributes)


def b_dropdown_form(*children, **attributes):
    return Component(*children, tag_name="b-dropdown-form", **attributes)


def b_dropdown_group(*children, **attributes):
    return Component(*children, tag_name="b-dropdown-group", **attributes)


def b_dropdown_header(*children, **attributes):
    return Component(*children, tag_name="b-dropdown-header", **attributes)
