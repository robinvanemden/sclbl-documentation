# 3.3 Model pipelines on multiple devices

Multiple devices can be managed at the same time, but this feature is limited at the moment. You can create a new model pipeline for multiple devices, but the [chained models](model-pipeline-configuration.md) inside a pipeline as well as the [model settings](model-settings.md) must be set per device.

Setting multiple pipelines can only be done for a single site at a time.

## Creating a new pipeline on multiple devices

Start at the site page, where you can see all the available devices on the available servers.

<figure><img src="../../.gitbook/assets/Screenshot From 2025-01-24 14-33-14 (2).png" alt=""><figcaption><p>The site details page with the list of available devices</p></figcaption></figure>

The highlighted "here" link starts the process and enables the checkboxes next to the available devices. Devices on servers are marked with a chain icon next to the version number support model pipelines.

<figure><img src="../../.gitbook/assets/Screenshot From 2025-01-24 14-33-22.png" alt=""><figcaption><p>The site details page with checkboxes for the available devices</p></figcaption></figure>

Only devices that are enabled can be selected.

<figure><img src="../../.gitbook/assets/Screenshot From 2025-01-24 14-33-36.png" alt=""><figcaption><p>The site details page with selected devices</p></figcaption></figure>

When one or more devices are selected the "Assign a new pipeline" button is enabled and can be clicked. This will redirect you to the models page where you will see the message "Currently assigning..." that is indicating the amount of devices that will receive the new pipeline.

<figure><img src="../../.gitbook/assets/Screenshot From 2025-01-24 15-49-04.png" alt=""><figcaption><p>The model catalogue with the assignment message and the option to select a model for the current pipeline</p></figcaption></figure>



<figure><img src="../../.gitbook/assets/Screenshot From 2025-01-24 14-34-01.png" alt=""><figcaption><p>The model catalogue with a highlighted button to select a model for the current pipeline</p></figcaption></figure>

When you click the "Add to pipeline..." button a confirmation dialog will appear, because the next action is irreversible. Confirm to wipe all existing model pipelines on the selected devices and replace them with the new pipeline containing the single selected model.

When you are unsure, clicking cancel will prevent the assignment, but will not change the selected devices. To also unset the selected devices for assignment click the "Cancel the assignment" button at the top of the page.

<figure><img src="../../.gitbook/assets/Screenshot From 2025-01-24 14-34-07.png" alt=""><figcaption><p>The model catalogue with a dialog explaing the replacement</p></figcaption></figure>

After you've confirmed the new model pipeline will be deployed to all selected devices

<figure><img src="../../.gitbook/assets/Screenshot From 2025-01-24 14-34-11.png" alt=""><figcaption><p>Message about the deployment to multiple devices</p></figcaption></figure>

You can verify the deployment of the new model pipeline by checking one or all the previously selected devices.

<figure><img src="../../.gitbook/assets/Screenshot From 2025-01-24 14-35-03.png" alt=""><figcaption><p>The device detail page with a single pipeline containing one model</p></figcaption></figure>

The rest of the configuration must be done per device at the moment. This includes setting NMS Thresholds per model, pre and postprocessors and chained models.
