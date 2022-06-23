# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

bl_info = {
	"name": "Addon Updater Demo",
	"description": "Demo addon for showcasing the blender-addon-updater module",
	"author": "Patrick W. Crawford, neomonkeus",
	"version": (1, 4, 6),
	"blender": (3, 1, 0),
	"location": "View 3D > Tool Shelf > Demo Updater",
	"warning": "",
	"wiki_url": "https://github.com/CGCookie/blender-addon-updater",
	"tracker_url": "https://github.com/CGCookie/blender-addon-updater/issues",
	"category": "System"
}

from . import kaedimexporter
from . import addon_constructor


def register():
    kaedimexporter.register()
    addon_constructor.register()


def unregister():
    kaedimexporter.unregister()
    addon_constructor.unregister()

    