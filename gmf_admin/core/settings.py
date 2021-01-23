# -*- coding: utf-8 -*-
from builtins import int

from qgis.core import QgsApplication, QgsProject
from qgis.PyQt.QtCore import QSettings


class UserSetting(object):
    """
    Property descriptor for plugin setting stored in QGIS user settings.
    """

    def __init__(self, name, type_=str, default=None):
        self.name = name
        self.type = type_
        self.default = default

    def __get__(self, instance, owner):
        """
        Get setting value from the QGIS user settings.
        """
        value = instance._qsettings.value(self.name, self.default, type=self.type)
        if self.type is str and value == '':
            return self.default
        return value

    def __set__(self, instance, value):
        """
        Store setting value in QGIS user settings.
        """
        instance._qsettings.setValue(self.name, value)

    def __delete__(self, instance):
        instance._qsettings.remove(self.name)


class ProjectSetting(object):
    """
    Property descriptor for plugin setting stored in QGIS project.
    """

    def __init__(self, name, type=str, default=None):
        self.name = name
        self.type = type
        self.default = default

    def __get__(self, instance, owner):
        if self.type == str:
            value, ok = QgsProject.instance().readEntry(instance.project_scope, self.name)
        elif self.type == int:
            value, ok = QgsProject.instance().readNumEntry(instance.project_scope, self.name)
        else:
            raise NotImplementedError("This setting type is not supported for the moment.")
        return value if ok else self.default

    def __set__(self, instance, value):
        QgsProject.instance().writeEntry(instance.project_scope, self.name, value)

    def __delete__(self, instance):
        QgsProject.instance().removeEntry(instance.project_scope, self.name)


class Settings(object):
    """
    Class responsible of storing and retrieving plugin settings.
    """

    group = 'gmf_admin'
    project_scope = 'gmf_admin'

    def __init__(self):
        self._qsettings = QSettings()
        self._qsettings.beginGroup(self.group)

        '''
        # Save defaults values in QgsSettings on first load
        for name, attr in self.__class__.__dict__.items():
            if isinstance(attr, UserSetting):
                setattr(self, name, getattr(self, name))
        '''

    gmf_url = UserSetting('gmf_url', str, None)
    ogc_server_id = ProjectSetting("ogc_server_id", int, 0)
    debug = UserSetting('debug', bool, False)

    @property
    def auth_token(self):
        return QgsApplication.authManager().authSetting("gmf_admin_auth_token", "", decrypt=True)

    @auth_token.setter
    def set_auth_token(self, value):
        QgsApplication.authManager.instance().storeAuthSetting("gmf_admin_auth_token", value, encrypt=True)

    def auth_token_exists(self):
        return QgsApplication.authManager.instance().existsAuthSetting("gmf_admin_auth_token")


settings = Settings()
