#  ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# ##### END GPL LICENSE BLOCK #####

import bpy


class ThreeJoint:
    def __init__(self, objs, rest, ready, up, hit):
        """
        Initializes three joint arm.
        :param objs: List of objects: [joint1, joint2, joint3]
        :param rest: List of euler rotations for rest [joint1, joint2, joint3]
        :param ready: List of euler rotations for ready [joint1, joint2, joint3]
        :param up: List of euler rotations for up stroke [joint1, joint2, joint3]
        :param hit: List of euler rotations for hit [joint1, joint2, joint3]
        """
        self.objs = objs
        self.rotations = {
            "rest": rest,
            "ready": ready,
            "up": up,
            "hit": hit,
        }