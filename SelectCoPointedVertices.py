import bpy,bmesh
print('Co-points')
rez = 21 #decimal places|treshold| .21 to .0
mesh=bmesh.from_edit_mesh(bpy.context.object.data)

all = []
allobj = []
seen = set()
ex = True

for v in mesh.verts:
    all.append(str(v.co.to_tuple(rez)))
    allobj.append(v)

for i,x in enumerate(all):
    if x not in seen:seen.add(x)
    else:allobj[i].select = True;ex = False;
[bpy.ops.object.editmode_toggle() for _ in range(2)]#toggle twice to refresh view

if not ex:
	print('all finish, no encounters')