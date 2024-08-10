# How to get support

To get support for the Nx AI Manager, check the following resources

The support pages and community forums

* [https://support.networkoptix.com/](https://support.networkoptix.com/)
* [https://support.networkoptix.com/hc/en-us/community/topics](https://support.networkoptix.com/hc/en-us/community/topics)

And check the steps in the troubleshooting section below.

## Contacting us

If your problem is not solved by the steps in the troubleshooting section you can contact us through the Network Optix support. Please make sure to prepare your question by collecting all relevant logs and system information beforehand.

Logs can be gathered by running the following command on the relevant machine:

```
tar -cf nxai_logs.tar \
-C /opt/networkoptix-metavms/mediaserver/bin/plugins/nxai_plugin \
nxai_plugin_start.log \
nxai_plugin.log \
-C /opt/networkoptix-metavms/mediaserver/bin/plugins/nxai_plugin/nxai_manager/etc \
sclblmod_start.log \
sclblmod_log.log \
sclbld_start.log \
sclbld_log.log
```

This will create a file called `nxai_logs.tar` in your current directory. Attaching this file to your support question will make it much easier for us to help you.
