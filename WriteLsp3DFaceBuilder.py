#3 vert facer will u do by hand comd
#At autocad, Tools->Load application, load
#this generated file -> execute shortcut
#you choose, at (defun c:_<shortcut>_()
#--riba--
print('<-_ this run _^')
import bpy,bmesh
mesh=bmesh.from_edit_mesh(bpy.context.object.data)

units = 1000 #enlarge values if autocad is set in milimeters
function_call = 'PREZENTACIJU_TELPA'
filepath = 'PREZENTACIJU_TELPA.lsp' #must be lsp for aCad

def multby(elem):
    #return elem * units #or
	return round(elem * units)

line = '(defun c:'+function_call+'()'
comd = ''

for p in mesh.faces:
	if len(p.verts) == 4:
		comd += '3DFACE '
		line+='(command "._3dface" '
		for v in p.verts:
			exp = ','.join(map(str,map(multby,v.co)))
			line+='"'+exp+'" '
			comd+=exp+' '
		line += '"")'
		if len(p.verts) == 4:
			comd += '    '
		else:
			comd += '       '
line += ')'
fo = open(filepath, 'w+')
fo.write( line )
print(comd)
fo.close()
