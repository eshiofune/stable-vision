import replicate

# Zip file containing input images, hosted somewhere on the internet
zip_url = "https://replicate.delivery/pbxt/IFYJBZ8XoHFfXPkkk3ToCv2n2ccyJHjSo5avPWsXJqbwHs7N/pokemon.zip"
zip_url = "https://drive.google.com/uc?export=download&id=1SzWjdzOGcNJJv8pjPlx6UhC5wh4sTf6M&confirm=t&uuid=5c27edde-99f7-4b7c-bd96-5d74034a330b&at=AB6BwCCurgyk3AJX78bPI5Y7PX-a:1701616498968"

# Train the model
lora_url = replicate.run(
    "replicate/lora-training:b2a308762e36ac48d16bfadc03a65493fe6e799f429f7941639a6acec5b276cc",
    input={"instance_data": zip_url, "task": "object"}
)