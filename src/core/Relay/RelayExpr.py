
class RelayExprNode:
	def accept(self, Functor):
		Functor.visit(self)
	def accept(self, Functor, extra):
		return Functor.visit(self, extra)

class IfRelayExprNode(RelayExprNode):
	def __init__(self, cond, expr_true, expr_false):
		self.cond = cond
		self.expr_true = expr_true
		self.expr_false = expr_false

class LetRelayExprNode(RelayExprNode):
	pass

class FunctionelayExprNode(RelayExprNode):
	pass

class VarRelayExprNode(RelayExprNode):
	def __init__(self, name, real):
		self.name = name
		self.value = real

class OperRelayExprNode(RelayExprNode):
	pass

class AddOperRelayExprNode(OperRelayExprNode):
	def __init__(self, A, B):
		self.A = A
		self.B = B

class EqualOperRelayExprNode(OperRelayExprNode):
	def __init__(self, A, B):
		self.A = A
		self.B = B

class FunctorRelayExprNode:
	def visit(self, node):
		pass
	def visit(self, node, extra):
		pass
