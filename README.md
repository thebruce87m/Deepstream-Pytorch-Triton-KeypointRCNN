

# Dependencies

Install MiniConda
```bash

# Download
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh

# Change permissions to allow execute
chmod u+x Miniconda3-latest-Linux-x86_64.sh

# Execute
./Miniconda3-latest-Linux-x86_64.sh

# No base on boot
conda config --set auto_activate_base false
```


# Download Keypoint R-CNN Model and export as Torchscript

Create the environment (first time only):
```bash
conda env create --file environment.yml
```

Active the virtual environment (Each time you open a new terminal)
```bash
conda activate ds-pyt-triton
```

Export the model

```bash
python scripts/model_to_torchscript.py
```

# Conda notes

Update after editing `environment.yml`
```bash
conda env update --file environment.yml
```

Note: How to Deactivate
```bash
conda deactivate
```