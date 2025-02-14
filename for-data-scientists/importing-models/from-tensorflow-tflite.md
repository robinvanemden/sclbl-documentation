# From TensorFlow / TFLite

## About TensorFlow

![](../../.gitbook/assets/TensorFlow_logo.svg.png)

**TensorFlow** is a [free and open-source](https://en.wikipedia.org/wiki/Free_and_open-source_software) [software library](https://en.wikipedia.org/wiki/Library_\(computing\)) for [machine learning](https://en.wikipedia.org/wiki/Machine_learning) and [artificial intelligence](https://en.wikipedia.org/wiki/Artificial_intelligence). It can be used across a range of tasks but has a particular focus on [training](https://en.wikipedia.org/wiki/Types_of_artificial_neural_networks#Training) and [inference](https://en.wikipedia.org/wiki/Statistical_inference) of [deep neural networks](https://en.wikipedia.org/wiki/Deep_neural_networks).[\[4\]](https://en.wikipedia.org/wiki/TensorFlow#cite_note-4)[\[5\]](https://en.wikipedia.org/wiki/TensorFlow#cite_note-YoutubeClip-5)

TensorFlow was developed by the [Google Brain](https://en.wikipedia.org/wiki/Google_Brain) team for internal [Google](https://en.wikipedia.org/wiki/Google) use in research and production.[\[6\]](https://en.wikipedia.org/wiki/TensorFlow#cite_note-6)[\[7\]](https://en.wikipedia.org/wiki/TensorFlow#cite_note-7)[\[8\]](https://en.wikipedia.org/wiki/TensorFlow#cite_note-8) The initial version was released under the [Apache License 2.0](https://en.wikipedia.org/wiki/Apache_License_2.0) in 2015.[\[1\]](https://en.wikipedia.org/wiki/TensorFlow#cite_note-Credits-1)[\[9\]](https://en.wikipedia.org/wiki/TensorFlow#cite_note-Metz-Nov9-9)Google released the updated version of TensorFlow, named TensorFlow 2.0, in September 2019.[\[10\]](https://en.wikipedia.org/wiki/TensorFlow#cite_note-:12-10)

TensorFlow can be used in a wide variety of programming languages, including [Python](https://en.wikipedia.org/wiki/Python_\(programming_language\)), [JavaScript](https://en.wikipedia.org/wiki/JavaScript), [C++](https://en.wikipedia.org/wiki/C%2B%2B), and [Java](https://en.wikipedia.org/wiki/Java_\(programming_language\)).[\[11\]](https://en.wikipedia.org/wiki/TensorFlow#cite_note-:13-11) This flexibility lends itself to a range of applications in many different sectors.

## Model deployment from TFLite

You can upload a [TFLite](https://www.tensorflow.org/lite) model directly, and the cloud will take care of exporting the model to ONNX.

## Model deployment from TensorFlow

Exporting from TensorFlow to ONNX is also possible using [the tf2onnx tools](https://github.com/onnx/tensorflow-onnx), as illustrated in these examples: [here](https://github.com/scailable/sclblonnx/blob/master/examples/example_04.py) and [here](https://onnxruntime.ai/docs/tutorials/tf-get-started.html#converting-a-model).

Your TensorFlow model can be exported to ONNX and subsequently using cleaned and checked by the the `sclblonnx` package for an upload to the Nx AI cloud.&#x20;

After obtaining a [clean ONNX graph that adheres to our requirements](../onnx-requirements.md), you can upload it to the [Nx AI cloud for deployment](../../nx-ai-cloud/upload-your-model/).
