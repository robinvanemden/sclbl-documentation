# Supported AI accelerators

The Nx AI Manager has integrated several runtimes allowing to benefit from hardware acceleration to run the deployed models.

The following table contains a compiled list of supported runtimes:

| AI Accelerator                                                          | CPU Architecture | API/driver version                         |
| ----------------------------------------------------------------------- | ---------------- | ------------------------------------------ |
| CPU                                                                     | aarch64, x86\_64 | -                                          |
| Intel (OpenVINO)                                                        | x86\_64          | -                                          |
| Hailo-8                                                                 | x86\_64          | 4.17.0, 4.18.0, 4.19.0                     |
| Hailo-8L                                                                | aarch64          | 4.18.0, 4.19.0                             |
| MemryX                                                                  | x86\_64          | 2.2.37                                     |
| Nvidia [CUDA](https://developer.nvidia.com/cuda-toolkit-archive)        | x86\_64          | CUDA 11, CUDA 12                           |
| Nvidia [Jetpack](https://developer.nvidia.com/embedded/jetpack-archive) | aarch64          | Jetpack 4.6, Jetpack 5.x, Jetpack 6.x \*\* |
| Qualcomm (coming soon)                                                  | aarch64          | 2.20.x                                     |
| MemryX (coming soon)                                                    | aarch64          | 2.2.37                                     |

\*\* Recent Jetpack installs need an additional command to add `networkoptix-metavms` to the  `render` group. This will be automated in a future Nx Server release.

You should add the user to the group to ensure that the VMS can fully utilize the NVIDIA GPU. Here's how you can do it:

1.  **Open a Terminal Window**

    You can generally access the terminal through the application menu or by pressing `Ctrl+Alt+T`.
2.  **Execute the Usermod Command**

    Run the following command to add the user to the `render` group:

    ```bash
    sudo usermod -aG render networkoptix-metavms
    ```

    * `sudo` runs the command with administrative privileges.
    * `usermod` is the command used to modify user accounts.
    * `-aG` appends the user to the specified group(s).
    * `render` is the group you are adding the user to.
    * `networkoptix-metavms` is the username.
3.  **Verify the Group Membership**

    You can verify that the user has been added to the `render` group by running:

    ```bash
    groups networkoptix-metavms
    ```

    This command will list all the groups the user is a part of, which should now include `render`.
4.  **Restart Service**

    For the changes to take effect, you need to restart the Network Optix services:

    ```bash
    sudo systemctl restart networkoptix-mediaserver.service
    ```
