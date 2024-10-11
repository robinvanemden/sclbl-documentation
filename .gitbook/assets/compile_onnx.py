from os.path import *
import onnx

from hailo_sdk_client import ClientRunner

_here = dirname(abspath(__file__))

onnx_model_name = 'model'
onnx_path = join(_here, 'model.onnx')   # TODO: insert the path to the ONNX model

output_onnx_path = splitext(onnx_path)[0] + '_hailo.onnx'
chosen_hw_arch = 'hailo8'               # TODO: set the target hardware architecture

# TODO: Update this function to load your calibration dataset
def load_coco_val_images():
    val_dir = join(_here, 'val2017')
    from PIL import Image
    import os
    import numpy as np
    mean = 0        # TODO: set the mean value of the mode
    std = 1         # TODO: set the standard deviation value of the model
    images = []
    for img in os.listdir(val_dir):
        img = Image.open(os.path.join(val_dir, img)).convert('RGB')
        img = img.resize((640, 640))    # TODO: change
        img = np.array(img).astype('float32')
        img = (img - mean) / std
        images.append(img)
    return np.array(images)

def calib_dataset():
    return load_coco_val_images()

runner = ClientRunner(hw_arch=chosen_hw_arch)
hn, npz = runner.translate_onnx_model(onnx_path, onnx_model_name,
                                start_node_names=['sclbl-onnx-node1'],  # TODO: set the start node names       
                                end_node_names=['Conv_66',   # TODO: set the end node names
                                                'Conv_282'], 
)

runner.optimize(calib_dataset())

hef = runner.compile() # the returned HEF is not needed when working with ONNXRT
onnx_model = runner.get_hailo_runtime_model() # only possible on a compiled model
onnx_file = onnx.save(onnx_model , output_onnx_path) # save model to file