---
description: >-
  This page gives instructions on how to configure basic operations of the Nx AI
  Manager plugin
---

# 3. Configure the Nx AI Manager plugin

Configure Nx Meta

After successful installation of Nx Server and Client, a 'Plugins' tab should be visible when opening a camera's settings:

<figure><img src="../../.gitbook/assets/1.png" alt=""><figcaption><p>Camera Settings Navigation</p></figcaption></figure>

The plugin can be enabled/disabled per device on the Plugins tab:

<figure><img src="../../.gitbook/assets/NXPluginGreet.png" alt="" width="375"><figcaption><p>Nx AI Manager Plugin Tab</p></figcaption></figure>

Once the plugin is activated you can change the settings and choose a different model than the default.

&#x20;

<figure><img src="../../.gitbook/assets/plugin-popup-manage-device (1).png" alt="" width="375"><figcaption><p>The Nx Plugin Settings Tab with the Manage Device button</p></figcaption></figure>

To change a model, click the "Manage Device" button, which will open a Device Client popup with the Nx AI Manager open at the device details page where the model library can be used to select another model.

<figure><img src="../../.gitbook/assets/Screenshot From 2025-01-24 14-35-03.png" alt=""><figcaption><p>The Nx Client Popup where models can be managed for a device.</p></figcaption></figure>

For specific settings see the [next section about the configuration](model-settings.md).

#### Visualizing Bounding Boxes

If a model that outputs compatible bounding boxes is selected and running the Edge AI Manager, bounding boxes can be visualized by visiting the _Objects_ tab on the right pane in the Nx Meta Client:

<figure><img src="../../.gitbook/assets/image (120).png" alt=""><figcaption><p>Visible Bounding Boxes in Nx Meta Client</p></figcaption></figure>

#### Adding Event Rules

The Nx AI Manager plugin can generate several different types of events. Network Optix gives the user control over what these events should do, from sending an email to showing a notification. In this example, we will show a text overlay on the video.

Rules can be added by navigating to the Camera Rules menu:

<figure><img src="../../.gitbook/assets/image (52).png" alt="" width="563"><figcaption></figcaption></figure>

On the Event Rules window, click the **Add** button to add a new rule.&#x20;

From here, several options are available. First, on the left side, select **Analytics Event** from the **When** context menu. This is the type of event the Nx AI Manager plugin generates.&#x20;

Select any, or multiple, camera(s) in the **At** context menu.&#x20;

Under the **Event Type** context menu, you will find a number of event types the Nx AI Manager plugin can generate, from alarms to counting objects. In this example, we will select the _Objects Counted_ type.&#x20;

On the right side, it can be configured what should be done when one of these events is triggered. Here you could set up an email or notification trigger. In this example, we will select the Show text overlay option in the **Do** context menu **at** the source camera

<figure><img src="../../.gitbook/assets/image (51).png" alt=""><figcaption><p>Example Settings for Objects Counted Rule</p></figcaption></figure>

If set up correctly, and a model generating counts is selected and running, we should see an overlay on the camera feed showing us the object counts:

<figure><img src="../../.gitbook/assets/image (37).png" alt=""><figcaption><p>Example of Objects Counted text overlay</p></figcaption></figure>
