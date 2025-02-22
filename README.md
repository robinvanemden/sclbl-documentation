# Nx AI Manager plugin v4.3

The Nx AI Manager plugin is a tool that enables you to create and manage large-scale Edge AI solutions using [Network Optix Meta](https://meta.nxvms.com/) and the [Network Optix toolkit](https://www.networkoptix.com/developers/nx-toolkit). With this plugin, you can turn any compatible edge device, like a router, gateway, or IPC, into a "smart" device that can run advanced Artificial Intelligence (AI) and Machine Learning (ML) models on input data. Using AI and ML models, you can analyze a video stream and gain valuable insights, such as counting the number of cars passing by in the video stream.

The documentation here offers detailed instructions on setting up and configuring your edge AI solutions on Linux-based Nx Meta-supported edge hardware.

## The high-level Nx AI Manager plugin Architecture.

The Nx AI Manager plugin is the starting point for creating AI solutions within the Nx Meta framework. It can run within any Linux-based Nx Meta Server on any supported edge device (such as a smart camera, gateway, and PC) and allows you to configure the solution you want to create by selecting an AI model and configuring the device settings.&#x20;

The Nx AI Manager plugin currently mainly focuses on video input (a stream of images from a camera).

You can use the Nx Cloud Platform to remotely configure your solution and manage it at scale: i.e., if you have hundreds of devices, you can manage them in one go.&#x20;

The core "magic" that goes into creating edge AI solutions is the **AI model**; the model effectively transforms the input (images) to the desired output (a count of the number of people in front of the camera, an "OK" / "NG" output for product inspection, the license plate of a car in front of the camera, or whether or not a person in front of the camera is wearing a helmet). We have some of off-the-shelf models in our model library, allowing users to configure new solutions. However, if you are a data scientist, you can create models and upload them to our platform for your custom needs.

## Often used terms

Here, we provide a short list of terms that pop up repeatedly in these docs and are good to know:

* **The Nx AI Manager plugin**: Nx plugin that runs on an edge device, enabling you to configure your edge AI solution. Also just called **the plugin**.
* **The Nx AI Manager**: is the component of the Nx toolkit responsible for running AI models on AI accelerators.
* **Nx AI Manager Cloud:** The Nx cloud environment (found at [https://admin.sclbl.nxvms.com/](https://admin.sclbl.nxvms.com/)) allows you to \
  a) manage your devices and AI models and \
  b) add your models to your personal AI model collections.&#x20;
* **The Network Optix Toolkit**: All development tools, libraries, applications, and utilities that enable integration with Network Optix in your own application are available, including the AI Manager plugin and the [Nx Meta API](https://meta.nxvms.com/doc/developers/api-tool/main).
* **EVOS**: Network Optix's Enterprise Video Operating System, which includes all of Network Optix's open tools, enables developers to manage numerous video streams across multiple locations, deploy on-site AI models (at the edge), visualize videos, establish business rules, and deliver meaningful applications to end users.
* **Nx Meta:** The version of EVOS that is mostly used for development with the Nx AI Manager
* **An AI/ML model:** We use this term somewhat loosely for any model definition that describes the transformation of input (streams of images) to output (bounding boxes, license plate, "OK"/"NG" etc.). This model can be a Deep Neural Network (AI), a simple classification model (ML), or a traditional Vision pipeline. Ultimately, the logic running on the device does the "magic".&#x20;
* **Edge device:** We loosely refer to any device (camera, gateway, IPC, etc.) that runs the Nx AI manager.&#x20;
