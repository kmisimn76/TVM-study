from Stmt import *

# C Lowering
class CLowerFunctor(FunctorStmtNode, FunctorExprNode):
    def visit_stmt(self, node, extra):
        indent = extra
        if isinstance(node, IfThenElseStmtNode):
            return self.visit_If(node, extra)
        elif isinstance(node, ForStmtNode):
            return self.visit_For(node, extra)
    def visit_expr(self, node, extra):
        indent = extra

    def visit_If(self, node, extra):
        code_cond = node.cond.accept(self)
        code_expr_true = node.expr_true.accept(self)
        code_expr_false = node.expr_false.accept(self)
        code = " if("+code_cond+") {\n" + code_expr_true +"\n} else {\n" \
                + code_expr_false + "}\n"
        return code
    def visit_For(self, node, extra):
        code_init = node.init.accept(self)
        code_cond = node.cond.accept(self)
        code_increment = node.increment.accept(self)
        code_loop_code = node.loop_code.accept(self)
        code = " for("+code_init+";"+code_cond+";"+code_increment+") {\n" \
                + code_loop_code + "}\n"
        return code

# OpenCL Lowering
class OpenCLLowerFunctor(FunctorStmtNode, FunctorExprNode):
    def visit_stmt(self, node, extra):
        indent = extra
        if isinstance(node, IfThenElseStmtNode):
            return self.visit_If(node, extra)
        elif isinstance(node, ForStmtNode):
            return self.visit_For(node, extra)
    def visit_expr(self, node, extra):
        indent = extra

    def visit_If(self, node, extra):
        code_cond = node.cond.accept(self)
        code_expr_true = node.expr_true.accept(self)
        code_expr_false = node.expr_false.accept(self)
        code = " if("+code_cond+") {\n" + code_expr_true +"\n} else {\n" \
                + code_expr_false + "}\n"
        return code
    def visit_For(self, node, extra):
        code_init = node.init.accept(self)
        code_cond = node.cond.accept(self)
        code_increment = node.increment.accept(self)
        code_loop_code = node.loop_code.accept(self)
        code = " for("+code_init+";"+code_cond+";"+code_increment+") {\n" \
                + code_loop_code + "}\n"
        return code

