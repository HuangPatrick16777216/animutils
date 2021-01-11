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

import math
import bpy


def anim_pass_ind(obj, value, frame, handle="AUTO_CLAMPED", type="KEYFRAME"):
    if handle != "AUTO_CLAMPED" or type != "KEYFRAME":
        bpy.ops.action.select_all(action='DESELECT')

    obj.pass_index = value
    obj.keyframe_insert(data_path="pass_index", frame=frame)

    if handle != "AUTO_CLAMPED":
        bpy.ops.action.handle_type(type=handle)
    if type != "KEYFRAME":
        bpy.ops.action.keyframe_type(type=type)


def anim_loc(obj, value, frame, handle="AUTO_CLAMPED", type="KEYFRAME"):
    if handle != "AUTO_CLAMPED" or type != "KEYFRAME":
        bpy.ops.action.select_all(action='DESELECT')

    obj.location = value
    obj.keyframe_insert(data_path="location", frame=frame)

    if handle != "AUTO_CLAMPED":
        bpy.ops.action.handle_type(type=handle)
    if type != "KEYFRAME":
        bpy.ops.action.keyframe_type(type=type)

def anim_loc_x(obj, value, frame, handle="AUTO_CLAMPED", type="KEYFRAME"):
    if handle != "AUTO_CLAMPED" or type != "KEYFRAME":
        bpy.ops.action.select_all(action='DESELECT')

    obj.location[0] = value
    obj.keyframe_insert(data_path="location", frame=frame)

    if handle != "AUTO_CLAMPED":
        bpy.ops.action.handle_type(type=handle)
    if type != "KEYFRAME":
        bpy.ops.action.keyframe_type(type=type)

def anim_loc_y(obj, value, frame, handle="AUTO_CLAMPED", type="KEYFRAME"):
    if handle != "AUTO_CLAMPED" or type != "KEYFRAME":
        bpy.ops.action.select_all(action='DESELECT')

    obj.location[1] = value
    obj.keyframe_insert(data_path="location", frame=frame)

    if handle != "AUTO_CLAMPED":
        bpy.ops.action.handle_type(type=handle)
    if type != "KEYFRAME":
        bpy.ops.action.keyframe_type(type=type)

def anim_loc_z(obj, value, frame, handle="AUTO_CLAMPED", type="KEYFRAME"):
    if handle != "AUTO_CLAMPED" or type != "KEYFRAME":
        bpy.ops.action.select_all(action='DESELECT')

    obj.location[2] = value
    obj.keyframe_insert(data_path="location", frame=frame)

    if handle != "AUTO_CLAMPED":
        bpy.ops.action.handle_type(type=handle)
    if type != "KEYFRAME":
        bpy.ops.action.keyframe_type(type=type)


def anim_rot(obj, value, frame, handle="AUTO_CLAMPED", type="KEYFRAME", value_is_degrees=True):
    if handle != "AUTO_CLAMPED" or type != "KEYFRAME":
        bpy.ops.action.select_all(action='DESELECT')

    if value_is_degrees:
        value = [math.radians(i) for i in value]
    obj.rotation_euler = value
    obj.keyframe_insert(data_path="rotation_euler", frame=frame)

    if handle != "AUTO_CLAMPED":
        bpy.ops.action.handle_type(type=handle)
    if type != "KEYFRAME":
        bpy.ops.action.keyframe_type(type=type)

def anim_rot_x(obj, value, frame, handle="AUTO_CLAMPED", type="KEYFRAME", value_is_degrees=True):
    if handle != "AUTO_CLAMPED" or type != "KEYFRAME":
        bpy.ops.action.select_all(action='DESELECT')

    if value_is_degrees:
        value = math.radians(value)
    obj.rotation_euler[0] = value
    obj.keyframe_insert(data_path="rotation_euler", frame=frame)

    if handle != "AUTO_CLAMPED":
        bpy.ops.action.handle_type(type=handle)
    if type != "KEYFRAME":
        bpy.ops.action.keyframe_type(type=type)

def anim_rot_y(obj, value, frame, handle="AUTO_CLAMPED", type="KEYFRAME", value_is_degrees=True):
    if handle != "AUTO_CLAMPED" or type != "KEYFRAME":
        bpy.ops.action.select_all(action='DESELECT')

    if value_is_degrees:
        value = math.radians(value)
    obj.rotation_euler[1] = value
    obj.keyframe_insert(data_path="rotation_euler", frame=frame)

    if handle != "AUTO_CLAMPED":
        bpy.ops.action.handle_type(type=handle)
    if type != "KEYFRAME":
        bpy.ops.action.keyframe_type(type=type)

def anim_rot_z(obj, value, frame, handle="AUTO_CLAMPED", type="KEYFRAME", value_is_degrees=True):
    if handle != "AUTO_CLAMPED" or type != "KEYFRAME":
        bpy.ops.action.select_all(action='DESELECT')

    if value_is_degrees:
        value = math.radians(value)
    obj.rotation_euler[2] = value
    obj.keyframe_insert(data_path="rotation_euler", frame=frame)

    if handle != "AUTO_CLAMPED":
        bpy.ops.action.handle_type(type=handle)
    if type != "KEYFRAME":
        bpy.ops.action.keyframe_type(type=type)


def anim_scale(obj, value, frame, handle="AUTO_CLAMPED", type="KEYFRAME"):
    if handle != "AUTO_CLAMPED" or type != "KEYFRAME":
        bpy.ops.action.select_all(action='DESELECT')

    obj.scale = value
    obj.keyframe_insert(data_path="scale", frame=frame)

    if handle != "AUTO_CLAMPED":
        bpy.ops.action.handle_type(type=handle)
    if type != "KEYFRAME":
        bpy.ops.action.keyframe_type(type=type)


def anim_attr(obj, attr, value, frame, handle="AUTO_CLAMPED", type="KEYFRAME"):
    if handle != "AUTO_CLAMPED" or type != "KEYFRAME":
        bpy.ops.action.select_all(action='DESELECT')

    setattr(obj, attr, value)
    obj.keyframe_insert(data_path=attr, frame=frame)

    if handle != "AUTO_CLAMPED":
        bpy.ops.action.handle_type(type=handle)
    if type != "KEYFRAME":
        bpy.ops.action.keyframe_type(type=type)
