---
description: Things you can try to narrow down where the problem might be.
---

# Things to try

### Have you tried turning it off and on again <a href="#have-you-tried-turning-it-off-and-on-again" id="have-you-tried-turning-it-off-and-on-again"></a>

Always try to restart the system to see if it fixes the problem.&#x20;

Also check all cables (by unplugging them and plugging them back in)

#### Restart the Nx Meta Mediaserver <a href="#restart-the-nx-meta-mediaserver" id="restart-the-nx-meta-mediaserver"></a>

For the plugin to be detected after install, make sure to restart the Nx Meta mediaserver. This can be done through the Nx Meta mediaserver web interface.Navigate to "\<Server IP Address>:7001" in your web browser. Go to the **Servers** tab, and click the restart button.

### Reinstall the plugin <a href="#reinstall-the-plugin" id="reinstall-the-plugin"></a>

Firstly completely remove the existing version of the plugin by following [the uninstall instructions](https://app.gitbook.com/o/bcLqIPiXVKcQXjqrnQSu/s/4Ho7de78I0gSMd4YY72l/nx-ai-manager/removing-the-nx-ai-manager).And then follow the [install instructions](https://app.gitbook.com/o/bcLqIPiXVKcQXjqrnQSu/s/4Ho7de78I0gSMd4YY72l/nx-ai-manager/install-nx-ai-manager-plugin) for a clean installation the plugin.

### Try another version <a href="#try-another-version" id="try-another-version"></a>

There might be a newer version of Nx Meta or Nx EVOS available. The new version might have improved functionality. Download the [new version](https://meta.nxvms.com/download/releases) and install it to see if your problems are solved.Check if the latest beta fixes your problem, or if it worked in a previous release.

* Nx AI Manager plugin - see the [install instructions](https://app.gitbook.com/o/bcLqIPiXVKcQXjqrnQSu/s/4Ho7de78I0gSMd4YY72l/nx-ai-manager/install-nx-ai-manager-plugin).
* Nx Meta Mediaserver - check if there is a [newer version or a beta](https://meta.nxvms.com/download/releases) available.
* Nx Meta client - check if there is a [newer version or a beta](https://meta.nxvms.com/download/releases) available.

### Try another model <a href="#try-another-model" id="try-another-model"></a>

See if you can install another model and see if it gives correct resultsVerify that the model is [downloaded](https://app.gitbook.com/o/bcLqIPiXVKcQXjqrnQSu/s/4Ho7de78I0gSMd4YY72l/~/changes/836/support-and-troubleshooting/troubleshooting/plugin-checks#is-the-model-downloaded) and running.

### Try another camera <a href="#try-another-camera" id="try-another-camera"></a>

Check if the model works on another camera. If no other camera is available, you can point the camera at a different scene.

### Try to reset an unresponsive USB camera

When you are using a USB webcam on ubuntu or another linux, those cameras can get lost in sleep mode and become unresponsive.

You can unplug it and reconnect it to get the camera back, but that's kind of hard to do when you're remote.

To remotely reset a USB camera you can login to the console of the machine where the camera is connected and use the command `usbreset` to get a list of the USB devices. Resetting a specific device can then be done with `usbreset 001/001` for example to reset a device that is located on that bus number.

### Try a test camera stream <a href="#try-a-test-camera-stream" id="try-a-test-camera-stream"></a>

If no camera change is possible, try a video feed instead of a live camera. You can then try a [test camera](https://support.networkoptix.com/hc/en-us/articles/360018067074-Testcamera-IP-Camera-Emulator) with a video which is especially suited for your model.

### Try another computer <a href="#try-another-computer" id="try-another-computer"></a>

If you have another computer available, install the Nx Meta Mediaserver or Nx EVOS and check if it works on that system.The Nx AI Manager in Nx Meta and Nx EVOS can run on systems like the Raspberry Pi or the NVIDIA Orin Nano and on many standard PCs and laptops.
