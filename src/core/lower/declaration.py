from core.Relay.RelayExpr import *
from core.Relay.RelayLayer import *
from core.tir.stmt.Stmt import *
from core.tir.expr.Expr import *
from core.tir.Pass.PassFunctors import *

class TIRMapperFunctor(FunctorRelayExprNode):
    ##
    # Map RelayExpr to TIR Stmt
    ##
    pass

class ScheduleFunctor(FunctorStmtNode, FunctorExprNode):
    def visit_stmt(self, node, extra):
        pass_list = extra
        if isinstance(node, IfStmtNode):
            self.visit_If(node, extra)
        elif isinstance(node, ForStmtNode):
            self.visit_For(node, extra)
        #node_clone = node.clone()
        print(node.nodeid)
        if node.nodeid in pass_list[1]:
            pass_functor = pass_list[0][pass_list[1].index(node.nodeid)]
            #if node==isinstance(stmt):
            node_transform = pass_functor.visit_stmt(node, pass_list[2][pass_list[1].index(node.nodeid)])
            node = node_transform
        #node = node_clone
        return node
    def visit_expr(self, node, extra):
        ## Expr couldn't applied schedules
        #node_clone = node.clone()
        #node = node_clone
        if isinstance(node, VarExprNode):
            self.visit_var(node, extra)
        return node

    # Stmt
    def visit_If(self, node, extra):
        node.nodes['cond'] = node.nodes['cond'].accept(self, extra)
        node.nodes['expr_true'] = node.nodes['expr_true'].accept(self, extra)
        node.nodes['expr_false'] = node.nodes['expr_false'].accept(self, extra)
    def visit_For(self, node, extra):
        node.nodes['init'] = node.nodes['init'].accept(self, extra)
        node.nodes['cond'] = node.nodes['cond'].accept(self, extra)
        node.nodes['increment'] = node.nodes['increment'].accept(self, extra)
        node.nodes['loop_code'] = node.nodes['loop_code'].accept(self, extra)

    # Expr
    def visit_var(self, node, extra):
        return None

class Scheduler:
    def __init__(self, graph):
        self.orig_graph = graph
        self.dest_graph = None
        self.loop_unrolling_functor = LoopUnrollingFunctor()
        self.loop_tiling_functor = LoopTilingFunctor()
        self.vectorize_functor = VectorizeFunctor()
        self.schedule_functor = ScheduleFunctor()
        self.pass_list = [[], [], []] # Type, Target Node, Extra info(unroll factor, ...)

    def regist_loop_unroll(self, node, unroll_factor):
        self.pass_list[0].append(self.loop_unrolling_functor)
        self.pass_list[1].append(node.nodeid)
        self.pass_list[2].append(unroll_factor)
    def regist_loop_tiling(self, node):
        self.pass_list[0].append(self.loop_tiling_functor)
        self.pass_list[1].append(node.nodeid)
        self.pass_list[2].append(None)
    def regist_vectorize(self, node):
        self.pass_list[0].append(self.vectorize_functor)
        self.pass_list[1].append(node.nodeid)
        self.pass_list[2].append(None)

    def apply_schedule(self):
        self.dest_graph = self.orig_graph.clone()
        self.dest_graph = self.schedule_functor.visit_stmt(self.dest_graph, self.pass_list)
        return self.dest_graph
