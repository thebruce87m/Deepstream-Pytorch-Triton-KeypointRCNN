#https://djl.ai/docs/pytorch/how_to_convert_your_model_to_torchscript.html

import torch
import torchvision


# Instance of the model
model = torchvision.models.detection.keypointrcnn_resnet50_fpn(pretrained=True)

# Switch the model to eval model
model.eval()

# An example input you would normally provide to your model's forward() method.
example = [torch.rand(3, 300, 400), torch.rand(3, 500, 400)]

# Use torch.jit.trace to generate a torch.jit.ScriptModule via tracing.
traced_script_module = torch.jit.trace(model, example)

# Save the TorchScript model
traced_script_module.save("traced_resnet_model.pt")
