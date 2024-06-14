from django.utils.translation import gettext_lazy as _

from netbox.plugins import PluginMenu, PluginMenuButton, PluginMenuItem

menu = PluginMenu(
    label='Branching',
    groups=(
        (_('Branches'), (
            PluginMenuItem(
                link='plugins:netbox_vcs:branch_list',
                link_text=_('Branches'),
                buttons=(
                    PluginMenuButton('plugins:netbox_vcs:branch_add', _('Add'), 'mdi mdi-plus-thick'),
                    PluginMenuButton('plugins:netbox_vcs:branch_import', _('Import'), 'mdi mdi-upload'),
                )
            ),
            PluginMenuItem(
                link='plugins:netbox_vcs:changediff_list',
                link_text='Changes'
            ),
        )),
    ),
    icon_class='mdi mdi-source-branch'
)
