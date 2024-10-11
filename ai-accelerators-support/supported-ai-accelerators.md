# Supported AI accelerators

The Nx AI Manager has integrated several runtimes allowing to benefit from hardware acceleration to run the deployed models.

The following table contains a compiled list of supported runtimes:

| AI Accelerator                                                          | CPU Architecture | API/driver version                    |
| ----------------------------------------------------------------------- | ---------------- | ------------------------------------- |
| CPU                                                                     | aarch64, x86\_64 | -                                     |
| Intel (OpenVINO)                                                        | x86\_64          | -                                     |
| Hailo-8                                                                 | x86\_64          | 4.17.0, 4.18.0, 4.19.0                |
| Hailo-8L                                                                | aarch64          | 4.18.0, 4.19.0                        |
| MemryX                                                                  | x86\_64          | 2.2.37                                |
| Nvidia [CUDA](https://developer.nvidia.com/cuda-toolkit-archive)        | x86\_64          | CUDA 11, CUDA 12                      |
| Nvidia [Jetpack](https://developer.nvidia.com/embedded/jetpack-archive) | aarch64          | Jetpack 4.6, Jetpack 5.x, Jetpack 6.x |
| Qualcomm (coming soon)                                                  | aarch64          | 2.20.x                                |
| MemryX (coming soon)                                                    | aarch64          | 2.2.37                                |

