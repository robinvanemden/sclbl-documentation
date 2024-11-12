# How to get support

To get support for the Nx AI Manager, check the following resources

The support pages and community forums

* [https://support.networkoptix.com/](https://support.networkoptix.com/)
* [https://support.networkoptix.com/hc/en-us/community/topics](https://support.networkoptix.com/hc/en-us/community/topics)

And check the steps in the troubleshooting section below.

## Contacting us

If your problem is not solved by the steps in the troubleshooting section you can contact us through the Network Optix support. Please make sure to prepare your question by collecting all relevant logs and system information beforehand.

Logs can be gathered by running the following shell script on the relevant machine:

{% hint style="info" %}
Please make sure you have the `zip` command installed on the machine as it's used to assemble the collect logs and information in a single archive file
{% endhint %}

<details>

<summary>Shell script to gather logs and system information</summary>

```bash
#!/bin/bash

# This script is used to gather information about the HW and SW of the system, in addition to information about the AI Manager and the AI Plugin.
# The information is stored in a directory located in ~/nxai_info and then zipped into a file named ~/nxai_info.zip.

# Enable debug mode
# set -x

# Create directory where the information will be stored
info_dir=~/nxai_info
rm -rf $info_dir >/dev/null 2>&1
rm -rf $info_dir.zip >/dev/null 2>&1
mkdir -p $info_dir

############################### Basic System Information
lsb_release -a >$info_dir/lsb_release.txt
uname -a >$info_dir/uname.txt
lscpu >$info_dir/lscpu.txt
lshw >$info_dir/lshw.txt
lspci >$info_dir/lspci.txt
df -h >$info_dir/df.txt
ldd --version >$info_dir/ldd_version.txt

############################### Check if the mediaserver is installed
plugins_dir=""
if [ -d /opt/networkoptix-metavms/mediaserver/bin/plugins/ ]; then
    plugins_dir="/opt/networkoptix-metavms/mediaserver/bin/plugins/"
elif [ -d /opt/networkoptix/mediaserver/bin/plugins/ ]; then
    plugins_dir="/opt/networkoptix/mediaserver/bin/plugins/"
else
    echo "MediaServer is not installed."
    exit 1
fi
# get MediaServer installed version
cat $plugins_dir/../../build_info.txt >$info_dir/mediaserver_info.txt

############################### Check if AI Plugin is installed
if [ -f $plugins_dir/nxai_plugin/libnxai_plugin.so ]; then
    echo "AI Plugin is installed."
else
    echo "AI Plugin is not installed."
    exit 2
fi
libnxai_plugin_dir=$plugins_dir/nxai_plugin/
# Get list of files in the AI Plugin directory
tree -h --du $libnxai_plugin_dir/ >$info_dir/nxai_plugin_tree.txt
# Gather all log files in the AI Plugin directory
find $libnxai_plugin_dir -name "*.log" -exec cp {} $info_dir/ \;
find $libnxai_plugin_dir -name "*.log.*" -exec cp {} $info_dir/ \;

############################### Check if AI Manager is installed
if [ -d $libnxai_plugin_dir/nxai_manager/bin ]; then
    echo "AI Manager is installed."
else
    echo "AI Manager is not installed."
    exit 3
fi
nxai_manager_dir=$libnxai_plugin_dir/nxai_manager/
bin_dir=$nxai_manager_dir/bin/

############################### Check AI Manager configuration
if [ -f $bin_dir/installed_runtime.txt ]; then
    echo "Runtime might be installed."
else
    echo "Runtime not installed."
    exit 4
fi
# Get the installed runtime information
cp $bin_dir/installed_runtime.txt $info_dir/installed_runtime.txt
# Get the settings file
cp $bin_dir/../etc/settings.json $info_dir/settings.json

############################### Check if AI Manager is running
# get running processes
ps aux | grep sclbl >$info_dir/nxai_manager_ps_aux.txt
# start the ai manager manually and stop it after 5 seconds
echo "Running AI Manager for 5 seconds..."
cd $bin_dir
timeout 5s ./sclblmod >$info_dir/ai_manager_run.txt 2>&1
# Use the following line if the ai manager doesn't exit after 5 seconds
# timeout --signal=SIGKILL 5s ./sclblmod >$info_dir/ai_manager_run.txt 2>&1

############################### Check connectivity to the Nx AI Cloud
curl -s https://api.sclbl.nxvms.com/dev/ >$info_dir/nxai_cloud_connectivity.txt

############################### Zip the information
zip -r $info_dir.zip $info_dir/* >/dev/null || echo "ERROR: Failed to zip the information."

echo "System information gathering complete."
echo "The collected information is stored in $info_dir.zip"
```

</details>

This will create a file called `nxai_info.zip` in the home directory. Attaching this file to your support question will make it much easier for us to help you.
