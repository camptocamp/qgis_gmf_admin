# -*- coding: utf-8 -*-
"""
/***************************************************************************
 GMFSynchronizer
                                 A QGIS plugin
 Synchronize GMF layer tree with QGIS project
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2021-01-22
        copyright            : (C) 2021 by Camptocamp
        email                : info@camptocamp.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load GMFSynchronizer class from file GMFSynchronizer.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .gmf_admin_plugin import GMFAdminPlugin
    return GMFAdminPlugin(iface)
