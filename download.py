# This file runs during container build time to get model weights built into the container
import os

MODEL_CACHE = "cache"

def download_model():
    # do a dry run of loading the huggingface model, which will download weights
    if not os.path.exists(MODEL_CACHE):
        os.makedirs(MODEL_CACHE)
    
    # Download GFPGANv1.4
    os.system("cd cache && wget https://github.com/TencentARC/GFPGAN/releases/download/v1.3.0/GFPGANv1.4.pth")
    # Download inswapper_128.onnx
    os.system("cd cache && wget http://43.153.104.112:814/inswapper_128.onnx.zip && unzip inswapper_128.onnx.zip")

    # Caches insight files
    os.system("mkdir -p /opt/conda/lib/python3.8/site-packages/insightface/models/buffalo_l/")
    os.system("wget https://github.com/deepinsight/insightface/releases/download/v0.7/buffalo_l.zip")
    os.system("unzip buffalo_l.zip -d /opt/conda/lib/python3.8/site-packages/insightface/models/buffalo_l")

if __name__ == "__main__":
    download_model()