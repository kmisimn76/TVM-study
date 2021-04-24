from core.util.Layout import Layout
from core.util.Shape import Shape

class RelayExprNode:
    input_shape = Shape([0,0,0,0])
    optimal_input_layout = Layout.NCHW

    def accept(self, Functor):
        Functor.visit(self)
    def accept(self, Functor, extra):
        return Functor.visit(self, extra)

class FunctorRelayExprNode:
    def visit(self, node):
        pass
    def visit(self, node, extra):
        pass

#### Define Relay Statment Nodes

class IfRelayExprNode(RelayExprNode):
    '''
    Relay If Expression Node
    cond, expr_true, expr_false
    '''
    def __init__(self, cond, expr_true, expr_false):
        self.cond = cond
        self.expr_true = expr_true
        self.expr_false = expr_false

class LetRelayExprNode(RelayExprNode):
    pass

# For Operation Fusing
class FunctionRelayExprNode(RelayExprNode):
    pass

class VarRelayExprNode(RelayExprNode):
    '''
    Relay Variable Expression Node
    name, value?
    '''
    def __init__(self, name, real):
        self.name = name
        self.value = real

class OperRelayExprNode(RelayExprNode):
    pass

class AddOperRelayExprNode(OperRelayExprNode):
    '''
    Relay Add Expression Node
    A, B
    '''
    def __init__(self, A, B):
        self.A = A
        self.B = B

class EqualOperRelayExprNode(OperRelayExprNode):
    '''
    Relay Equal(==) Expression Node
    A, B
    '''
    def __init__(self, A, B):
        self.A = A
        self.B = B

class LayerRelayExprNode(RelayExprNode):
    pass

