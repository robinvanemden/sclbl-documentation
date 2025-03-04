# Nx AI Certification Test

## Certification Test

### Quickstart

The Nx AI Certification test should be able to run on any Ubuntu installation which is also compatible with Network Optix Server.&#x20;

Ensure your device has at least a few gigabytes of free space, a working internet connection and a working Python 3 and Pip installation.

{% code title="Python requirements" %}
```bash
# on some systems you may need to install pip
# for example with the following command on ubuntu
sudo apt update
sudo apt install python3-pip
```
{% endcode %}

{% hint style="warning" %}
If you are testing a GPU or NPU, also make sure that the required drivers are installed, for example the Jetpack drivers for NVIDIA accelerators.
{% endhint %}

Execute the following commands:

{% code title="Download tests" %}
```bash
## Create and enter folder for test
mkdir nxai_test
cd nxai_test

## Download testing suite
wget https://artifactory.nxvms.dev/artifactory/nxai_open/NXAITest/nxai_test.tgz

## Unpack testing suite
tar -xvf nxai_test.tgz
```
{% endcode %}

{% code title="Ubuntu quirk" %}
```bash
# on newer ubuntu systems you need to activate a python venv
sudo apt install python3-venv
python3 -m venv ./ # create venv in current dir
source ./bin/activate # activate python venv in current dir
```
{% endcode %}

{% code title="Install acceleration library" %}
```bash
## Install all required Python packages
pip3 install -r requirements.txt

## Install NX AI Manager
./Utilities/install_nxai_manager.sh

## Install acceleration runtime
python3 Utilities/install_acceleration_library.py
#python3 Utilities/install_acceleration_library.py "Nx CPU"
```
{% endcode %}

{% hint style="info" %}
Running the `python3 Utilities/install_acceleration_library.py` command will automatically detect the available hardware acceleration that is available on your device. If the script finds more than one option, it will pause execution and ask you to choose. If you want to execute these commands without pausing, add an the accelerator name to the command, such as the "Nx CPU" example.
{% endhint %}

{% code title="Download models" %}
```bash
## Download required models
python3 Utilities/download_models.py
```
{% endcode %}

{% hint style="warning" %}
The `download_models.py` command will download approximately 3.5GB of model data, depending on your connection this may take a while.
{% endhint %}

{% code title="Run tests" %}
```bash
## Start test
python3 all_suites.py

## Gather info
python3 Utilities/gather_hwinfo.py

## Upload results to cloud
python3 Utilities/upload_results.py
```
{% endcode %}

{% hint style="warning" %}
The test will run for a couple of hours and will stress the device. Do not power off your device.
{% endhint %}

### Introduction

The Nx AI Certification Test is meant to test any device to ensure it is compatible and stable enough to run the Nx AI Manager for extended periods of time.&#x20;

The test will attempt to run multiple common model architectures, with different sizes, and even multiples of those models to test compatibility and what can be expected to run on the device. The test will also run long operation tests to check if there are any memory issues or degradation in performance due to overheating or other reasons.

Finally, the test will gather all results in a folder which can be used to generate a report, either on the device or somewhere else. The report should contain enough information to determine if the device is indeed compatible.

### Installing Nx AI Manager

A useful script is provided to install the Nx AI Manager runtime locally within the test environment. This will ensure that this testing does not interfere with any existing installations on the device.&#x20;

```bash
./Utilities/install_nxai_manager.sh
```

### Installing Nx Acceleration Library

Acceleration libraries act as layers between the Nx AI Manager and your acceleration hardware. Any device should be able to run the tests on CPU, without acceleration hardware. However if your device has AI acceleration hardware, such as an Nvidia Cuda device, or a Hailo AI chip, these can be used to accelerate the AI pipeline.

Running this script will automatically detect available hardware. If more than one is found, the script will present a list of options which you can choose from.

```
python3 Utilities/install_acceleration_library.py
```

### Download Models

The Certification Test will test a variety of models to see if they can run on your device and libraries. After installing the acceleration library the correct models for your device can be downloaded.

{% hint style="warning" %}
This step could use a lot of data as many large files need to be downloaded. This might also take a long time depending on network conditions.
{% endhint %}

```
## Download required models
python3 Utilities/download_models.py
```

### Running test

The Nx AI Certification test includes a collection of tests to test different aspects of your device to ensure that the Nx AI Toolkit can run on your device. To run all of these tests in one large test, run:

```bash
python3 all_suites.py
```

This could take many hours to complete.

### Gathering Hardware Information

This command will detect some hardware information about your device and package it with the test results. This will gives context to the test results and allows for better analysis about the device's performance.

```
## Gather info
python3 Utilities/gather_hwinfo.py
```

### Uploading Results

An endpoint was created where you can upload and view the test results of your device. After the test has completed, run the following to automatically upload the script to the cloud:

```bash
python3 Utilities/upload_results.py
```

## Custom Model Benchmark

{% hint style="info" %}
The Custom Model Benchmark can only be used to benchmark models which have been uploaded to the Nx AI Cloud.
{% endhint %}

The test allows you to benchmark your own models on different devices. The Certification Test includes the functionality to add your own models to its benchmark test. If you already have that downloaded, you can skip downloading and extracting the benchmark test. If you are only interested in benchmarking a model, you can instead download the smaller benchmark package:

{% code title="Download benchmark" %}
```sh
## Create and enter folder for test
mkdir nxai_benchmark
cd nxai_benchmark

## Download testing suite
wget https://artifactory.nxvms.dev/artifactory/nxai_open/NXAITest/nxai_benchmark.tgz

## Unpack testing suite
tar -xvf nxai_benchmark.tgz
```
{% endcode %}

Install an Nx AI Manager with runtime by following the steps at [#installing-nx-ai-manager](nx-ai-certification-test.md#installing-nx-ai-manager "mention")

Next, add as many models as you want to benchmark by running:

```bash
python3 Utilities/add_benchmark_model.py <Model ID>
```

And entering the ID of the model you want to test. The ID of your model can be found by navigating to your model in the [model cloud](https://admin.sclbl.nxvms.com/models). For example:

```bash
python3 Utilities/add_benchmark_model.py 4c5527f3-242a-4e17-b2e3-727dd6740f7c
```

After you have successfully added all the models you want to benchmark, you can download the model files from the cloud by running:

```bash
python3 Utilities/download_models.py
```

Once all your models have been downloaded, start the benchmark by running:

```bash
python3 Benchmark-Suite/run_suite.py
```

The test should now automatically benchmark all the models you've added and give you an overview of how this model/device performs.

## Troubleshooting

If the device is working well, but the test is not passing, feel free to contact us for support. To make it easier for us to provide support, please include log files so that we can see what is going wrong on the device.&#x20;

Make sure you're in the root folder of the test suite and run the following command to gather all the log files:

```bash
find ./ -type f \( -name "*.log" -o -name "failed_output.json" \) -printf '%P\n' | xargs tar -czf test_logs.tgz Results/
```

This will create a file called `test_logs.tgz` , please send us this file with your request.
