
from core.util.Const import *

## Supeclass of TIR Statement Nodes
# define 'data' of expression
class StmtNode:
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
    def accept(self, Functor):
        return Functor.visit_stmt(self)
    def accept(self, Functor, extra):
        return Functor.visit_stmt(self, extra)

## Supaeclass of Relay Expr Functor
# define 'action' about expression
class FunctorStmtNode:
    def visit_stmt(self, node):
        pass
    def visit_stmt(self, node, extra):
        pass

### Define TIR Statement Nodes
        
# If Node
class IfStmtNode(StmtNode):
    '''
    TIR If Statement Node
    cond, expr_true, expr_false
    '''
    def __init__(self, cond, expr_true, expr_false, clone=None):
        super().__init__(clone)
#        self.cond = cond
#        self.expr_true = expr_true
#        self.expr_false = expr_false
#        self.node_list = [self.cond,self.expr_true,self.expr_false]
        self.nodes = {  'cond': cond,
                        'expr_true': expr_true,
                        'expr_false': expr_false}
    def clone(self):
        node_clone = IfStmtNode(self.nodes['cond'].clone(), self.nodes['expr_true'].clone(), self.nodes['expr_false'].clone(), self.nodeid)
        return node_clone

# Evaluation Node for PrimExpr Evaluation
class EvalStmtNode(StmtNode):
    def __init__(self, target_expr, clone=None):
        super().__init__(clone)
#        self.target_expr = target_expr
#        self.node_list = [self.target_expr]
        self.nodes = {  'target_expr': target_expr}
    def clone(self):
        node_clone = EvalStmtNode(self.nodes['target_expr'].clone(), self.nodeid)
        return node_clone

# Variable Allocation Node
class AllocStmtNode(StmtNode):
    '''
    TIR Allocate Statement Node
    tar, src
    '''
    def __init__(self, tar, src, clone=None):
        super().__init__(clone)
#        self.tar = tar
#        self.src = src
#        self.node_list = [self.tar, self.src]
        self.nodes = {  'tar' : tar,
                        'src' : src}
    def clone(self):
        node_clone = AllocStmtNode(self.nodes['tar'].clone(), self.nodes['src'].clone(), self.nodeid)
        return node_clone

# Store Node
class StoreStmtNode(StmtNode):
    def __init__(self, clone=None):
        super().__init__(clone)

# For Node
class ForStmtNode(StmtNode):
    '''
    TIR For Statement Node
    init, cond, increment, loop_code
    '''
    def __init__(self, init, cond, increment, loop_code, clone=None):
        super().__init__(clone)
#        self.init = init
#        self.cond = cond
#        self.increment = increment
#        self.loop_code = loop_code
#        self.node_list = [self.init,self.cond,self.increment,self.loop_code]
        self.nodes = {  'init' : init,
                        'cond' : cond,
                        'increment' : increment,
                        'loop_code' : loop_code}
    def clone(self):
        node_clone = ForStmtNode(self.nodes['init'].clone(), self.nodes['cond'].clone(), self.nodes['increment'].clone(), self.nodes['loop_code'].clone(), self.nodeid)
        return node_clone

# List of statements Node
class StatementsStmtNode(StmtNode):
    '''
    TIR Statements Node
    list of statements
    '''
    def __init__(self, statements, clone=None):
        super().__init__(clone)
        if isinstance(statements, list) is not True:
            raise TypeError
        for node in statements:
            if isinstance(node, StmtNode) is not True:
                raise TypeError
#        self.stmts = statements
#        self.node_list = self.stmts
        self.nodes = { }
        for idx, nd in zip(range(len(statements)), statements):
            self.nodes[str(idx)] = nd
    def clone(self):
        node_clone = StatementsStmtNode([nd.clone() for nd in self.nodes.values()], self.nodeid)
        return node_clone


