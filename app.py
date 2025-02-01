from flask import Flask
from diffusers import StableDiffusionPipeline
import torch

app = Flask(__name__)

# Initialize the Stable Diffusion model with low CPU memory usage or half-precision
pipe = StableDiffusionPipeline.from_pretrained(
    "CompVis/stable-diffusion-v1-4",
    low_cpu_mem_usage=True,
    torch_dtype=torch.float16
).to("cuda")

@app.route("/")
def home():
    return "Stable Diffusion is ready!"

if __name__ == "__main__":
    app.run(debug=True)
