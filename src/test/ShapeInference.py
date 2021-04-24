import sys
sys.path.append("/home/sumin/workspace/TVM-study/src") ##HARDCODDED

from core.Relay.RelayExpr import *
from core.Relay.RelayLayer import *
from core.Relay.LayerFunctor import *

PrintFunc = PrintFunctor()
ShapeInferFunc = ShapeInferenceFunctor()

layer_in = InputRelayLayerNode("Input")
layer_conv1 = Conv2DRelayLayerNode("Conv1", layer_in, Shape([5,3,3,3]), Shape([5,0,0,0]), Shape([0,0,3,3]), Shape([2,2,2,2]), Shape([1,1,1,1]))
layer_bn1 = BatchNormRelayLayerNode("bn1", layer_conv1, Shape([0,0,0,5]), Shape([0,0,0,5]), Shape([0,0,0,5]), Shape([0,0,0,5]))
layer_act1 = ActivationRelayLayerNode("act1", layer_bn1, 0)
layer_conv_f = Conv2DRelayLayerNode("Conv_f", layer_in, Shape([5,3,3,3]), Shape([5,0,0,0]), Shape([0,0,3,3]), Shape([2,2,2,2]), Shape([1,1,1,1]))
layer_add1 = AddRelayLayerNode("Add1", layer_act1, layer_conv_f)

output_shape = ShapeInferFunc.visit(layer_add1, [Shape([2, 3, 224, 224]), {}])

PrintFunc.visit(layer_add1, {})
print(output_shape)
