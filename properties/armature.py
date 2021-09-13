"""Nif Format Properties, stores custom nif properties for armature settings"""

# ***** BEGIN LICENSE BLOCK *****
# 
# Copyright © 2014, NIF File Format Library and Tools contributors.
# All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
# 
#    * Redistributions of source code must retain the above copyright
#      notice, this list of conditions and the following disclaimer.
# 
#    * Redistributions in binary form must reproduce the above
#      copyright notice, this list of conditions and the following
#      disclaimer in the documentation and/or other materials provided
#      with the distribution.
# 
#    * Neither the name of the NIF File Format Library and Tools
#      project nor the names of its contributors may be used to endorse
#      or promote products derived from this software without specific
#      prior written permission.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
# ***** END LICENSE BLOCK *****

import bpy
from bpy.props import (PointerProperty,
                       IntProperty,
                       EnumProperty,
                       StringProperty,
                       BoolProperty
                       )
from bpy.types import PropertyGroup

from io_scene_niftools.utils.decorators import register_classes, unregister_classes

# allow multiple selection updates
def update_fields(field_name):
    def update_fields_inner(self, context):
        if not context or not context.selected_pose_bones:
            return
        for pose_bone in context.selected_pose_bones:
            nif_bone_props = pose_bone.bone.niftools
            nif_bone_props[field_name] = context.bone.niftools[field_name] # prevent infinite recursion of calling update_priorities
    return update_fields_inner


class BoneProperty(PropertyGroup):
    flags: IntProperty(
        name='Bone Flag',
        default=0,
        update=update_fields('flags')
    )
    priority: IntProperty(
        name='Bone Priority',
        default=0,
        update=update_fields('priority')
    )
    longname: StringProperty(
        name='Nif Long Name',
        update=update_fields('longname')
    )
    exclude_from_export: BoolProperty(
        name='Exclude From Animation Export',
        default=False,
        update=update_fields('exclude_from_export')
    )


class ArmatureProperty(PropertyGroup):

    axis_forward: EnumProperty(
            name="Forward",
            items=(('X', "X Forward", ""),
                   ('Y', "Y Forward", ""),
                   ('Z', "Z Forward", ""),
                   ('-X', "-X Forward", ""),
                   ('-Y', "-Y Forward", ""),
                   ('-Z', "-Z Forward", ""),
                   ),
            default="X",
            )

    axis_up: EnumProperty(
            name="Up",
            items=(('X', "X Up", ""),
                   ('Y', "Y Up", ""),
                   ('Z', "Z Up", ""),
                   ('-X', "-X Up", ""),
                   ('-Y', "-Y Up", ""),
                   ('-Z', "-Z Up", ""),
                   ),
            default="Y",
            )


CLASSES = [
    BoneProperty,
    ArmatureProperty
]


def register():
    register_classes(CLASSES, __name__)

    bpy.types.Armature.niftools = bpy.props.PointerProperty(type=ArmatureProperty)
    bpy.types.Bone.niftools = bpy.props.PointerProperty(type=BoneProperty)


def unregister():
    del bpy.types.Armature.niftools
    del bpy.types.Bone.niftools

    unregister_classes(CLASSES, __name__)
