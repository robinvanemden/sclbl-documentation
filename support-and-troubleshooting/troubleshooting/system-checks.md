---
description: >-
  Things to check on the system if everything is running correctly, and how to
  check it.
---

# System checks

### Is Nx Meta version 6.0 or later installed <a href="#is-nx-meta-version-6.0-or-later-installed" id="is-nx-meta-version-6.0-or-later-installed"></a>

You need Nx Meta 6.0 or later for the Nx AI Manager plugin. Follow the instructions to see [1.-install-network-optix.md](../../nx-ai-manager/1.-install-network-optix.md "mention"). You need both the client and server programs, but the server can be installed on another machine than the client. Typically the **server** is a computer connected to some **cameras** over the network, and the **client** can be installed on your **local workstation** or **laptop**.

### Is the storage full <a href="#is-the-storage-full" id="is-the-storage-full"></a>

Can you store data or is the system low on resources. If the system has no space left the Nx AI Manager will not work correctly.

### Is the camera working <a href="#is-the-camera-working" id="is-the-camera-working"></a>

Do you see images in the camera preview window?If not, check the camera control app that came with the camera if that does show images.

* If the camera is not working there, you need to fix the camera input first before trying any next steps.
* If the camera is working but not visible in Nx Meta, please try to fix the camera display in Nx Meta first before trying any next steps.

### Are the necessary drivers installed <a href="#are-the-needed-drivers-installed" id="are-the-needed-drivers-installed"></a>

#### NVIDIA Orin accelerated <a href="#nvidia-orin-accelerated" id="nvidia-orin-accelerated"></a>

If you're running on NVIDIA Orin - is a current version of NVIDIA Jetpack installed?

#### Hailo Accelerated Devices <a href="#hailo-accelerated-devices" id="hailo-accelerated-devices"></a>

In order for the runtime using Hailo accelerators to work, the correct Hailo Runtime (**hailort)** needs to be installed. Currently, the Nx AI Runtime supports Hailo driver version **4.17.0**. Ensure that the correct runtime is installed.

### Is the system registered to a cloud user <a href="#is-the-system-registered-to-a-cloud-user" id="is-the-system-registered-to-a-cloud-user"></a>

If the plugin is detected and you are greeted with this message:

<figure><img src="https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F4Ho7de78I0gSMd4YY72l%2Fuploads%2Ff8RbtUAIVoB88Knm5UnH%2Fnocloud.png?alt=media&#x26;token=d281363e-7b9f-41d6-93a0-e229306c80ff" alt=""><figcaption></figcaption></figure>

It is most likely that your system is not connected to a cloud account. If you do not have an Nx Cloud account yet, follow the steps at [1.-install-network-optix.md](../../nx-ai-manager/1.-install-network-optix.md "mention") . The plugin requires a system to be connected to the cloud account to work.To add your system to your cloud account, right click on your system in the left-hand pane and select the Cloud tab:​​​

<figure><img src="https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F4Ho7de78I0gSMd4YY72l%2Fuploads%2F3C4k7HioYwwHZKNh3KUo%2Fcloud_management.png?alt=media&#x26;token=2c02991d-cb36-42c5-8b60-514b213be44a" alt=""><figcaption></figcaption></figure>
