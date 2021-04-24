from core.util import Layout
from core.util import Shape
from core.Relay.RelayExpr import *

class InputRelayLayerNode(LayerRelayExprNode):
    '''
    Relay Input Layer Expr Node : opaque
    Lname
    '''
    def __init__(self, name):
        self.name = name

class Conv2DRelayLayerNode(LayerRelayExprNode):
    '''
    Relay Conv2D Layer Expr Node : complex-out-fusable
    Lname, bottom layer, shape of weight, bias, filter, stride, padding
    '''
    weight_shape = Shape([0,0,0,0])
    optimal_weight_layout = Layout.NCHW
    bias_shape = Shape([0,0,0,0])
    optimal_bias_layout = Layout.NCHW

    kernelSize = Shape([0,0,1,1])
    stride = Shape([1,1,1,1])
    padding = Shape([0,0,0,0])

    def __init__(self, name, in_layer0, shape_w, shape_b, shape_k, shape_s, shape_p):
        self.name = name
        self.input_layer0 = in_layer0
        self.weight_shape = shape_w
        self.bias_shape = shape_b
        self.kernelSize = shape_k
        self.stride = shape_s
        self.padding = shape_p

class AddRelayLayerNode(LayerRelayExprNode):
    '''
    Relay Eltwise Add Layer Expr Node : injective
    Lname, bottom layer 0, 1
    '''
    def __init__(self, name, in_layer0, in_layer1):
        self.name = name
        self.input_layer0 = in_layer0
        self.input_layer1 = in_layer1

class BatchNormRelayLayerNode(LayerRelayExprNode):
    '''
    Relay BatchNorm Layer Expr Node : injective
    Lname, bottom layer, shape of r,B,m,v
    '''
    gamma_shape = Shape([0,0,0,0])
    beta_shape = Shape([0,0,0,0])
    mean_shape = Shape([0,0,0,0])
    var_shape = Shape([0,0,0,0])
    optimal_gamma_layout = Layout.NCHW
    optimal_beta_layout = Layout.NCHW
    optimal_mean_layout = Layout.NCHW
    optimal_var_layout = Layout.NCHW

    def __init__(self, name, in_layer0, shape_g, shape_b, shape_m, shape_v):
        self.name = name
        self.input_layer0 = in_layer0
        self.gamma_shape = shape_g
        self.beta_shape = shape_b
        self.mean_shape = shape_m
        self.var_shape = shape_v

class PaddingRelayLayerNode(LayerRelayExprNode):
    '''
    Relay Padding Layer Expr Node : injective?
    Lname, bottom layer, shape of padding
    '''
    padding = Shape([0,0,0,0])

    def __init__(self, name, in_layer0, shape_p):
        self.name = name
        self.input_layer0 = in_layer0
        self.padding = shape_p

class ActivationRelayLayerNode(LayerRelayExprNode):
    '''
    Relay Activation Layer Expr Node : injective
    Lname, bottom layer, activation type
    '''
    act_type = 0 #ReLU

    def __init__(self, name, in_layer0, activation):
        self.name = name
        self.input_layer0 = in_layer0
        self.act_type = activation

