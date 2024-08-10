# Q\&A

### I don't see any bounding boxes in the Nx Client <a href="#i-dont-see-any-bounding-boxes-in-the-nx-client" id="i-dont-see-any-bounding-boxes-in-the-nx-client"></a>

First make sure that the model actually has something to detect. For example if you're using a model that is expecting vehicles, that will not be detected on a camera that is viewing an empty warehouse.If the camera actually sees something that should be detected you can check if the objects view is active. If the notifications or another tab is active the bounding boxes will not be displayed.When you switch to the objects tab the bounding boxes should show up.If there are still no bounding boxes, please go through the [plugin checks](https://app.gitbook.com/o/bcLqIPiXVKcQXjqrnQSu/s/4Ho7de78I0gSMd4YY72l/support-and-troubleshooting/troubleshooting/plugin-checks), [system checks](https://app.gitbook.com/o/bcLqIPiXVKcQXjqrnQSu/s/4Ho7de78I0gSMd4YY72l/support-and-troubleshooting/troubleshooting/system-checks) and [things to try](https://app.gitbook.com/o/bcLqIPiXVKcQXjqrnQSu/s/4Ho7de78I0gSMd4YY72l/support-and-troubleshooting/troubleshooting/things-to-try) sections to solve the problem.

<figure><img src="https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F4Ho7de78I0gSMd4YY72l%2Fuploads%2FUxDv5NA4DaORwcb9tGgP%2Fimage.png?alt=media&#x26;token=6c34c3d4-f646-4dda-a9f2-d3ce2b949e41" alt=""><figcaption></figcaption></figure>

<figure><img src="https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F4Ho7de78I0gSMd4YY72l%2Fuploads%2FtfickTa2IFac8PNGeXPY%2Fimage.png?alt=media&#x26;token=4985cf72-ed7f-4b48-9612-2d565e3f873e" alt=""><figcaption></figcaption></figure>

### The Nx AI Manager cannot be started <a href="#the-nx-ai-manager-cannot-be-started" id="the-nx-ai-manager-cannot-be-started"></a>

If, after clicking Start, the following message appears:There could be a problem with your installation. Try manually installing the Nx AI Manager [7.1 NX AI Manager Manual Installation](https://app.gitbook.com/o/bcLqIPiXVKcQXjqrnQSu/s/4Ho7de78I0gSMd4YY72l/nx-ai-manager/advanced-configuration/nx-ai-manager-manual-installation)​If there are no bounding boxes being displayed in the Nx Client, it could point to a problem with the runtime, or driver incompatibilities. It can also mean that the model is not picking up any useful data.

<figure><img src="https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F4Ho7de78I0gSMd4YY72l%2Fuploads%2F2aceU4cO160rtVwxloDa%2Fruntime_status_nostart.png?alt=media&#x26;token=5db6d9e4-c393-40a6-92d2-102705e1aca0" alt=""><figcaption></figcaption></figure>

### How can I check if the Metadata is generated <a href="#how-can-i-check-if-the-metadata-is-generated" id="how-can-i-check-if-the-metadata-is-generated"></a>

> I noticed that plugin stops generating metadata for some reason Is there any log or additional information I can collect for you so it would be useful in this case?

For advanced users, it might be advisable to check the output log of the Nx Mediaserver to see if any errors are logged. The log can be gathered by executing:

```sh
sudo journalctl -u networkoptix-metavms-mediaserver.service
```

### Is it possible to send output to a different endpoint? <a href="#is-it-possible-to-send-output-to-a-different-endpoint" id="is-it-possible-to-send-output-to-a-different-endpoint"></a>

No this is not possible. It is possible to access the data and pass it through.TODO: show how to do that
