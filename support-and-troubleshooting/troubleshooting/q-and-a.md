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



### The bounding boxes appear to be out of sync with the stream

This issue occurs when the visualized stream differs from the one used for AI inference. It typically happens when using a [test camera](https://support.networkoptix.com/hc/en-us/articles/360018067074-Testcamera-IP-Camera-Emulator). The problem usually arises from a mismatch between the primary and secondary streams, leading to the visualization of a different stream than the one used for AI processing. If the plugin operates on the secondary stream while you are viewing the primary stream, it can appear as though the bounding boxes are out of sync in the video:

<figure><img src="https://mail.google.com/mail/u/1?ui=2&#x26;ik=c0def2cba3&#x26;attid=0.1&#x26;permmsgid=msg-a:r-2168785569618819936&#x26;th=191792f7d5bbb8d8&#x26;view=fimg&#x26;fur=ip&#x26;sz=s0-l75-ft&#x26;attbid=ANGjdJ8ZnW7QaSsRFItDttyEXycruOmPMkS0U_hLiykPnOtn7D5k9xtRW1QSuIVYLoMtJAwL9h7jFE5JlgElX7KaBMBQe2uatQe15E0BWN5Td0RATvQOfHZFZq2YtDE&#x26;disp=emb&#x26;realattid=ii_m050ie1e0" alt=""><figcaption></figcaption></figure>

To fix this issue, either set the plugin to use the Primary stream or view the ‘Low’ resolution stream in the Client:

<figure><img src="https://mail.google.com/mail/u/1?ui=2&#x26;ik=c0def2cba3&#x26;attid=0.2&#x26;permmsgid=msg-a:r-2168785569618819936&#x26;th=191792f7d5bbb8d8&#x26;view=fimg&#x26;fur=ip&#x26;sz=s0-l75-ft&#x26;attbid=ANGjdJ8lXNyzRSaNphCAACkVJjOUOVYmKzkcZC0DllLD045hD7Rn4RWByF8RtqAItqGTr1SzvXWU6FG6SUV4PMonq30IZ84HktwnnYqyEGIKIUgMbbAn_y0nHyT931s&#x26;disp=emb&#x26;realattid=ii_m050ir0f2" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (120).png" alt=""><figcaption></figcaption></figure>
