# Nvidia Support

The ONNX-Cuda runtime is available on both x86\_64 machines (for eg. machines with Nvidia RTX 4090, A100, etc.) and AARCH64 machine (for eg. Jetson Orin AGX, Jetson Xavier NX, etc.).

## Operating conditions

For the AI Manager to work on the machine with Nvidia GPUs, the machine needs to have CUDA properly installed, in which case these conditions needs to be met:

### X86\_64

1. This file `/proc/driver/nvidia/version` needs to be available.
2.  This file `/usr/local/cuda/version.json` needs to be available and contain the install CUDA version. An example of the file should like this:

    ```cpp
    {
       "cuda" : {
          "name" : "CUDA SDK",
          "version" : "12.2.20230823"
       },
       ...
    }
    ```
3. The `nvidia-smi` command should be installed and has to be compatible with the installed Nvidia drivers.

### AARCH64

*   A compatible JetPack version needs to be installed. You can verify that by running this command:

    ```cpp
    dpkg-query --showformat='${Version}' --show nvidia-l4t-core
    ```

The command returns the version of the installed NVIDIA JetPack SDK.

## Installing the runtime manually

{% hint style="info" %}
Before trying to  install the runtime, make sure that the Nvidia GPU and CUDA version are supported by reviewing [this table](supported-ai-accelerators.md), and that they correctly installed by checking the conditions above.
{% endhint %}

First setup to setup the runtime manually is to download the correct runtime library for the relevant machine using one of the links below:

### X86\_64

* [CUDA 11](https://artifactory.nxvms.dev/artifactory/nxai\_open/OAAX/runtimes/v4-1/nvidia-cuda\_11-x86\_64-ort.tar.gz)
* [CUDA 12](https://artifactory.nxvms.dev/artifactory/nxai\_open/OAAX/runtimes/v4-1/nvidia-cuda\_12-x86\_64-ort.tar.gz)

## AARCH64

* [Jetpack 4.6](https://artifactory.nxvms.dev/artifactory/nxai\_open/OAAX/runtimes/v4-1/nvidia-cuda\_10-aarch64-ort.tar.gz)
* [Jetpack 5.x](https://artifactory.nxvms.dev/artifactory/nxai\_open/OAAX/runtimes/v4-1/nvidia-cuda\_11-aarch64-ort.tar.gz)
* [Jetpack 6.0 ](https://artifactory.nxvms.dev/artifactory/nxai\_open/OAAX/runtimes/v4-1/nvidia-cuda\_12-aarch64-ort.tar.gz)

When the download is complete, unpack the archive in this directory using this command:

```bash
tar -xf <archive-path> -C /opt/networkoptix-metavms/mediaserver/bin/plugins/nxai_plugin/nxai_manager/bin
```

then, create a file named `installed_runtime.txt` in the same directory and set its content as `ONNX-CUDA` using this command:

```bash
echo "ONNX-CUDA" > /opt/networkoptix-metavms/mediaserver/bin/plugins/nxai_plugin/nxai_manager/bin/installed_runtime.txt
```

After that, for changes to take effect, restart the Nx server using this command:

```bash
sudo systemctl restart networkoptix-metavms-mediaserver.service
```
