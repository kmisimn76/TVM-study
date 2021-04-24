from core.tir.stmt.Stmt import *
from core.tir.expr.Expr import *

def ad_indent(code):
    code = "    " + code
    code = code.replace('\n','\n    ')
    return code

class TIRPrintFunctor(FunctorStmtNode, FunctorExprNode):
    def visit_stmt(self, node, extra):
        if isinstance(node, ForStmtNode):
            code_init = node.nodes['init'].accept(self, extra)
            code_cond = node.nodes['cond'].accept(self, extra)
            code_increment = node.nodes['increment'].accept(self, extra)
            code_loop_code = node.nodes['loop_code'].accept(self, extra) + ";"
            code = "for ("+code_init+"; "+code_cond+"; "+code_increment+") {\n"
            code = code + ad_indent(code_loop_code)
            code = code + "\n}\n"
            return code
        elif isinstance(node, AllocStmtNode):
            code_tar = node.nodes['tar'].accept(self, extra)
            code_src = node.nodes['src'].accept(self, extra)
            code = code_tar+" = "+code_src
            return code
        elif isinstance(node, StatementsStmtNode):
            code = ""
#            for nd in node.nodes['stmts']:
            for nd in node.nodes.values():
                code = code + nd.accept(self, extra) + ";\n"
            return code
    def visit_expr(self, node, extra):
        if isinstance(node, VarExprNode):
            code = node.name
            return code
        elif isinstance(node, ArrayExprNode):
            code = node.name+"["+node.nodes['index'].accept(self, extra)+"]"
            return code
        elif isinstance(node, ConstExprNode):
            code = node.value
            return code
        elif isinstance(node, AddExprNode):
            code = "("+node.nodes['A'].accept(self, extra)+" + "+node.nodes['B'].accept(self, extra)+")"
            return code
        elif isinstance(node, CompExprNode):
            comp_list = ['==', '!=', '>', '<']
            comp = comp_list[node.comp_type]
            code = node.nodes['A'].accept(self, extra)+" " + comp + " "+node.nodes['B'].accept(self, extra)
            return code
