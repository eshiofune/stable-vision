import replicate

lora_url = ""

output_url = replicate.run(
    "replicate/lora:97ec1b97e5e6a6476e45ba7211d368509bbf39c30a927e39637f3cb98b36ac91",
    input={
        "prompt": "an office chair in the style of <1>",
        "lora_urls": lora_url,
    },
)