import onnx
from os.path import *

_here = dirname(abspath(__file__))
onnx_path = join(_here, 'model_hailo.onnx')         # TODO: insert the path to the ONNX model
new_onnx_path = splitext(onnx_path)[0] + '_new.onnx'
# Load the ONNX model
model = onnx.load(onnx_path)

# get the graph
graph = model.graph

# remote "post_" prefix from the input and output names
for i in range(len(graph.input)):
    old_name = graph.input[i].name
    if old_name == 'input0':
        graph.input[i].name = 'image-'
    graph.input[i].name = graph.input[i].name.replace("post_", "")
    # replace old name with new one in all nodes inputs & outputs
    for node in graph.node:
        for j in range(len(node.input)):
            if node.input[j] == old_name:
                node.input[j] = graph.input[i].name
                print(node.name, graph.input[i].name)
        for j in range(len(node.output)):
            if node.output[j] == old_name:
                node.output[j] = graph.input[i].name
                print(node.name, node.output)
for i in range(len(graph.output)):
    old_name = graph.output[i].name
    graph.output[i].name = old_name.replace("post_", "")
    # replace old name with new one in all nodes inputs & outputs
    for node in graph.node:
        for j in range(len(node.input)):
            if node.input[j] == old_name:
                node.input[j] = graph.output[i].name
                print(node.name, node.input)
        for j in range(len(node.output)):
            if node.output[j] == old_name:
                node.output => CACHED [ 5/11] RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections                                                          0.0s[j] = graph.output[i].name
                print(node.name, node.output)

# Update shape of nms_sensitivity- input to [1]
for i in range(len(graph.input)):
    if graph.input[i].name == 'nms_sensitivity-':
        graph.input[i].type.tensor_type.shape.dim[0].dim_value = 1

# Update shape of mask- input to [640, 640]
for i in range(len(graph.input)):
    if graph.input[i].name == 'mask-':
        graph.input[i].type.tensor_type.shape.dim[0].dim_value = 640    # TODO: change to the new shape
        graph.input[i].type.tensor_type.shape.dim[1].dim_value = 640    # TODO: change to the new shape

# Replace shape of the output to [20, 6]
for i in range(len(graph.output)):
    assert i==0
    graph.output[i].type.tensor_type.shape.dim[0].dim_value = 20
    graph.output[i].type.tensor_type.shape.dim[1].dim_value = 6
# Save the ONNX model
onnx.save(model, new_onnx_path)

