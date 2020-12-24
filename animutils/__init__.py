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

import sys
import mido


class XMido:
    """Extended single track midi object (uses mido)"""

    def __init__(self, path):
        """
        Initializes midi object. Only the first track of the midi will be used.
        :param path: Path of midi file.
        """
        self.midi = mido.MidiFile(path)
        self.track = self.midi.tracks[0]

    def parse(self, fps, offset):
        """
        Removes meta messages and changes timescale to absolute frames.
        :param fps: Frames per second of animation.
        :param offset: Number of frames to offset
        """
        tempo = 500000
        num_msgs = len(self.track)
        final = []
        frame = offset

        sys.stdout.write(f"Parsing {num_msgs}...")
        for i, msg in enumerate(self.track):
            print_msg = f"Message {i} of {num_msgs}"
            sys.stdout.write(print_msg)
            sys.stdout.flush()
            sys.stdout.write("\b" * len(print_msg))
            sys.stdout.write(" " * len(print_msg))
            sys.stdout.write("\b" * len(print_msg))

            if msg.is_meta:
                frame += msg.time / self.midi.ticks_per_beat * tempo / 1000000 * fps

                if msg.type == "set_tempo":
                    tempo = msg.tempo
                else:
                    if msg.type == "note_on":
                        curr_note = {}
                        curr_note["note"] = msg.note
                        curr_note["volume"] = msg.velocity
                        curr_note["time"] = frame

        sys.stdout.write("\nFinished parsing messages.\n")
        sys.stdout.flush()