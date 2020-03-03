# -*- coding: utf-8 -*-

import os

from panel_components.component import Component


def b_container(*children, **attributes):
    return Component(*children, tag_name="b-container", **attributes)

def b_row(*children, **attributes):
    return Component(*children, tag_name="b-row", **attributes)

def b_col(*children, **attributes):
    return Component(*children, tag_name="b-col", **attributes)

def b_form_row(*children, **attributes):
    return Component(*children, tag_name="b-form-row", **attributes)
