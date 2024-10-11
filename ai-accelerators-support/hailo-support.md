# Hailo Support

Deploying to Hailo chips requires the compilation of ONNX models to Hailo-ONNX format. Due to the nature and involvement in the compilation process, it's prohibitively complicated to automate this process on the cloud. Hence, we provide a workaround where the user compiles the model locally, then upload the compiled Hailo-ONNX file to the Nx AI Cloud.

### Compiling an ONNX model

#### Requirements

* Python 3.8
* Python environment
* **Hailo Dataflow compiler** and **HailoRT Python API** installed in that environment
* A validation dataset

#### Example

In this example, we'll go over the compilation steps of a Yolov4-tiny model trained on the COCO dataset. Albeit, most of the instructions mentioned here apply to all kinds of ONNX models, with some requiring changes based on the model.

{% file src="../.gitbook/assets/object-detection-640x640.onnx" %}
A Yolov4-tiny model that's conforming to Nx's model requirements
{% endfile %}

To compile the model, you can run the Python script below after changing the ONNX path.

{% hint style="info" %}
To  adap this script for any other ONNX model, make sure to check out the TODO comments and adjust them accordingly.
{% endhint %}

{% file src="../.gitbook/assets/compile_onnx.py" %}

{% file src="../.gitbook/assets/update_model_io.py" %}

{% file src="broken-reference" %}
A Python script to compile ONNX files.
{% endfile %}

{% file src="broken-reference" %}
A Python script to correct the ONNX IO names and shapes to match the originals.
{% endfile %}

### Deploying on x86\_64 machine with Hailo-8

1. The first step is to verify that you have a compatible HailoRT driver installed. Please check out this [table](supported-ai-accelerators.md) to determine if your driver version is supported.
2. Next, install the Nx AI plugin by following [these instructions](../nx-ai-manager/2.-install-nx-ai-plugin.md).
3. If all is well, you should be able to select the Hailo runtime when enabling the Nx plugin as shown below:

![](../.gitbook/assets/hailo-runtime-in-plugin-ui.png)

4. After the installation is finished, the plugin interface will look something like this:

![](../.gitbook/assets/plugin-ui.png)

5. To manually verify that the Hailo runtime is downloaded and set up, feel free to check out the content of the `bin` folder of the AI Manager and make sure it contains these files:\
   \- libhailort.so.4.xx.0\
   \- libonnxruntime\_providers\_hailo.so\
   \-libonnxruntime\_providers\_shared.so\
   \- libRuntimeLibrary.so

```sh
ubuntu@ThinkStation-P360-Tower:~$ ls /opt/networkoptix-metavms/mediaserver/bin/plugins/nxai_plugin/nxai_manager/bin/
installed_runtime.txt libhailort.so.4.17.0 libonnxruntime_providers_hailo.so libonnxruntime_providers_shared.so libRuntimeLibrary.so sclbld sclblmod
```

6. Finally, to deploy a model that can be accelerated on the Hailo chip, make sure that it has a `application/x-onnx; device=hailo` model file in the Nx AI Cloud:

![](../.gitbook/assets/model-files-2.png)

If that is not the case, you'll need to manually compile the ONNX model and upload the generated model to the cloud. Please refer to [this](https://github.com/OAAX-standard/contributions/tree/main/Hailo-8) page for a quick start guide.

### Common issues

* Sometimes, after compiling an ONNX model to a Hailo-ONNX, the input names and shapes are _not_ kept intact. Hence, the model might not work correctly within the Nx AI Manager. \
  So, please make sure that the generated ONNX conforms to our specifications.

### Monitoring

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

<figure><img src="../.gitbook/assets/image (119).png" alt=""><figcaption></figcaption></figure>

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
