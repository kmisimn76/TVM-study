from core.util.Const import *
from core.util.Layout import Layout
from core.util.Shape import Shape

class ExprNode:
    def __init__(self, clone):
        global TIR_NODE_ID
        if clone == None:
            self.nodeid = TIR_NODE_ID
            TIR_NODE_ID = TIR_NODE_ID + 1
#            print(TIR_NODE_ID)
        else:
#            print("COPY")
            self.nodeid = clone
    def clone(self): #have to override
        raise "Empty action : Copy()"
    def accept(self, Fucntor):
        return Functor.visit_expr(self)
    def accept(self, Functor, extra):
        return Functor.visit_expr(self, extra)

class FunctorExprNode:
    def visit_expr(self, node):
        pass
    def visit_expr(self, node, extra):
        pass

### Define TIR Expression Nodes

# Variable Node
class VarExprNode(ExprNode):
    '''
    TIR Variable Expression Node
    name
    '''
    def __init__(self, name, clone=None):
        super().__init__(clone)
        self.name = name
#        self.node_list = []
        self.nodes = { }
    def clone(self):
        node_clone = VarExprNode(self.name, self.nodeid)
        return node_clone

# Pointer Node
class ArrayExprNode(ExprNode):
    '''
    TIR Array Expression Node
    name, index
    '''
    def __init__(self, name, index, clone=None):
        super().__init__(clone)
        self.name = name
#        self.index = index
#        self.node_list = [index]
        self.nodes = {  'index': index }
    def clone(self):
        node_clone = ArrayExprNode(self.name, self.nodes['index'].clone(), self.nodeid)
        return node_clone

# Constant node
class ConstExprNode(ExprNode):
    '''
    TIR Constant Expression Node
    value
    '''
    def __init__(self, value, clone=None):
        super().__init__(clone)
        if isinstance(value, str) is not True:
            value = str(value)
        self.value = value
#        self.node_list = []
        self.nodes = { }
    def clone(self):
        node_clone = ConstExprNode(self.value, self.nodeid)
        return node_clone

class LoadExprNode(ExprNode):
    def __init__(self, clone=None):
        super().__init__(clone)

class StoreExprNode(ExprNode):
    def __init__(self, clone=None):
        super().__init__(clone)

class AddExprNode(ExprNode):
    '''
    TIR Addition Expression Node
    exression A, B : A+B
    '''
    def __init__(self, A, B, clone=None):
        super().__init__(clone)
#        self.A = A
#        self.B = B
#        self.node_list = [self.A, self.B]
        self.nodes = {  'A': A,
                        'B': B }
    def clone(self):
        node_clone = AddExprNode(self.nodes['A'].clone(), self.nodes['B'].clone(), self.nodeid)
        return node_clone

class SubExprNode(ExprNode):
    def __init__(self, clone=None):
        super().__init__(clone)

class MultExprNode(ExprNode):
    def __init__(self, clone=None):
        super().__init__(clone)

class DivExprNode(ExprNode):
    def __init__(self, clone=None):
        super().__init__(clone)

class MaxExprNode(ExprNode):
    def __init__(self, clone=None):
        super().__init__(clone)

# Bitwise operator
class BitExprNode(ExprNode):
    def __init__(self, clone=None):
        super().__init__(clone)

# == != > <
EXPR_COMPARE_TYPE_EQ = 0
EXPR_COMPARE_TYPE_NE = 1
EXPR_COMPARE_TYPE_GT = 2
EXPR_COMPARE_TYPE_LT = 3
class CompExprNode(ExprNode):
    '''
    TIR Addition Expression Node
    exression A, B : A ? B, comp_type : 0(==), 1(!=), 2(>), 3(<)
    '''
    def __init__(self, A, B, comp_type, clone=None):
        super().__init__(clone)
#        self.A = A
#        self.B = B
        self.comp_type = comp_type
#        self.node_list = [self.A, self.B]
        self.nodes = {  'A': A,
                        'B': B }
    def clone(self):
        node_clone = CompExprNode(self.nodes['A'].clone(), self.nodes['B'].clone(), self.comp_type, self.nodeid)
        return node_clone

