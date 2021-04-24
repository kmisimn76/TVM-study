import sys
sys.path.append("/home/sumin/workspace/TVM-study/src") ##HARDCODDED

from core.tir.expr.Expr import *
from core.tir.stmt.Stmt import *
from core.tir.UtilFunctors import *
from core.lower.declaration import *

tir_print_functor = TIRPrintFunctor()

##
# for(i=0;i<n;i=i+1) {
#   for(j=0;j<100;j=j+1) { ===> Unroll Target
#       for(l=0;l<j;l=l+1) {
#           B[i] = B[i] + A[i] + j+l;
#       }
#   }
# }
##

# B[i] = B[i] + A[i] + j+l;
loop_body = AllocStmtNode(ArrayExprNode("B", VarExprNode("i")), AddExprNode(ArrayExprNode("B", VarExprNode("i")),
                        AddExprNode(ArrayExprNode("A", VarExprNode("i")), AddExprNode(VarExprNode("j"), VarExprNode("l")) )) )

# for(l=0;l<j;l=l+1)
inner_most_for = ForStmtNode(AllocStmtNode(VarExprNode("l"), ConstExprNode("0")),
                        CompExprNode(VarExprNode("l"), VarExprNode("j"), EXPR_COMPARE_TYPE_LT),
                        AllocStmtNode(VarExprNode("l"), AddExprNode(VarExprNode("l"), ConstExprNode("1"))),
                        loop_body)


# for(j=0;j<100;j=j+1)
inner_for = ForStmtNode(AllocStmtNode(VarExprNode("j"), ConstExprNode("0")),
                        CompExprNode(VarExprNode("j"), ConstExprNode("100"), EXPR_COMPARE_TYPE_LT),
                        AllocStmtNode(VarExprNode("j"), AddExprNode(VarExprNode("j"), ConstExprNode("1"))),
                        inner_most_for)

# for(i=0;i<n;i=i+1)
outer_for = ForStmtNode(AllocStmtNode(VarExprNode("i"), ConstExprNode("0")), 
                        CompExprNode(VarExprNode("i"), VarExprNode("n"), EXPR_COMPARE_TYPE_LT), 
                        AllocStmtNode(VarExprNode("i"), AddExprNode(VarExprNode("i"), ConstExprNode("1"))),
                        inner_for)

graph = outer_for

code = tir_print_functor.visit_stmt(graph, None)
print(code)


#Loop Unrolling with Scheduler
unroll_scheduler = Scheduler(graph)

unroll_scheduler.regist_loop_unroll(inner_for, 4)
unroll_scheduler.regist_loop_unroll(inner_most_for, 2)
unroll_scheduler.regist_loop_unroll(outer_for, 2)
opt_graph = unroll_scheduler.apply_schedule()

code = tir_print_functor.visit_stmt(opt_graph, None)
print(code)
