import bpy
from math import *

from bpy.types import(Panel, Operator, PropertyGroup)

from bpy.props import(StringProperty, PointerProperty, IntProperty)


def evaluate2(l, r, start, stop, step):
    res = []    
    if ('x' in r):
        if ('y' in l):
            for i in range(start, stop, step):
                x = i
                y = eval(r)
                z = 0
                res.append([x, y, z])
            return res
        if ('z' in l):
            for i in range(start, stop, step):
                x = i
                y = 0
                z = eval(r)
                res.append([x, y, z])
            return res
                
    if ('y' in r):
        if ('x' in l):
            for i in range(start, stop, step):
                y = i
                x = eval(r)
                z = 0
                res.append([x, y, z])
            return res
        if ('z' in l):
            for i in range(start, stop, step):
                y = i
                x = 0
                z = eval(r)
                res.append([x, y, z])
            return res
                
    if ('z' in r):
        if ('x' in l):
            for i in range(start, stop, step):
                z = i
                x = eval(r)
                y = 0
                res.append([x, y, z])
            return res
        if ('y' in l):
            for i in range(start, stop, step):
                z = i
                x = 0
                y = eval(r)
                res.append([x, y, z])
            return res
        

class AP(PropertyGroup):
    
    eq : StringProperty(name = "Equation", description = "Equation", default = "")    
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
        eq1 = eq.split('=')
        res = evaluate2(eq1[0], eq1[1], start, end, step)
        for i in res:
            k = bpy.ops.object
            k.duplicate_move(OBJECT_OT_duplicate={"linked":False, "mode":'TRANSLATION'}, TRANSFORM_OT_translate={"value":(0, 0, 0)})
            bpy.context.active_object.location.x = i[0]
            bpy.context.active_object.location.y = i[1]
            bpy.context.active_object.location.z = i[2]
        return {'FINISHED'}
        

class AddonPanel1(Panel):
    bl_label = "Two Variable Equation"
    bl_idname = "OBJECT_PT_eq"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Two Variable Equation"
    
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