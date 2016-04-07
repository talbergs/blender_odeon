import bpy,bmesh
class BlendOneLisp():
	def __init__(self, opts = {}):
		self.opts = {
			"cad3dpoly":False, # use 3d poly command
			"cad3face":True, # use 3d face command
			"_flipZ":False, # flip Zed axis upon export >> not often needed
			"units":1000, #enlarge values if autocad is set in milimeters
			"function_call":'zidafabrika03',
			"filepath":'zidafabrika03.lsp', #must be lsp for aCad
			"resolution":3,
		}
		self.mesh = bmesh.from_edit_mesh(bpy.context.object.data)

		self.opts.update(opts)
		self.run()

	def run(self):
		line = '(defun c:'+self.opts["function_call"]+'()'
		comd = ''

		for p in self.mesh.faces:
			if len(p.verts) == 4 and self.opts["cad3face"]: #3dface can have 4points MAX ( 3point have different spacings )
				comd += '3DFACE '
				line+='(command "._3dface" '
				for v in p.verts:
					exp = ','.join(map(str,map(self.multby,self.prep(v.co))))
					line+='"'+exp+'" '
					comd+=exp+' '
				line += '"")'
				comd += '    '
			elif self.opts["cad3dpoly"]: #fallback to 3d polyline
				comd += '3DPOLY '
				line+='(command "._3dpoly" '
				for v in p.verts:
					exp = ','.join(map(str,map(self.multby,self.prep(v.co))))
					line+='"'+exp+'" '
					comd+=exp+' '
				# close polyline on first vert
				exp = ','.join(map(str,map(self.multby,self.prep(p.verts[0].co))))
				line+='"'+exp+'" '
				comd+=exp+' '
				line += '"")'
				comd += ' '
			else:
				printDanger("unrendered some data")
		line += ')'
		fo = open(self.opts["filepath"], 'w+')
		fo.write( line )
		print(comd)
		fo.close()

	def prep(self, elem): #apply transforms
			if self.opts["_flipZ"]:
				elem[2] = 0 - elem[2]
			return elem

	def multby(self, elem): 
			return round(elem * self.opts["units"],self.opts["resolution"])
	def printDanger(s):
		print("---------")
		print(s)
		print("---------")

BlendOneLisp({
	"cad3dpoly":True,
    "function_call":"KLASE",
    "filepath":"KLASE.lsp",
    "units":1,
    "resolution":3,
})