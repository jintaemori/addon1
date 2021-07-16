import bpy
from math import *

from bpy.types import(Panel, Operator, PropertyGroup)

from bpy.props import(StringProperty, PointerProperty, IntProperty)


class AP(PropertyGroup):
    
    eq : StringProperty(name = "Name", description = "Equation", default = "")
    
    start : IntProperty(name = "Start", description = "Start", default = 1)
        
    end : IntProperty(name = "End", description = "End", default = 10)
        
    step : IntProperty(name = "Step", description = "Step", default = 1)        



class ObjectAdder(Operator):
    """Tooltip"""
    bl_idname = "add.ob"
    bl_label = "Add objects"
    bl_description = "Adds objects on the equation"
    
    def execute(self, context):
        scene = context.scene.your_properties
        eq = scene.eq
        start = scene.start
        end = scene.end
        step = scene.step
        for i in range(start, end, step):
            print(i)
            k = bpy.ops.object
            k.duplicate_move(OBJECT_OT_duplicate={"linked":False, "mode":'TRANSLATION'}, TRANSFORM_OT_translate={"value":(i, 0, 0)})
        
        return {'FINISHED'}
        

class AddonPanel1(Panel):
    bl_label = "Addon Panel 1"
    bl_idname = "OBJECT_PT_eq"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Addon Panel 1"
    
    def draw(self, context):
        layout = self.layout
        scene = context.scene.your_properties
        
        col = layout.column()
        col.prop(scene, "eq")
        col = layout.column()
        col.prop(scene, "start")
        col.prop(scene, "end")
        col.prop(scene, "step")
        col = layout.column()
        col.operator("add.ob")    
        
        
    
classes = (AP, AddonPanel1, ObjectAdder)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.Scene.your_properties = PointerProperty(type = AP)

  
def unregister():  
    for cls in classes:
        bpy.utils.unregister_class(cls)
    del bpy.types.Scene.your_properties
    
    
if __name__ == "__main__":
    register()