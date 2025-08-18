# How to get support

To get support for the Nx AI Manager, check the following resources

The support pages and community forums

* [https://support.networkoptix.com/](https://support.networkoptix.com/)
* [https://support.networkoptix.com/hc/en-us/community/topics](https://support.networkoptix.com/hc/en-us/community/topics)

And check the steps in the troubleshooting section below.

## Contacting us

If your problem is not solved by the steps in the troubleshooting section you can contact us through the Network Optix support. Please make sure to prepare your question by collecting all relevant logs and system information beforehand.

Logs can be gathered by running the following shell script on the relevant machine:

<details>

<summary>Shell script to gather logs and system information</summary>

```bash
#!/bin/bash

# This script is used to gather information about the HW and SW of the system, in addition to information about the Nx AI Manager.
# The information is stored in a directory located in ~/nxai_troubleshooting and then compressed into a file named ~/nxai_troubleshooting.tgz.
# To get support, please attach the compressed file to your support request.
# NOTE: No sensitive information is collected, only the basic system information and the Nx AI Manager information.
# Enable debug mode
# set -x

# Create directory where the information will be stored
current_dir=$(pwd)
info_dir=~/nxai_troubleshooting
rm -rf $info_dir >/dev/null 2>&1
rm -rf $info_dir.tgz >/dev/null 2>&1
mkdir -p $info_dir

# Redirect all output and error streams to a log file
log_file="$info_dir/nxai_troubleshooting.log"
exec > >(tee -a "$log_file") 2>&1

############################### Basic System Information
lsb_release -a >$info_dir/lsb_release.txt
uname -a >$info_dir/uname.txt
lscpu >$info_dir/lscpu.txt
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
    echo "Mediaserver is not installed."
fi
# get Mediaserver installed version
cat $plugins_dir/../../build_info.txt >$info_dir/mediaserver_info.txt

############################### Check if AI Plugin is installed
if [ -f $plugins_dir/nxai_plugin/libnxai_plugin.so ]; then
    echo "AI Plugin is installed."
else
    echo "AI Plugin is not installed."
fi
libnxai_plugin_dir=$plugins_dir/nxai_plugin/
# Check if tree is installed
if command -v tree >/dev/null 2>&1; then
    echo "Using tree to list files in the AI Plugin directory"
    tree -h --du "$libnxai_plugin_dir/" >"$info_dir/nxai_plugin_tree.txt"
else
    echo "Using du to list file sizes in the AI Plugin directory"
    du -ah "$libnxai_plugin_dir/" >"$info_dir/nxai_plugin_du.txt"
fi

# Gather all log files in the AI Plugin directory
find $libnxai_plugin_dir -name "*.log" -exec cp {} $info_dir/ \;
find $libnxai_plugin_dir -name "*.log.*" -exec cp {} $info_dir/ \;

############################### Check if AI Manager is installed
if [ -d $libnxai_plugin_dir/nxai_manager/bin ]; then
    echo "AI Manager is installed."
else
    echo "AI Manager is not installed."
fi
nxai_manager_dir=$libnxai_plugin_dir/nxai_manager/
bin_dir=$nxai_manager_dir/bin/

############################### Check AI Manager configuration
if [ -f $bin_dir/installed_runtime.txt ]; then
    echo "Runtime might be installed."
else
    echo "Runtime not installed."
fi
# Get the installed runtime information
cp $bin_dir/installed_runtime.txt $info_dir/installed_runtime.txt
# Get the settings file
cp $bin_dir/../etc/settings.json $info_dir/settings.json

############################### Check if AI Manager is running
# get running processes
ps aux | grep nxai >>$info_dir/nxai_manager_ps_aux.txt

############################### Check connectivity to the Nx AI Cloud
# Check if curl or wget is available
if command -v curl >/dev/null 2>&1; then
    echo "Using curl"
    # check if Nx AI Cloud is reachable
    curl -s https://api.sclbl.nxvms.com/dev/ >$info_dir/nxai_cloud_connectivity.txt
    # Download a file from the Nx AI Cloud to measure the download speed
    echo "Downloading a test file from the Nx AI Cloud to measure download speed..."
    curl -s -m 10 "https://cdn.sclbl.nxvms.com/benchmark.bin?size=10" -o /dev/null -w "%{speed_download}" |
        awk '{print "Model download speed: " $1/1048576 " MB/sec"}' \
            >$info_dir/nxai_cloud_download_speed_1.txt
    curl -s -m 10 "https://artifactory.nxvms.dev/artifactory/nxai_open/files/23MB.bin" -o /dev/null -w "%{speed_download}" |
        awk '{print "Runtime download speed: " $1/1048576 " MB/sec"}' \
            >$info_dir/nxai_cloud_download_speed_2.txt
elif command -v wget >/dev/null 2>&1; then
    echo "Using wget"
    wget -q -O "$info_dir/nxai_cloud_connectivity.txt" https://api.sclbl.nxvms.com/dev/
    wget --timeout=10 "https://artifactory.nxvms.dev/artifactory/nxai_open/files/23MB.bin" -O /dev/null >$info_dir/nxai_cloud_download_speed_1.txt 2>&1
    wget --timeout=10 "https://cdn.sclbl.nxvms.com/benchmark.bin?size=10" -O /dev/null >$info_dir/nxai_cloud_download_speed_2.txt 2>&1
else
    echo "ERROR: Neither curl nor wget is installed."
fi
# Get the latency to the Nx AI Cloud
ping -c 10 api.sclbl.nxvms.com >$info_dir/nxai_cloud_ping.txt

# Get information about DEEPX if available
# Checking if dxrt-cli is installed
if command -v dxrt-cli >/dev/null 2>&1; then
    echo "dxrt-cli is installed."
    dxrt-cli -s >$info_dir/dxrt_cli_version.txt 2>&1
else
    echo "dxrt-cli is not installed."
fi

############################### tar compress the information
cd $info_dir/..
tar -cvf $info_dir.tgz "$(basename $info_dir)" >/dev/null || echo "ERROR: Failed to compress the information."
rm -rf $info_dir >/dev/null 2>&1

echo "System information gathering complete."
echo "The collected information is stored in $info_dir.tgz"
echo "Please attach this archive to your support request, and optionally delete it from the disk."
cd "$current_dir"

```

</details>

This will create a file called `nxai_troubleshooting.tgz` in the home directory. Attaching this file to your support question will make it much easier for us to help you.
