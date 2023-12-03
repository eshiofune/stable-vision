import replicate

# Zip file containing input images, hosted somewhere on the internet
zip_url = "https://replicate.delivery/pbxt/IFYJBZ8XoHFfXPkkk3ToCv2n2ccyJHjSo5avPWsXJqbwHs7N/pokemon.zip"

# Train the model
lora_url = replicate.run(
    "replicate/lora-training:b2a308762e36ac48d16bfadc03a65493fe6e799f429f7941639a6acec5b276cc",
    input={"instance_data": zip_url, "task": "object"}
)