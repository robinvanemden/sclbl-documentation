# 3.1 Model Settings

<figure><img src="../../.gitbook/assets/Screenshot From 2025-01-24 14-38-59.png" alt=""><figcaption><p>A device is one model pipeline with a single model</p></figcaption></figure>

A model that is active on a device can have multiple settings These settings depend on the capabilities of the model or the server.

When you change one of these settings, the pipeline form will change to indicate that the settings need to be saved manually.

<figure><img src="../../.gitbook/assets/Screenshot From 2025-01-24 14-44-15.png" alt=""><figcaption><p>A model pipeline form with changed settings that are not saved yet</p></figcaption></figure>

To save the settings, click the "Save pipelines" button. If you do not want to save the settings, refreshing the page will reset the form. Navigating away from the device details page will also reset the form without saving the settings.

### Model NMS Threshold

The NMS Threshold (Non Max Suppression) sets the cut off for when models should not return detections with a probability score below the current threshold value.

This is a setting that is model dependent, so not all models have this option.

### Preprocessor

If the server that the device is connected to has any preprocessors available, they can be selected here.

This is a setting that is server dependent, so moving a device to another server may change the available options.

### Postprocessor

If the server that the device is connected to has any postprocessors available, they can be selected here.

This is a setting that is server dependent, so moving a device to another server may change the available options.

