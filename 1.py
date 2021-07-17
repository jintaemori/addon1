import bpy
from math import *

from bpy.types import(Panel, Operator, PropertyGroup)

from bpy.props import(StringProperty, PointerProperty, IntProperty, FloatProperty)


def evaluate2(l, r, start, stop, step):
    res = []  
    in_mat = []
    k = start
    while k < stop:
        in_mat.append(k)
        k += step  
    if ('x' in r):
        if ('y' in l):
            for i in in_mat:
                x = i
                y = eval(r)
                z = 0
                res.append([x, y, z])
            return res
        if ('z' in l):
            for i in in_mat:
                x = i
                y = 0
                z = eval(r)
                res.append([x, y, z])
            return res
                
    if ('y' in r):
        if ('x' in l):
            for i in in_mat:
                y = i
                x = eval(r)
                z = 0
                res.append([x, y, z])
            return res
        if ('z' in l):
            for i in in_mat:
                y = i
                x = 0
                z = eval(r)
                res.append([x, y, z])
            return res
                
    if ('z' in r):
        if ('x' in l):
            for i in in_mat:
                z = i
                x = eval(r)
                y = 0
                res.append([x, y, z])
            return res
        if ('y' in l):
            for i in in_mat:
                z = i
                x = 0
                y = eval(r)
                res.append([x, y, z])
            return res

def evaluate3(l, r, start1, stop1, step1, start2, stop2, step2):
    res = []
    in_mat1 = []
    in_mat2 = []
    k = start1
    while k < stop1:
        in_mat1.append(k)
        k += step1
    k = start2
    while k < stop2:
        in_mat2.append(k)
        k += step2
        
    if ((('x' in r) and ('y' in r)) and ('z' in l)):
        for i in in_mat1:
            x = i
            for j in in_mat2:
                y = j
                z = eval(r)
                res.append([x, y, z])
        return res
    if ((('x' in r) and ('z' in r)) and ('y' in l)):
        for i in in_mat1:
            x = i
            for j in in_mat2:
                z = j
                y = eval(r)
                res.append([x, y, z])
        return res    
    if ((('y' in r) and ('z' in r)) and ('x' in l)):
        for i in in_mat1:
            y = i
            for j in in_mat2:
                z = j
                x = eval(r)
                res.append([x, y, z])
        return res
    
def evaluatei(xi, yi, zi, start, stop, step):
    res = []
    in_mat = []
    k = start
    while k < stop:
        in_mat.append(k)
        k += step
    for i in in_mat:
        x = eval(xi)
        y = eval(yi)
        z = eval(zi)
        res.append([x, y, z])
    return res
      

class AP(PropertyGroup):
    
    '''2DEQ'''
    eq : StringProperty(name = "Equation", description = "Equation", default = "")    
    start : IntProperty(name = "Start", description = "Start", default = 1)        
    end : IntProperty(name = "End", description = "End", default = 10)        
    step : FloatProperty(name = "Step", description = "Step", default = 1)  
    st : StringProperty(name = "Selection", description = "Selection", default = "")    
    
    '''3DEQ'''
    eq1 : StringProperty(name = "Equation", description = "Equation", default = "")    
    start1 : IntProperty(name = "Start1", description = "Start1", default = 1)        
    end1 : IntProperty(name = "End1", description = "End1", default = 10)        
    step1 : FloatProperty(name = "Step1", description = "Step1", default = 1)  
    start2 : IntProperty(name = "Start2", description = "Start2", default = 1)        
    end2 : IntProperty(name = "End2", description = "End2", default = 10)        
    step2 : FloatProperty(name = "Step2", description = "Step2", default = 1) 
    st1 : StringProperty(name = "Selection", description = "Selection1", default = "")
    
    '''3DEQi'''
    eqx : StringProperty(name = "Equation x", description = "Equation", default = "")  
    eqy : StringProperty(name = "Equation y", description = "Equation", default = "")
    eqz : StringProperty(name = "Equation z", description = "Equation", default = "")  
    starti : IntProperty(name = "Starti", description = "Start", default = 1)        
    endi : IntProperty(name = "Endi", description = "End", default = 10)        
    stepi : FloatProperty(name = "Stepi", description = "Step", default = 1)  
    sti : StringProperty(name = "Selectioni", description = "Selection", default = "")


class ObjectAdder1(Operator):
    bl_idname = "add.ob"
    bl_label = "Add objects"
    bl_description = "Adds objects on the equation"
    
    def execute(self, context):
        scene = context.scene.your_properties
        st = scene.st        
        eq = scene.eq
        start = scene.start
        end = scene.end
        step = scene.step

        eq1 = eq.split('=')
        res = evaluate2(eq1[0], eq1[1], start, end, step)
        bpy.ops.object.select_all(action='DESELECT')
        bpy.data.objects[st].select_set(True)
        for i in res:    
            bpy.ops.object.duplicate_move(OBJECT_OT_duplicate={"linked":False, "mode":'TRANSLATION'}, TRANSFORM_OT_translate={"value":(0, 0, 0)})
            bpy.context.active_object.location.x = i[0]
            bpy.context.active_object.location.y = i[1]
            bpy.context.active_object.location.z = i[2]
        bpy.ops.object.select_all(action='DESELECT')
        bpy.ops.object.select_all(action='TOGGLE')
        bpy.ops.object.select_all(action='TOGGLE')
        return {'FINISHED'}
    
class ObjectAdder2(Operator):
    bl_idname = "add.ob1"
    bl_label = "Add objects"
    bl_description = "Adds objects on the equation"

    def execute(self, context):
        scene = context.scene.your_properties
        st1 = scene.st1        
        eq1 = scene.eq1
        start1 = scene.start1
        end1 = scene.end1
        step1 = scene.step1
        start2 = scene.start2
        end2 = scene.end2
        step2 = scene.step2

        eq2 = eq1.split('=')
        res = evaluate3(eq2[0], eq2[1], start1, end1, step1, start2, end2, step2)
        bpy.ops.object.select_all(action='DESELECT')
        bpy.data.objects[st1].select_set(True)
        for i in res:    
            bpy.ops.object.duplicate_move(OBJECT_OT_duplicate={"linked":False, "mode":'TRANSLATION'}, TRANSFORM_OT_translate={"value":(0, 0, 0)})
            bpy.context.active_object.location.x = i[0]
            bpy.context.active_object.location.y = i[1]
            bpy.context.active_object.location.z = i[2]
        bpy.ops.object.select_all(action='DESELECT')
        bpy.ops.object.select_all(action='TOGGLE')
        bpy.ops.object.select_all(action='TOGGLE')
        return {'FINISHED'}
    
class ObjectAdder3(Operator):
    bl_idname = "add.ob2"
    bl_label = "Add objects"
    bl_description = "Adds objects on the equation"

    def execute(self, context):
        scene = context.scene.your_properties
        sti = scene.sti        
        eqx = scene.eqx
        eqy = scene.eqy
        eqz = scene.eqz
        starti = scene.starti
        endi = scene.endi
        stepi = scene.stepi

        res = evaluatei(eqx, eqy, eqz, starti, endi, stepi)
        bpy.ops.object.select_all(action='DESELECT')
        bpy.data.objects[sti].select_set(True)
        for i in res:    
            bpy.ops.object.duplicate_move(OBJECT_OT_duplicate={"linked":False, "mode":'TRANSLATION'}, TRANSFORM_OT_translate={"value":(0, 0, 0)})
            bpy.context.active_object.location.x = i[0]
            bpy.context.active_object.location.y = i[1]
            bpy.context.active_object.location.z = i[2]
        bpy.ops.object.select_all(action='DESELECT')
        bpy.ops.object.select_all(action='TOGGLE')
        bpy.ops.object.select_all(action='TOGGLE')
        return {'FINISHED'}
        

class AddonPanel1(Panel):
    bl_label = "2 Variable"
    bl_idname = "OBJECT_PT_eq2"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Equation solver"
    
    def draw(self, context):
        layout = self.layout
        scene = context.scene.your_properties   
        
        col = layout.column()
        
        col.label(text = "2 Variable")
        col.prop_search(scene, "st", context.scene, "objects")
        col = layout.column()
        col.prop(scene, "eq")
        col = layout.column()
        col.prop(scene, "start")
        col.prop(scene, "end")
        col.prop(scene, "step")
        col = layout.column()
        col.operator("add.ob")  
        
        
        
class AddonPanel2(Panel):
    bl_label = "3 Variable"
    bl_idname = "OBJECT_PT_eq3"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Equation solver"
    
    def draw(self, context):
        layout = self.layout
        scene = context.scene.your_properties   
        
        col = layout.column()
        
        col.label(text = "3 Variable")  
        col = layout.column()
        col.prop_search(scene, "st1", context.scene, "objects")
        col = layout.column()
        col.prop(scene, "eq1")
        col = layout.column()
        col.label(text = "Variable 1")
        col.prop(scene, "start1")
        col.prop(scene, "end1")
        col.prop(scene, "step1")
        col.label(text = "Variable 2")
        col.prop(scene, "start2")
        col.prop(scene, "end2")
        col.prop(scene, "step2")
        col = layout.column()
        col.operator("add.ob1")
        
class AddonPanel3(Panel):
    bl_label = "3 Variable over i"
    bl_idname = "OBJECT_PT_eqi"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Equation solver"
    
    def draw(self, context):
        layout = self.layout
        scene = context.scene.your_properties   
        
        col = layout.column()
        
        col.label(text = "3 Variable over i")  
        col = layout.column()
        col.prop_search(scene, "sti", context.scene, "objects")
        col = layout.column()
        col.prop(scene, "eqx")
        col.prop(scene, "eqy")
        col.prop(scene, "eqz")
        col = layout.column()
        col.label(text = "i")
        col.prop(scene, "starti")
        col.prop(scene, "endi")
        col.prop(scene, "stepi")
        col = layout.column()
        col.operator("add.ob2")
        

        
        
    
classes = (AP, AddonPanel1, AddonPanel2, AddonPanel3, ObjectAdder1, ObjectAdder2, ObjectAdder3)


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