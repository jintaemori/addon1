import bpy

class Panel1 (bpy.types.Panel):
    bl_label = "Panel1"
    bl_idname = "Panel1"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'EqAdd'
    
    def draw(self, context):
        layout = self.layout
        
        row = layout.row()
        row.label(text = "Sample text", icon = 'CUBE')
        row = layout.row()
        row.operator("mesh.primitive_cube_add")
        
def register():
    bpy.utils.register_class(Panel1)
    
def unregister():
    bpy.utils.unregister_class(Panel1)
    
if __name__ == "__main__":
    register()