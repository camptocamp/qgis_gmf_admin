# -*- coding: utf-8 -*-
"""
/***************************************************************************
 GMFSynchronizerDialog
                                 A QGIS plugin
 Synchronize GMF layer trree with QGIS project
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2021-01-22
        git sha              : $Format:%H$
        copyright            : (C) 2021 by Camptocamp
        email                : info@camptocamp.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

from pkg_resources import resource_filename

from qgis.PyQt import uic
from qgis.PyQt import QtWidgets

from gmf_admin.core.settings import settings

# This loads your .ui file so that PyQt can populate your plugin with the elements from Qt Designer
FORM_CLASS, _ = uic.loadUiType(
    resource_filename("gmf_admin", "ui/settings_dialog_base.ui"),
    from_imports=True,
    import_from='gmf_admin',
)


class SettingsDialog(QtWidgets.QDialog, FORM_CLASS):

    def __init__(self, parent=None):
        super(SettingsDialog, self).__init__(parent)
        self.setupUi(self)
        self.authTokenLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.authTokenLineEdit.textEdited.connect(self.auth_token_edited)
        self.has_to_save_auth_token = False
        self.load_settings()

    def load_settings(self):
        self.gmfUrlLineEdit.setText(settings.gmf_url)
        self.authTokenLineEdit.setText("******")
        self.ogcServerIdSpinBox.setValue(settings.ogc_server_id)
        self.debugCheckBox.setChecked(settings.debug)

    def auth_token_edited(self):
        self.has_to_save_auth_token = True

    def save_settings(self):
        settings.gmf_url = self.gmfUrlLineEdit.text()
        if self.has_to_save_auth_token:
            settings.auth_token = self.authTokenLineEdit.text()
        settings.ogc_server_id = self.ogcServerIdSpinBox.value()
        settings.debug = self.debugCheckBox.isChecked()

    def accept(self, *args, **kwargs):
        self.save_settings()
        super(SettingsDialog, self).accept(*args, **kwargs)
