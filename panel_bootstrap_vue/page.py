# -*- coding: utf-8 -*-

import os

from panel_components.utils import IS_A_JUPYTER_NOTEBOOK
from panel_components.vue import vue


def page(*children, **attributes):
    if IS_A_JUPYTER_NOTEBOOK:
        component = vue("", *children, style="height: 80vh", **attributes)
    else:
        component = vue("", *children, **attributes)
    (
        component
        .asset_folders(
            os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets")
        )
        .prepend_body_css(bootstrap="bootstrap/bootstrap.min.css")
        .prepend_body_css(
            typography="typography/core.css",
            bootstrap_vue="vue/bootstrap-vue.min.css",
        )
        .append_body_js(
            bootstrap_vue="vue/bootstrap-vue.min.js",
            bootstrap_vue_icons="vue/bootstrap-vue-icons.min.js",
            portal_vue="vue/portal-vue.umd.min.js",
        )
        .append_body_script(bootstrap_vue='Vue.use(BootstrapVue);Vue.use(BootstrapVueIcons)')
    )
    return component
