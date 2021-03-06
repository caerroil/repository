# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Coordinate
                                 A QGIS plugin
 Restituisce le coordinate date
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2018-06-20
        copyright            : (C) 2018 by luca
        email                : lucacaliciotti@gmail.com
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
    """Load Coordinate class from file Coordinate.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .coordinate import Coordinate
    return Coordinate(iface)
