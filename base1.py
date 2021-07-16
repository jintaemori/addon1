bl_info = {
    "name" : "EqAdd",
    "author" : "Sai Sasank",
    "version" : (1, 0),
    "blender" : (2, 93, 0),
    "location" : "View3d > Tool",
    "warning" : "",
    "wiki_url" : "url", 
    "category" : "Add Mesh"
}





import bpy

def main(context):
    for ob in context.scene.objects:
        print(ob)

class Newoperator(bpy.types.Operator):
    bl_idname = "objects.yourname"
    bl_label = "My operator"
    bl_options = {'REGISTER', 'UNDO'}
    
    eq = bpy.props.StringProperty("Enter an equation")
    
    @classmethod
    def poll(cls, context):
        return context.active_object is not None
    
    def invoke(self, context, event):
        return context.window_manager.invoke_props_popup(self, event)
    
    def execute(self, context):
        main(context)
        return {"FINISHED"}


def register():
    bpy.utils.register_class(Newoperator)
        
def unregister():
    bpy.utils.unregister_class(Newoperator)
    
if __name__ == "__main__":
    register()
    bpy.ops.objects.yourname('INVOKE_DEFAULT')