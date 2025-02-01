import os
from diffusers import StableDiffusionPipeline
from PIL import Image
from diffusers import StableDiffusionPipeline
import torch

def get_pipeline():
    return StableDiffusionPipeline.from_pretrained(
        "CompVis/stable-diffusion-v1-4",
        low_cpu_mem_usage=True,
        torch_dtype=torch.float16
    ).to("cuda")

# Load the pre-trained AI model
pipe = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4")
pipe.to("cuda")  # Use GPU for faster inference

def process_image(image_path):
    # Load and preprocess the input image
    input_image = Image.open(image_path).convert("RGB")
    prompt = "A realistic rhinoplasty visualization with a reshaped nose"

    # Generate the processed image
    result = pipe(prompt, init_image=input_image, strength=0.5, guidance_scale=7.5).images[0]

    # Save the processed image
    output_path = os.path.join('app/processed', os.path.basename(image_path))
    result.save(output_path)

    return output_path
