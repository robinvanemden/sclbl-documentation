# Get started with the NX AI Manager plugin

{% hint style="info" %}
If you are getting error messages or not seeing any bounding boxes in your Nx Client, check out the [troubleshooting](../support-and-troubleshooting/troubleshooting/) or the [how to get support](../support-and-troubleshooting/how-to-get-support.md) page.
{% endhint %}

## Requirements

{% hint style="info" %}
**Minimum Hardware Requirements**

* **x86\_64 Systems**: Intel i5 (10th Gen quad-core equivalent) or higher, with at least 4 GB of RAM\
  &#xNAN;_&#x4E;ote: The processor must support AVX2 instructions. Check_ [_here_](https://avx2checker.com/processors) _if you are in doubt._
* **ARM Systems**: Raspberry Pi 4B equivalent or higher (AARCH64), with at least 4 GB of RAM



**OS Requirements**\
&#xNAN;_&#x55;buntu Linux LTS version 20.04 or higher_\
\
**Software Requirements**\
_Nx Meta Client 6.0+                                      \[X86\_64, Arm32, Arm64]_\
_Nx Meta Server 6.0+                                      \[X86\_64, Arm32, Arm64]_
{% endhint %}

## Performance recommendations

{% hint style="info" %}
**Note:** The recommendations below are based on the assumption that the computer being used is dedicated to the Nx Meta Server application with the default settings and one Nx AI Plugin and is not used to run additional applications concurrently as this may impact the performance and stability of your System.
{% endhint %}

For example, a system with one camera, no saved layouts, few rules, and a single user on the minimal required hardware will work just fine. A System with multiple models, many cameras per server, dozens or hundreds of layouts, numerous rules, and hundreds of concurrently connected users would require much more substantial hardware.

### AI input resolution and secondary stream recommendation

Enabling the plugin for a camera secondary stream with a resolution of 512x512 or slightly higher, e.g. 720p, and a minimum frame rate of 6 frames per second (FPS) is recommended. Please refer to your camera's documentation to configure the camera's secondary stream accordingly.

While enabling the Nx AI Manager plugin for a camera primary stream is possible, that is not recommended. Running the plugin on a primary stream will require the Nx server to decode the high-resolution stream and scale it down. This primary stream decoding and scaling imposes a high load on the CPU and will significantly increase memory consumption. Running AI plugins on the primary stream will not improve the accuracy of the AI detections and will reduce the number of AI detections per second on your Nx server.

### AI detections per second

For accurate AI detection in security or surveillance use cases, a minimum of 6 detections per second is typically sufficient. By default, the Nx AI Manager plugin will perform as many detections per second as possible. The number of detections per second is limited by the number of frames per second in the video stream and the AI processing power of the device it runs on.

On an Intel i5 12th gen device with 8GB of memory, using 720p resolution secondary camera streams, the following performance can be expected:

Single 720p RTSP H264 secondary stream at 24 fps stream performance with Detection plugin:

* Up to 23.2 FPS for the large people detection model.

Four 720p RTSP H264 secondary streams at 24 fps stream performance with Detection plugin:

* Up to 9.0 FPS per stream for the large people detection model

These numbers can serve as a reference point for estimating the system's performance, but remember that the actual performance may vary based on specific configurations, hardware variations, and other factors.

### Hardware recommendations

When AI is enabled on one or multiple cameras of an Nx server, that server's CPU/GPU load and memory consumption will increase. This is because the Nx server needs to decode the camera streams for which AI is enabled, and the Nx AI Manager plugin requires resources to perform the AI inference.&#x20;

The following recommendations assume that the device is dedicated to Nx with Nx AI Manager plugin with default settings and that the AI plugin is enabled on 720p secondary camera streams.

#### Memory requirement

It is recommended to add 512 MB in RAM capacity per stream for which the AI plugin is enabled

#### CPU/GPU requirement

Up to 6 cameras with AI detection: Intel i5 10th gen or AMD Ryzen 5 3000 Quad-Core.

Up to 12 cameras with AI detection: Intel i7 12th gen or AMD Ryzen 7 3000 Quad-Core.

#### Other hardware

For other hardware architectures such as ARM, Nvidia Jetson Orin, Hailo, etc, please contact info@networkoptix.com

## Get started with Network Optix and the Nx AI Manager plugin

To get started with Nx and the Nx AI Manager plugin, follow the steps outlined below:

{% content-ref url="https://app.gitbook.com/s/tAnveGJ71G8niBIFFZ2k/nx-ai-manager/1.-install-network-optix" %}
[1. Install Network Optix](https://app.gitbook.com/s/tAnveGJ71G8niBIFFZ2k/nx-ai-manager/1.-install-network-optix)
{% endcontent-ref %}

{% content-ref url="https://app.gitbook.com/s/tAnveGJ71G8niBIFFZ2k/nx-ai-manager/2.-install-nx-ai-plugin" %}
[2. Install NX AI Plugin](https://app.gitbook.com/s/tAnveGJ71G8niBIFFZ2k/nx-ai-manager/2.-install-nx-ai-plugin)
{% endcontent-ref %}

{% content-ref url="https://app.gitbook.com/s/tAnveGJ71G8niBIFFZ2k/nx-ai-manager/2.-configure-the-nx-ai-manager-plugin" %}
[3. Configure the Nx AI Manager plugin](https://app.gitbook.com/s/tAnveGJ71G8niBIFFZ2k/nx-ai-manager/2.-configure-the-nx-ai-manager-plugin)
{% endcontent-ref %}

{% content-ref url="https://app.gitbook.com/s/tAnveGJ71G8niBIFFZ2k/nx-ai-manager/3.-other-network-optix-plugin-settings" %}
[4. Other Network Optix Plugin Settings](https://app.gitbook.com/s/tAnveGJ71G8niBIFFZ2k/nx-ai-manager/3.-other-network-optix-plugin-settings)
{% endcontent-ref %}

{% content-ref url="https://app.gitbook.com/s/tAnveGJ71G8niBIFFZ2k/nx-ai-manager/4.-manual-plugin-installation" %}
[5. Manual Plugin Installation](https://app.gitbook.com/s/tAnveGJ71G8niBIFFZ2k/nx-ai-manager/4.-manual-plugin-installation)
{% endcontent-ref %}

{% content-ref url="https://app.gitbook.com/s/tAnveGJ71G8niBIFFZ2k/nx-ai-manager/7.-advanced-configuration" %}
[7. Advanced configuration](https://app.gitbook.com/s/tAnveGJ71G8niBIFFZ2k/nx-ai-manager/7.-advanced-configuration)
{% endcontent-ref %}

And because it's sometimes necessary:

{% content-ref url="https://app.gitbook.com/s/tAnveGJ71G8niBIFFZ2k/support-and-troubleshooting/troubleshooting" %}
[Troubleshooting](https://app.gitbook.com/s/tAnveGJ71G8niBIFFZ2k/support-and-troubleshooting/troubleshooting)
{% endcontent-ref %}

