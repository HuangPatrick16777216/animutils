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
from .midi import XMido
from .anim import *


class ThreeJoint:
    def __init__(self, objs: tuple, rest: tuple, ready: tuple, up: tuple, hit: tuple) -> None:
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

    def animate(self, xmido: XMido, notes: list, fps: int, offset: int, rest_margin: int) -> None:
        """
        Animates arm.
        :param xmido: Extensive mido object.
        :param notes: List of notes to take as belonging to this instrument.
        :param fps: Fps of animation.
        :param offset: Offset of animation start.
        :param rest_margin: Time (frames) to enter into rest if not playing.
        """
        messages = xmido.parse(fps, offset)
        messages = [msg for msg in messages if msg["note"] in notes]

        resting = True
        prev_hit = float("-inf")
        for i, msg in enumerate(messages):
            volume, frame = msg.volume, msg.time
            next_hit = float("inf")
            for m in messages[i+1:]:
                if m.volume > 0:
                    next_hit = m.time
                    break

            if volume > 0:
                # Before hit
                if resting:
                    self._unrest()
                    resting = False

                # Hit
                begin = (frame-prev_hit) > 30
                end = (next_hit-frame) > 30
                self._hit(frame, prev_hit, next_hit)

                # After hit
                if next_hit - frame > rest_margin:
                    self._rest()
                    resting = True
                prev_hit = frame
