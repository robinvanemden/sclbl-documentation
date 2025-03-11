# OpenVino Support

To use OpenVino runtimes, you have the option select it on plugin install for compatible hardware.\
\
If you want to preselect GPU or NPU runtimes, make sure you have the very latest Intel drivers and  libtbb installed on your machine.\
\
For the Intel drivers, follow:\
\
\-  For GPU: [https://github.com/intel/compute-runtime/releases](https://github.com/intel/compute-runtime/releases) \
\-  For NPU: [https://github.com/intel/linux-npu-driver/releases](https://github.com/intel/linux-npu-driver/releases)

Also make sure you have the latest libtbb installed:

```
sudo apt update sudo apt install libtbb12
```

Add the user to video and gender groups:

```
sudo usermod -aG video $USER

sudo usermod -aG render $USER
```

\
\
Then,  add `Environment="DEVICE_TYPE=GPU" vs Environment="DEVICE_TYPE=NPU"` to `/etc/systemd/system/networkoptix-metavms-mediaserver.service` under `[Service]:`

```
# Network Optix Media Server

[Unit]
Description=Network Optix Media Server
After=network.target local-fs.target remote-fs.target
Requires=networkoptix-metavms-root-tool.service

[Service]
Environment="DEVICE_TYPE=GPU"
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

[Install]
WantedBy=multi-user.target




```
