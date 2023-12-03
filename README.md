# stable-vision

Follow [this tutorial](https://replicate.com/blog/lora-faster-fine-tuning-of-stable-diffusion).

Create an API token on Replicate and add it to your environmental variables:

```
export REPLICATE_API_TOKEN="xx-xx"
```

Install replicate:


```
pip install replicate
```

Run the following in order:

- [upload_images.py](/upload_images.py) (optional) - if you want to upload your training images to Replicate's server. You can also use Google Drive or GitHub Pages.
- [train_lora.py](/train_lora.py) - Add a URL pointing to your ZIP archive containing your training images to this script then run it. You can change the `task` parameter to "style", "object" or "person". Make sure to copy the model URL from Replicate. It usually ends in `.safetensors`.
- [run_lora.py](/run_lora.py) - Add a prompt, enter the LoRA model URL, and run the model.