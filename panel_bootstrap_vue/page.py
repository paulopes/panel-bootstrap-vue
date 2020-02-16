# -*- coding: utf-8 -*-

import os

from panel_components.vue import vue_app


def page(*children, **attributes):

    component = vue_app("", *children, **attributes)
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
            # bootstrap_vue_icons="vue/bootstrap-vue-icons.min.js",
            portal_vue="vue/portal-vue.min.js",
        )
        .append_body_script(bootstrap_vue=';Vue.use(BootstrapVue);')
    )
    return component
