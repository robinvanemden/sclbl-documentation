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

\*\*  **Additional Steps for Recent JetPack Installations**

For systems using NVIDIA's JetPack SDK, especially recent installations, the `networkoptix-metavms` user might not automatically be added to the `render` group. This group membership is essential for the Network Optix AI Manager plugin to fully utilize NVIDIA GPUs for hardware acceleration. While this process will be automated in a future Nx Server release, for now, you can manually add the user to the `render` group by following these steps:

#### 1. Check if the 'render' Group Exists

First, verify whether the `render` group exists on your system:

```bash
getent group render
```

*   **Expected Output**

    If the `render` group exists, you will see output similar to:

    ```
    render:x:104:username
    ```

    This indicates that the group exists and lists the users currently in the group.
*   **No Output**

    If there's **no output**, the `render` group does not exist on your system. In this case, there's no need to continue with the next steps. Y

#### 2. Add 'networkoptix-metavms' to the 'render' Group

**Open a Terminal Window**

* Access the terminal through the application menu or by pressing `Ctrl+Alt+T`.

**Execute the Usermod Command**

*   Run the following command to add the user to the `render` group:

    ```bash
    sudo usermod -aG render networkoptix-metavms
    ```

    **Explanation of the Command:**

    * `sudo` runs the command with administrative privileges.
    * `usermod` is used to modify user accounts.
    * `-aG` appends the user to the specified group(s) without removing them from others.
    * `render` is the group you're adding the user to.
    * `networkoptix-metavms` is the username for the Network Optix VMS user.

#### 3. Verify the Group Membership

Confirm that the `networkoptix-metavms` user has been added to the `render` group:

```bash
groups networkoptix-metavms
```

*   **Expected Output**

    The command will list all groups the user is a part of. You should see `render` included in the list.

#### 4. Restart the Network Optix Service

For the changes to take effect, restart the Network Optix media server service:

```bash
sudo systemctl restart networkoptix-mediaserver.service
```

* This command restarts the service, allowing it to recognize the updated group permissions.
