# Upload your model

After you have [created your model](../../for-data-scientists/custom-model-creation.md) and made sure it [conforms to the Nx ONNX requirements](../../for-data-scientists/onnx-requirements.md), you can easily upload it to make it available in Nx Cloud and, thereby, to all your Nx Servers. First, click on the "Add a model" button, top left:

<figure><img src="../../.gitbook/assets/Screenshot From 2025-01-27 11-16-56.png" alt=""><figcaption></figcaption></figure>

Next, choose (in the case of an ONNX model)  the "ONNX" upload button:&#x20;

<figure><img src="../../.gitbook/assets/Screenshot From 2025-01-24 14-32-24.png" alt=""><figcaption></figcaption></figure>

Drag and drop your ONNX model into the drag and drop area, choose a name for your model, add some documentation, and, potentially, set its [normalisation values](normalization.md):

<figure><img src="../../.gitbook/assets/Screenshot From 2025-01-27 11-19-01.png" alt=""><figcaption></figcaption></figure>

After the model is uploaded, a series of conversions will be run to generate optimized model files for each supported target [AI accelerator](../../ai-accelerators-support/supported-ai-accelerators.md).

When this is completed you will get an email and the model is [ready to be used](../use-your-model.md) on your devices.

