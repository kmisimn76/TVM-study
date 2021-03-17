from Stmt import *

def print_indent(message, indent):
	for i in range(indent):
		print("   ", end='')
	print(message)

# Print Information of Relay Expression AST
#		extra : indent
#		return : None
class PrintFunctor(FunctorRelayExprNode):
	def visit(self, node, extra):
		indent = extra
		if isinstance(node, IfRelayExprNode):
			self.visit_If(node, indent)
		elif isinstance(node, VarRelayExprNode):
			self.visit_Var(node, indent)
		elif isinstance(node, AddOperRelayExprNode):
			self.visit_AddOper(node, indent)
		elif isinstance(node, EqualOperRelayExprNode):
			self.visit_EqualOper(node, indent)
		return None

	def visit_If(self, node, indent):
			print_indent("IfNode", indent)
			print_indent("-COND", indent)
			node.cond.accept(self, indent+1)
			print_indent("-True Then,", indent)
			node.expr_true.accept(self, indent+1)
			print_indent("-False Then,", indent)
			node.expr_false.accept(self, indent+1)
	def visit_Var(self, node, indent):
			print_indent("VarNode", indent)
			print_indent("-Name: "+node.name, indent)
			print_indent("-Value: "+str(node.value), indent)
	def visit_AddOper(self, node, indent):
			print_indent("AddNode", indent)
			print_indent("-First Term", indent)
			node.A.accept(self, indent+1)
			print_indent("-Second Term", indent)
			node.B.accept(self, indent+1)
	def visit_EqualOper(self, node, indent):
			print_indent("EqualNode", indent)
			print_indent("-First Term", indent)
			node.A.accept(self, indent+1)
			print_indent("-Second Term", indent)
			node.B.accept(self, indent+1)
	
# Evaluate Relay Expression AST
#		Extra : None
#		Return : Evaluation Value
class EvalFunctor(FunctorRelayExprNode):
	def visit(self, node, extra):
		if isinstance(node, IfRelayExprNode):
			return self.visit_If(node, extra)
		elif isinstance(node, VarRelayExprNode):
			return self.visit_Var(node, extra)
		elif isinstance(node, AddOperRelayExprNode):
			return self.visit_AddOper(node, extra)
		elif isinstance(node, EqualOperRelayExprNode):
			return self.visit_EqualOper(node, extra)
	
	def visit_If(self, node, extra):
			valCond = node.cond.accept(self, extra)
			valTrue = node.expr_true.accept(self, extra)
			valFalse = node.expr_false.accept(self, extra)
			if valCond:
				return valTrue
			else:
				return valFalse
	def visit_Var(self, node, extra):
			return node.value
	def visit_AddOper(self, node, extra):
			valA = node.A.accept(self, extra)
			valB = node.B.accept(self, extra)
			return valA + valB
	def visit_EqualOper(self, node, extra):
			valA = node.A.accept(self, extra)
			valB = node.B.accept(self, extra)
			if valA==valB:
				return True
			else:
				return False
	
