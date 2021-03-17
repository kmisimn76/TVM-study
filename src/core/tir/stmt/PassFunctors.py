from Stmt import *

# LoopUnrolling Pass of TIR Statement
class LoopUnrollingFunctor(StmtNode):
	def visit(self, node, extra):
		indent = extra
		if isinstance(node, IfThenElseStmtNode):
			return self.visit_If(node, extra)
		elif isinstance(node, ForStmtNode):
			return self.visit_For(node, extra)
	
	def visit_If(self, node, extra):
		pass
	def visit_For(self, node, extra):
		pass
	

