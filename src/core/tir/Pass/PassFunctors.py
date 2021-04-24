from core.tir.stmt.Stmt import *
from core.tir.expr.Expr import *

# LoopUnrolling Pass of TIR Statement (Halide: Loop Transform)
class LoopUnrollingFunctor(FunctorStmtNode):
    def visit_stmt(self, node, extra):
        '''
        LoopUnrolling visit functor
        Extra: (const int) unroll factor
        '''
        if isinstance(node, ForStmtNode):
            return self.visit_For(node, extra)
        else:
            print("Not defined loop unroll")
            return node

    def visit_For(self, node, extra):
        if (isinstance(node.nodes['increment'], AllocStmtNode) and isinstance(node.nodes['increment'].nodes['src'], AddExprNode) and isinstance(node.nodes['increment'].nodes['src'].nodes['B'], ConstExprNode) and isinstance(node.nodes['init'], AllocStmtNode) and isinstance(node.nodes['init'].nodes['tar'], VarExprNode) and isinstance(node.nodes['cond'], CompExprNode) and isinstance(node.nodes['cond'].nodes['A'], VarExprNode)) is not True:
            print("Not supported: increment isn't const add or driver variable isn't specified")
            return node
        node = node.clone()
        unroll_factor = int(extra)
        unroll_var = node.nodes['cond'].nodes['A'].name
        incre_size = int(node.nodes['increment'].nodes['src'].nodes['B'].value)
        new_loop_code_stmts = []
        for i in range(0, incre_size*unroll_factor, incre_size):
            node_loop_code_clone = node.nodes['loop_code'].clone()
            # Node traversal
            nlist = [(node_loop_code_clone, None, None)]
            n_front = 0
            while n_front < len(nlist):
                sel_node, sel_parent, sel_key = nlist[n_front]
                n_front += 1
                nlist.extend(list(zip(sel_node.nodes.values(), [sel_node]*len(sel_node.nodes), sel_node.nodes.keys())))
                # var -> var+f, var -> var+f*2 ...
                if isinstance(sel_node, VarExprNode) and sel_node.name == unroll_var:
                    sel_node = AddExprNode(sel_node, ConstExprNode(str(i)))
                    sel_parent.nodes[sel_key] = sel_node
            new_loop_code_stmts.append(node_loop_code_clone)
        new_loop_code = StatementsStmtNode(new_loop_code_stmts)
        node = ForStmtNode(node.nodes['init'], node.nodes['cond'],
                            AllocStmtNode(VarExprNode(unroll_var),AddExprNode(VarExprNode(unroll_var),ConstExprNode(str(incre_size*unroll_factor)))), new_loop_code)
        return node
        

# LoopTiling (Halide: Loop Transform)
class LoopTilingFunctor(FunctorStmtNode):
    def visit_stmt(self, node, extra):
        if isinstance(node, IfThenElseStmtNode):
            return self.visit_If(node, extra)
        elif isinstance(node, ForStmtNode):
            return self.visit_For(node, extra)

    def visit_If(self, node, extra):
        pass
    def visit_For(self, node, extra):
        pass

# Vetorize (Halide: Increasing Compute Locality)
class VectorizeFunctor(FunctorStmtNode):
    def visit_stmt(self, node, extra):
        if isinstance(node, IfThenElseStmtNode):
            return self.visit_If(node, extra)
        elif isinstance(node, ForStmtNode):
            return self.visit_For(node, extra)

    def visit_If(self, node, extra):
        pass
    def visit_For(self, node, extra):
        pass

# Nested Parallelism with Cooperation(Using Shared Memory) (TVM: Data reuse)
class ThreadCooperationFunctor(FunctorStmtNode):
    ###
    # Data reuse using Shared Memory
    # To do:
    #   1. Construct shared data -> Thraed Barrier
    #   2. Compute operation using shared data
    ###
    def visit_stmt(self, node, extra):
        if isinstance(node, IfThenElseStmtNode):
            return self.visit_If(node, extra)
        elif isinstance(node, ForStmtNode):
            return self.visit_For(node, extra)
    def visit_If(self, node, extra):
        pass
    def visit_For(self, node, extra):
        pass

# Tensorize (TVM: HW Acceleration)
class TensorizeFunctor(FunctorStmtNode):
    ###
    # Tensorize
    # To do:
    #   1. 
    ###
    def visit_stmt(self, node, extra):
        if isinstance(node, IfThenElseStmtNode):
            return self.visit_If(node, extra)
        elif isinstance(node, ForStmtNode):
            return self.visit_For(node, extra)

    def visit_If(self, node, extra):
        pass
    def visit_For(self, node, extra):
        pass

# Latency Hiding (TVM: Exploit HW unit)
class LatencyHidingFunctor(FunctorStmtNode):
    ###
    # Latency Hiding
    # To do:
    #   1. Check dependency between two(or more) operations(Assembly level)
    #   2. Loop unrolling
    ###
    def visit_stmt(self, node, extra):
        if isinstance(node, IfThenElseStmtNode):
            return self.visit_If(node, extra)
        elif isinstance(node, ForStmtNode):
            return self.visit_For(node, extra)

    def visit_If(self, node, extra):
        pass
    def visit_For(self, node, extra):
        pass


