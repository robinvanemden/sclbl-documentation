# Hailo Support

It's currently possible to convert Teachable Machine models to the Hailo-ONNX format on the cloud.

Other generic ONNX models need to be locally compiled by the user using the Hailo dataflow compiler, then upload the generated file to the Nx AI Cloud. This is due to the nature of compiling ONNX models to Hailo format. For this the user needs to upload calibration images and specify the subgraph that can be accelerated by the Hailo chips. This is not possible in the available cloud conversion.

### Deploying on x86\_64 machine with Hailo-8

1. The first step is to verify that you have a compatible HailoRT driver installed. Please check out this [table](supported-ai-accelerators.md) to determine if your driver version is supported.
2. Next, install the Nx AI plugin by following [these instructions](../nx-ai-manager/2.-install-nx-ai-manager-plugin.md).
3. If all is well, you should be able to select the Hailo runtime when enabling the Nx plugin as shown below:

![](../.gitbook/assets/hailo-runtime-in-plugin-ui.png)

4. After the installation is finished, the plugin interface will look something like this:

![](../.gitbook/assets/plugin-ui.png)

5. To manually verify that the Hailo runtime is downloaded and set up, feel free to check out the content of the `bin` folder of the AI Manager and make sure it contains these files:\
   \- libhailort.so.4.xx.0\
   \- libonnxruntime\_providers\_hailo.so\
   \-libonnxruntime\_providers\_shared.so\
   \- libRuntimeLibrary.so

```sh
ubuntu@ThinkStation-P360-Tower:~$ ls /opt/networkoptix-metavms/mediaserver/bin/plugins/nxai_plugin/nxai_manager/bin/
installed_runtime.txt libhailort.so.4.17.0 libonnxruntime_providers_hailo.so libonnxruntime_providers_shared.so libRuntimeLibrary.so sclbld sclblmod
```

6. Finally, to deploy a model that can be accelerated on the Hailo chip, make sure that it has a `application/x-onnx; device=hailo` model file in the Nx AI Cloud:

![](../.gitbook/assets/model-files-2.png)

If it's not the case, you'll need to manually compile the ONNX model, and upload the generated model to the cloud. Please refer to [this](https://github.com/OAAX-standard/contributions/tree/main/Hailo-8) page for a quick start guide.

### Common issues

* Sometimes, after compiling an ONNX model to a Hailo-ONNX, the input names and shapes are _not_ kept intact. Hence, the model might not work properly within the Nx AI Manager. \
  So, please make sure that the generated ONNX is conforming to our [specification](../for-data-scientists/onnx-requirements.md).
