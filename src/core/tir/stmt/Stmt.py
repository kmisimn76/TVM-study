
## Supeclass of TIR Statement Nodes
# define 'data' of expression
class StmtNode:
	def accept(self, Functor):
		Functor.visit(self)
	def accept(self, Functor, extra):
		return Functor.visit(self, extra)


### Define TIR Statement Nodes
		
# If Node
class IfStmtNode(StmtNode):
	def __init__(self, cond, expr_true, expr_false):
		self.cond = cond
		self.expr_true = expr_true
		self.expr_false = expr_false

# Evaluation Node for PrimExpr Evaluation
class EvalStmtNode(StmtNode):
	def __init__(self, target_expr):
		self.target_expr = target_expr

# Variable Node
class VarStmtNode(StmtNode):
	def __init__(self, name, real):
		self.name = name
		self.value = real

# Variable Allocation Node
class AllocateStmtNode(StmtNode):
	pass

# Store Node
class StoreStmtNode(StmtNode):
	pass

# IfThenElse Node
class IfThenElseStmtNode(StmtNode):
	pass

# For Node
class ForStmtNode(StmtNode):
	pass

## Supaeclass of Relay Expr Functor
# define 'action' about expression
class FunctorStmtNode:
	def visit(self, node):
		pass
	def visit(self, node, extra):
		pass
