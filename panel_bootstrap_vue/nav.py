# -*- coding: utf-8 -*-

import html

from panel_components.component import Component


def navbar(*children, title=None, **attributes):
    content = Component(
        *children,
        auto_id=True,
        tag_name="b-collapse",
        **{"is-nav": ""}
    )
    component = Component(
        content,
        tag_name="b-navbar",
        **attributes
    )
    if title:
        component.prepend_html('''
<b-navbar-brand href="#">''' + html.escape(title) + '</b-navbar-brand>')
    component.prepend_html('''
<b-navbar-toggle target="''' + content.id + '"></b-navbar-toggle>')
    return component


def b_navbar_nav(*children, **attributes):
    return Component(*children, tag_name="b-navbar-nav", **attributes)


def b_navbar_brand(*children, **attributes):
    return Component(*children, tag_name="b-navbar-brand", **attributes)


def b_nav_form(*children, **attributes):
    return Component(*children, tag_name="b-nav-form", **attributes)


def b_nav_item(*children, **attributes):
    return Component(*children, tag_name="b-nav-item", **attributes)


def b_nav_item_dropdown(*children, **attributes):
    return Component(*children, tag_name="b-nav-item-dropdown", **attributes)
