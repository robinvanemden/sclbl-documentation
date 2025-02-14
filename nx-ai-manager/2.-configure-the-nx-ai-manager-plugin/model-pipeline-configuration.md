# 3.2 Model pipeline selection and configuration

The device detail page is the central place to manage the model pipelines that the device should run.

Pipelines are chains of one or more models that can run with the given video input from the device.

Usually a device has a default pipeline configured after the plugin is enabled for the device.

### Add a new pipeline

When no pipelines are set, the only available option is to add a new pipeline:

<figure><img src="../../.gitbook/assets/Screenshot From 2025-01-24 14-54-35.png" alt=""><figcaption><p>A device detail page without any pipelines</p></figcaption></figure>

Clicking the "Add a pipeline" button redirects you to the model catalogue.

### Selecting a model

In the model catalogue you can select a model to use in the new (or current) pipeline.

The top of the page will show a message that you are "Currently assigning...".

If you have uploaded custom models, they will be available here.

<figure><img src="../../.gitbook/assets/Screenshot From 2025-01-24 14-58-34.png" alt=""><figcaption><p>The model catalogue with the assignment message and the option to select a model for the current pipeline</p></figcaption></figure>

When a model is selected it will be assigned and downloaded to the server that the client is connected to.

<figure><img src="../../.gitbook/assets/Screenshot From 2025-01-24 14-58-50.png" alt=""><figcaption><p>Message that the model will be added to the server</p></figcaption></figure>

You will be redirected to the device details page again, with the newly assigned model.

<figure><img src="../../.gitbook/assets/Screenshot From 2025-01-24 14-58-55.png" alt=""><figcaption><p>The device detail page with a single pipeline containing one model</p></figcaption></figure>

### Add a chained model

Chained models are models that use the input of a parent model instead of processing the video from the device directly.

You add a chained model by clicking the chain icon <img src="../../.gitbook/assets/image (124).png" alt="" data-size="line"> next to the parent model name. You will be redirected to the model catalogue to select a chained model.

<figure><img src="../../.gitbook/assets/Screenshot From 2025-01-24 14-43-44.png" alt=""><figcaption><p>Model pipeline with settings and buttons to manage models in the pipeline</p></figcaption></figure>

The way a chained model will use the input can be selected, currently there are three modes:

* Direct - the chained model gets the output from the parent model as input
* Conditional - the chained model will only run if a field with a given name outputs "`true`"
* Feature extraction - the chained model will get the contents of the bounding boxes that have a certain label

<figure><img src="../../.gitbook/assets/Screenshot From 2025-01-24 15-17-15.png" alt=""><figcaption><p>A model pipeline with chaining options</p></figcaption></figure>

Choose the appropriate method, and when you have entered new data the pipeline form will change to indicate that settings need to be saved.

<figure><img src="../../.gitbook/assets/Screenshot From 2025-01-24 15-21-00.png" alt=""><figcaption><p>A model pipeline with changes that need to be saved</p></figcaption></figure>

The settings will be applied to the device when you click the "Save pipelines" button.

### Change a model in a pipeline

A parent model or a chained model can be replaced by clicking the left-right arrow button next to the chained model title <img src="../../.gitbook/assets/Screenshot From 2025-01-24 15-31-46.png" alt="" data-size="line">. This will redirect you to the normal model selection process where you can select a replacement model.&#x20;

The rest of the settings in the model pipeline are not affected, unless they are directly related to the model.

### Remove a chained model from a chain

Removing a model from a chain can be done by clicking the delete button next to a chained model <img src="../../.gitbook/assets/Screenshot From 2025-01-24 15-24-42.png" alt="" data-size="line"> and the model will be removed directly.

Undoing is not possible, to undo this you can select the same model again.

### Remove a chain

Removing a chain with all the models and settings can be done by clicking the delete button next to a parent model in a chain <img src="../../.gitbook/assets/Screenshot From 2025-01-24 15-24-42 (1).png" alt="" data-size="line"> and the full model chain with all associated settings and chained models will be removed.

Undoing is not possible, to restore the settings the same model chain must be rebuilt completely.
