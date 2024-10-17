# NX AI Certification Test

## Certification Test

### Quickstart

The NX AI Certification test should be able to run on any Ubuntu installation which is also compatible with Network Optix Server.&#x20;

Ensure your device has at least a few gigabytes of free space, a working internet connection and a working Python 3 and Pip installation. Execute the following commands:

```bash
## Create and enter folder for test
mkdir nxai_test
cd nxai_test

## Download testing suite
wget https://artifactory.nxvms.dev/artifactory/nxai_open/NXAITest/nxai_test.tgz

## Unpack testing suite
tar -xvf nxai_test.tgz

## Install all required Python packages
pip3 install -r requirements.txt

## Install NX AI Manager
./Utilities/install_nxai_manager.sh
#./Utilities/install_nxai_manager.sh cuda
#./Utilities/install_nxai_manager.sh hailo4.17
#./Utilities/install_nxai_manager.sh hailo4.18
#./Utilities/install_nxai_manager.sh hailo4.19

## Download required models
python3 Utilities/download_models.py

## Start test
python3 all_suites.py

## Gather info
python3 Utilities/gather_hwinfo.py

## Upload results to cloud
python3 Utilities/upload_results.py
```

The test will run for a couple of hours and will stress the device. Do not power off your device.

### Introduction

The Nx AI Certification Test is meant to test any device to ensure it is compatible and stable enough to run the Nx AI Manager for extended periods of time.&#x20;

The test will attempt to run multiple common model architectures, with different sizes, and even multiples of those models to test compatibility and what can be expected to run on the device. The test will also run long operation tests to check if there are any memory issues or degradation in performance due to overheating or other reasons.

Finally, the test will gather all results in a folder which can be used to generate a report, either on the device or somewhere else. The report should contain enough information to determine if the device is indeed compatible.

### Installing NxAI Manager

A useful script is provided to install the NX AI Manager runtime locally within the test environment. This will ensure that this testing does not interfere with any existing installations on the device.&#x20;

The script also allows for installing different acceleration libraries by giving command line arguments. For CPU acceleration:

```
./Utilities/install_nxai_manager.sh
```

For Nvidia Cuda acceleration:

```
./Utilities/install_nxai_manager.sh cuda
```

For Hailo acceleration:

```
./Utilities/install_nxai_manager.sh hailo
```

It is also possible to install multiple runtimes and have the NxAI Certification test performed on all installed runtimes. This can be done by running the installation script for each runtime you would like to test.

### Running test

The NxAI Certification test includes a collection of tests to test different aspects of your device to ensure that the NxAI Toolkit can run on your device. To run all of these tests in one large test, run:

```
python3 all_suites.py
```

This could take many hours to complete.

### Uploading Results

An endpoint was created where you can upload and view the test results of your device. After the test has completed, run the following to automatically upload the script to the cloud:

```
python3 Utilities/upload_results.py
```

### Generating Report

A script is provided which can be used to generate a report. To generate the report, additional dependencies must be installed. These can be installed with:

```sh
pip3 install -r requirements_report.txt
```

Finally the report can be generated with:

```bash
python3 Utilities/generate_report.py
```

This will create a "Report" folder containing a file called 'report.md', which is the generated report in Markdown format.

If the dependencies cannot be installed on the target device or there are space limitations, the "Results" folder can be distributed to another device where the report can be generated instead.

## Custom Model Benchmark

{% hint style="info" %}
The Custom Model Benchmark can only be used to benchmark models which have been uploaded to the NxAI Cloud.
{% endhint %}

The test allows you to benchmark your own models on different devices. The Certification Test includes the functionality to add your own models to its benchmark test. If you already have that downloaded, you can skip downloading and extracting the benchmark test. If you are only interested in benchmarking a model, you can instead download the smaller benchmark package:

```sh
## Create and enter folder for test
mkdir nxai_benchmark
cd nxai_benchmark

## Download testing suite
wget https://artifactory.nxvms.dev/artifactory/nxai_open/NXAITest/nxai_benchmark.tgz

## Unpack testing suite
tar -xvf nxai_benchmark.tgz
```

Install an NxAI Manager with runtime by following the steps at [#installing-nxai-manager](nx-ai-certification-test.md#installing-nxai-manager "mention")

Next, add as many models as you want to benchmark by running:

```
python3 Utilities/add_benchmark_model.py <Model ID>
```

And entering the ID of the model you want to test. The ID of your model can be found by navigating to your model in the [model cloud](https://admin.sclbl.nxvms.com/models). For example:

```
python3 Utilities/add_benchmark_model.py 4c5527f3-242a-4e17-b2e3-727dd6740f7c
```

After you have successfully added all the models you want to benchmark, you can download the model files from the cloud by running:

```
python3 Utilities/download_models.py
```

Once all your models have been downloaded, start the benchmark by running:

```
python3 Benchmark-Suite/run_suite.py
```

The test should now automatically benchmark all the models you've added and give you an overview of how this model/device performs.

## Troubleshooting

If the device is working well, but the test is not passing, feel free to contact us for support. To make it easier for us to provide support, please include log files so that we can see what is going wrong on the device.&#x20;

Make sure you're in the root folder of the test suite and run the following command to gather all the log files:

```shellscript
find ./ -type f \( -name "*.log" -o -name "failed_output.json" \) -printf '%P\n' | xargs tar -czf test_logs.tgz
```

This will create a file called `test_logs.tgz` , please send us this file with your request.
