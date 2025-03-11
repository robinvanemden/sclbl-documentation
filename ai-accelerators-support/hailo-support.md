# Hailo Support

Deploying to Hailo chips requires the compilation of ONNX models to Hailo-ONNX format. And due to the nature and involvement in the compilation process, it's prohibitively complicated to automate this process on the cloud. Hence, we provide a workaround where the user compiles the model locally, then uploads the compiled Hailo-ONNX file to the Nx AI Cloud.

## Compiling an ONNX model

### Requirements

* Python 3.8
* Python environment
* **Hailo Dataflow compiler** and **HailoRT Python API** installed in that environment
* A set of calibration images (similar to images used to train the model)

### Example

In this example, we'll go over the compilation steps of a Yolov4-tiny model trained on the COCO dataset. Albeit, most of the instructions mentioned here apply to all kinds of ONNX models, with some requiring changes based on the model.

{% file src="../.gitbook/assets/object-detection-640x640.onnx" %}
A Yolov4-tiny model that's conforming to Nx's model requirements
{% endfile %}

To compile the model, you can run the Python script below after changing the ONNX path.

{% file src="../.gitbook/assets/compile_onnx (1).py" %}
Python script to compile an ONNX model to the Hailo format
{% endfile %}

The code performs the following tasks:

1. it transpiles the ONNX model to another format optimized for Hailo,
2. it quantizes and optimizes the model using the supplied set of calibration images,
3. it compiles the model to a HEF and embedds it inside an ONNX file as an operator, while the keeping the pre-processing and post-processing intact. \
   **Please note that this step returns an ONNX file that can have different input & output names and shapes.**
4. Finally, a new metadata field, named `chip` is injected in the ONNX to save which Hailo chip the model was optimized for. This needed by the Nx AI Cloud to determine the target chip of the model.

{% hint style="info" %}
The value of chip can be either `hailo` for Hailo-8 chips or `hailo-8l` for Hailo-8L chips.
{% endhint %}

After all the aforementioned steps are executed, a new ONNX file is generated. The latter needs to have his IOs metadata (names & shapes) adjusted. The Python script below is used for that purpose, it creates a new ONNX model with the adjusted inputs and outputs.\
The idea of the script is to make sure the generated ONNX is conforming to Nx's ONNX [requirements](../for-data-scientists/onnx-requirements.md).

{% file src="../.gitbook/assets/update_model_io.py" %}
Python script to adjust the ONNX input & ouptut metadata.
{% endfile %}

{% hint style="info" %}
To  adapt these two scripts for any other ONNX model, make sure to check out the TODO comments and adjust them accordingly.
{% endhint %}

## Deploying on a machine with Hailo-8 or Hailo-8L chips

1. The first step is to verify that you have a compatible HailoRT driver installed. Please check out this [table](supported-ai-accelerators.md) to determine if your driver version is supported.\
   For general Hailo driver install [see here](https://hailo.ai/developer-zone/software-downloads/) (you will need to register for the Hailo Dev Zone).\
   For the Raspberry Pi AI HAT+ [see here](https://www.raspberrypi.com/documentation/accessories/ai-hat-plus.html#ai-hat-plus) for install instructions. For the Raspberry pi AI Kit [see here](https://www.raspberrypi.com/documentation/accessories/ai-kit.html#ai-kit).
2. Next, install the Nx AI plugin by following [these instructions](../nx-ai-manager/2.-install-nx-ai-manager-plugin.md).
3. If all is well, you should be able to select the Hailo runtime when enabling the Nx plugin as shown below:

![](../.gitbook/assets/hailo-runtime-in-plugin-ui.png)

4. After the installation is finished, the plugin interface will look something like this:

![](../.gitbook/assets/plugin-ui.png)

5. To manually verify that the Hailo runtime is downloaded and set up, feel free to check out the content of the `bin` folder of the AI Manager and make sure it contains these files:\
   \- libhailort.so.4.xx.0 (xx is the minor version of the library)\
   \- libonnxruntime\_providers\_hailo.so\
   -libonnxruntime\_providers\_shared.so\
   \- libRuntimeLibrary.so

```sh
ubuntu@ThinkStation-P360-Tower:~$ ls /opt/networkoptix-metavms/mediaserver/bin/plugins/nxai_plugin/nxai_manager/bin/
installed_runtime.txt libhailort.so.4.17.0 libonnxruntime_providers_hailo.so libonnxruntime_providers_shared.so libRuntimeLibrary.so sclbld sclblmod
```

6. Finally, to deploy a model that can be accelerated on the Hailo chip, make sure that it has a `application/x-onnx; device=hailo` or `application/x-onnx; device=hailo-8l` based on the Hailo chip (Hailo-8 or Hailo-8L) model file in the Nx AI Cloud:

![](../.gitbook/assets/model-files-2.png)

If that is not the case, you'll need to manually compile the ONNX model and upload the generated model to the cloud as illustrated in the example above.

## Limitations

### Number of parallel models

The Nx AI Manager offers the ability to operate multiple AI models at the same time. This flexibility allows you to efficiently manage resources and optimize the performance of your AI applications. However, it's important to consider the limitations of the hardware you're using. Specifically, each Hailo chip, whether it's the Hailo-8 or the Hailo-8L, is capable of running only one model at a given time. Therefore, the number of models you can run concurrently on a single machine directly corresponds to the number of Hailo chips installed in that machine. Failing to account for this limitation may lead to the AI Manager's failure.

## Monitoring

**How to Enable Hailo Monitoring with `hailortcli monitor`**

To monitor Hailo usage with the `hailortcli monitor` command, you need to set a specific environment variable. Follow these steps:

1.  **Edit the Media Server Service Configuration:**\


    Add the following line to the `/etc/systemd/system/networkoptix-metavms-mediaserver.service` file to set the necessary environment variable:\


    ```plaintext
    Environment="HAILO_MONITOR=1"
    ```

    \
    The updated configuration file should look like this:\


    ```plaintext
    [Unit]
    Description=Network Optix Media Server
    After=network.target local-fs.target remote-fs.target
    Requires=networkoptix-metavms-root-tool.service

    [Service]
    PermissionsStartOnly=true
    ExecStartPre=/opt/networkoptix-metavms/mediaserver/lib/scripts/systemd_mediaserver_pre_start.sh
    ExecStart=/opt/networkoptix-metavms/mediaserver/lib/scripts/systemd_mediaserver_start.sh
    User=networkoptix-metavms
    Group=networkoptix-metavms
    Restart=always
    TimeoutStopSec=120
    KillMode=process
    TasksMax=8191
    LimitCORE=infinity
    Environment="HAILO_MONITOR=1"

    [Install]
    WantedBy=multi-user.target
    ```
2.  **Restart the NX Media Server:**\


    After updating the configuration file, restart the Network Optix Media Server for the changes to take effect. You can do this by running one of the following commands:\


    ```bash
    sudo systemctl restart networkoptix-metavms-mediaserver.service
    ```

    \
    or\


    ```bash
    sudo service networkoptix-metavms-mediaserver restart
    ```
3. **Run hailortcli**\
   &#x20;\
   `HAILO_MONITOR=1 hailortcli monitor`

<figure><img src="../.gitbook/assets/image (121).png" alt=""><figcaption></figcaption></figure>

## PCIe descriptor page size error

If you encounter the following error (actual page size may vary), it indicates that your host does not support the specified PCIe descriptor page size:

```
[HailoRT] [error] CHECK_AS_EXPECTED failed - max_desc_page_size given 16384 is bigger than hw max desc page size 4096
```

This issue is common on ARM64 devices like the Raspberry Pi AI Kit. To resolve it, add the following configuration to `/etc/modprobe.d/hailo_pci.conf`. If the file does not exist, create it and set the `max_desc_page_size` to the value mentioned in the error (e.g., 4096):

```bash
options hailo_pci force_desc_page_size=4096
```

You can add this configuration by running the following command:

```bash
echo 'options hailo_pci force_desc_page_size=4096' | sudo tee -a /etc/modprobe.d/hailo_pci.conf
```

Reboot the machine for the changes to take effect. Alternatively, you can reload the driver without rebooting by executing these commands:

```bash
sudo modprobe -r hailo_pci
sudo modprobe hailo_pci
```



## Experimental `.ini` setting <a href="#enable-.ini-settings" id="enable-.ini-settings"></a>

Explicitly setting multiple Nx AI runtime engines is controlled by an `.ini` file. This `.ini` file does not exist by default and must be created by the user.

Create an empty file by running:



```bash
sudo mkdir -p /home/networkoptix-metavms/.config/nx_ini 
sudo touch /home/networkoptix-metavms/.config/nx_ini/nxai_plugin.ini 
sudo chmod 666 /home/networkoptix-metavms/.config/nx_ini/nxai_plugin.ini
```

Then restart the mediaserver:

```
sudo service networkoptix-metavms-mediaserver restart
```

Once the mediaserver is restarted, the .ini file should be filled with defaults. Each setting should have a description in the .ini file.

Now, you can set multiple runtimes through:&#x20;

```
#enableOutput=false

# If enabled, the NxAI Plugin, NXAI Manager, and Inference Engine logs will be logged to the console. Default: false
#logToConsole=false

# If enabled, the NxAI Plugin will send frames to the AI Manager even when inactive. Default: false
#sendFramesOverride=false

# The path of the AI Manager's socket file is listening for messages. Default: "/tmp/nxai_manager.sock"
#AIManagerSocketPath="/tmp/nxai_manager.sock"

# The path of the socket file the plugin will listen for messages. Default: "/tmp/nxai_plugin.sock"
#PluginSocketPath="/tmp/nxai_plugin.sock"

# The URL of the NXAI cloud. Default: "https://api.sclbl.nxvms.com"
#CloudAPI="https://api.sclbl.nxvms.com"

# The AI Manager will spawn this many runtimes per model. Default: 1
runtimesPerModel=2


```
