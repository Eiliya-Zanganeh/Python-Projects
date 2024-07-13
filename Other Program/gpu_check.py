import onnxruntime as ort
import torch
import tensorflow as tf

print(f'onnxruntime: {ort.get_device()}')
print(f'torch: {torch.cuda.is_available()}')

gpus = tf.config.list_physical_devices('GPU')
if not gpus:
    print("No GPU device found, using CPU.")
else:
    print("GPU device found:", gpus)
