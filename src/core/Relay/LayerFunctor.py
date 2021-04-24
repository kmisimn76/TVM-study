from core.Relay.RelayExpr import *
from core.Relay.RelayLayer import *

def print_indent(message, indent):
    for i in range(indent):
        print("   ", end='')
        print(message)


class PrintFunctor(FunctorRelayExprNode):
    def visit(self, node, extra):
        visited = extra
        visited[node.name] = True
        if isinstance(node, Conv2DRelayLayerNode):
            if node.input_layer0.name not in visited.keys():
                node.input_layer0.accept(self, visited)
            print_indent(node.name + " Conv "+str(node.input_shape), 1)
        elif isinstance(node, AddRelayLayerNode):
            if node.input_layer0.name not in visited.keys():
                node.input_layer0.accept(self, visited)
            if node.input_layer1.name not in visited.keys():
                node.input_layer1.accept(self, visited)
            print_indent(node.name + " Add: "+node.input_layer0.name+" + "+node.input_layer1.name, 1)
        elif isinstance(node, BatchNormRelayLayerNode):
            if node.input_layer0.name not in visited.keys():
                node.input_layer0.accept(self, visited)
            print_indent(node.name + " BatchNorm "+str(node.input_shape), 1)
        elif isinstance(node, PaddingRelayLayerNode):
            if node.input_layer0.name not in visited.keys():
                node.input_layer0.accept(self, visitied)
            print_indent(node.name + " Padding "+str(node.input_shape), 1)
        elif isinstance(node, ActivationRelayLayerNode):
            if node.input_layer0.name not in visited.keys():
                node.input_layer0.accept(self, visited)
            print_indent(node.name + " Activation("+str(node.act_type)+") "+str(node.input_shape), 1)
        return None

class ShapeInferenceFunctor(FunctorRelayExprNode):
    def visit(self, node, extra):
        in_shape, visited = extra
        visited[node.name] = True
        if isinstance(node, InputRelayLayerNode):
            node.input_shape = Shape(in_shape)
            return Shape(in_shape)
        if isinstance(node, Conv2DRelayLayerNode):
            input_shape = node.input_layer0.accept(self,[in_shape, visited])
            node.input_shape = Shape(input_shape)
            output_shape = Shape(input_shape)
            output_shape = (output_shape - node.kernelSize + node.padding + node.padding) // node.stride + Shape([0,0,1,1])
            output_shape.shape[0] = input_shape.shape[0]
            output_shape.shape[1] = node.weight_shape.shape[0]
        elif isinstance(node, BatchNormRelayLayerNode):
            input_shape = node.input_layer0.accept(self,[in_shape, visited])
            node.input_shape = Shape(input_shape)
            output_shape = Shape(input_shape)
        elif isinstance(node, AddRelayLayerNode):
            input_shape = node.input_layer0.accept(self,[in_shape, visited])
            input_shape_2 = node.input_layer1.accept(self,[in_shape, visited])
            node.input_shape = Shape(input_shape)
            output_shape = Shape(input_shape)
        elif isinstance(node, PaddingRelayLayerNode):
            input_shape = node.input_layer0.accept(self,[in_shape, visited])
            node.input_shape = Shape(input_shape)
            output_shape = Shape(input_shape)
            output_shape = output_shape + node.padding
        elif isinstance(node, ActivationRelayLayerNode):
            input_shape = node.input_layer0.accept(self,[in_shape, visited])
            node.input_shape = Shape(input_shape)
            output_shape = Shape(input_shape)
        return output_shape


class LayerFusionFunctor(FunctorRelayExprNode):
    ###
    # Functor for Layer Fusion
    # Needs: Function Relay Expr Node
    # Note that:
    #   1. Injective: One-by-one map (ex. add)
    #   2. Reduction: Reduced size for a dimension (ex. Sum)
    #   3. Complex: can fuse eltwise map to output (ex. Convolution)
    #   4. Opaque: Cannot be fused (ex. sort)
    # To do:
    #   1. Injective operators Fusing
    #   2. Fusing between Injective -> Reduction
    #   3. Fusing between Complex & <Injective or Reduction>
    ###
    pass

class LayoutTransformFucntor(FunctorRelayExprNode):
    ###
    # Functor for Layout Transformnation
    # Objective:
    #   Determine Optimal input Layout
    # To do :
    #   0. Apply optimal HW operation
    #   1. Pre-defining Optimal Layout for each layer in such an environment (consider HW operator)
    #   2. Insert proper transform overhead(operation)
    ###
    pass
