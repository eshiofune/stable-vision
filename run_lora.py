import replicate

lora_url = "https://replicate.delivery/pbxt/fEgTBPXdThRVZ63mD6AGkjKfQVAavynfJeMtIXBtfJFSEo0PC/tmp2jc6r3_auc.safetensors"

output_url = replicate.run(
    "replicate/lora:97ec1b97e5e6a6476e45ba7211d368509bbf39c30a927e39637f3cb98b36ac91",
    input={
        "prompt": "a picture in the style of <1>",
        "lora_urls": lora_url,
    },
)