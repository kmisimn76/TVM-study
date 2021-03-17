from TestFunctors import *
from Stmt import *

printFunc = PrintFunctor()
evalFunc = EvalFunctor()

#Test 1
print("===Test 1===")
A = VarRelayExprNode("A", 1)
B = VarRelayExprNode("B", 2)
AplusB = AddOperRelayExprNode(A, B)
AeqB = EqualOperRelayExprNode(A, B)
IfNode = IfRelayExprNode(AeqB, AplusB, B)

printFunc.visit(IfNode, 0)
res = evalFunc.visit(IfNode, None)
print("Output of AST: ", res)

#Test 2
print("===Test 2===")
A = VarRelayExprNode("A", 2)
B = VarRelayExprNode("B", 2)
AplusB = AddOperRelayExprNode(A, B)
AeqB = EqualOperRelayExprNode(A, B)
IfNode = IfRelayExprNode(AeqB, AplusB, B)

printFunc.visit(IfNode, 0)
res = evalFunc.visit(IfNode, None)
print("Output of AST: ", res)


