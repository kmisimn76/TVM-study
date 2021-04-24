from core.Relay.RelayExpr import *

def print_indent(message, indent):
	for i in range(indent):
		print("   ", end='')
	print(message)


class PrintFunctor(FunctorRelayExprNode):
	def visit(self, node, extra):
		indent = extra
		if isinstance(node, IfRelayExprNode):
			print_indent("IfNode", indent)
			print_indent("-COND", indent)
			node.cond.accept(self, indent+1)
			print_indent("-True Then,", indent)
			node.expr_true.accept(self, indent+1)
			print_indent("-False Then,", indent)
			node.expr_false.accept(self, indent+1)
		elif isinstance(node, VarRelayExprNode):
			print_indent("VarNode", indent)
			print_indent("-Name: "+node.name, indent)
			print_indent("-Value: "+str(node.value), indent)
		elif isinstance(node, AddOperRelayExprNode):
			print_indent("AddNode", indent)
			print_indent("-First Term", indent)
			node.A.accept(self, indent+1)
			print_indent("-Second Term", indent)
			node.B.accept(self, indent+1)
		elif isinstance(node, EqualOperRelayExprNode):
			print_indent("EqualNode", indent)
			print_indent("-First Term", indent)
			node.A.accept(self, indent+1)
			print_indent("-Second Term", indent)
			node.B.accept(self, indent+1)
		return None
	
class EvalFunctor(FunctorRelayExprNode):
	def visit(self, node, extra):
		if isinstance(node, IfRelayExprNode):
			valCond = node.cond.accept(self, extra)
			valTrue = node.expr_true.accept(self, extra)
			valFalse = node.expr_false.accept(self, extra)
			if valCond:
				return valTrue
			else:
				return valFalse
		elif isinstance(node, VarRelayExprNode):
			return node.value
		elif isinstance(node, AddOperRelayExprNode):
			valA = node.A.accept(self, extra)
			valB = node.B.accept(self, extra)
			return valA + valB
		elif isinstance(node, EqualOperRelayExprNode):
			valA = node.A.accept(self, extra)
			valB = node.B.accept(self, extra)
			if valA==valB:
				return True
			else:
				return False
	
	
