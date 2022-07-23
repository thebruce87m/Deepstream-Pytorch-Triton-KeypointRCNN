

wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh

conda config --set auto_activate_base false

conda env create -f environment.yml



Create the environment:
```bash
conda env create --file environment.yml
```

Update after editing `environment.yml`
```bash
conda env update --file environment.yml
```

Active the virtual environment (Each time you open a new terminal)
```bash
conda activate ds-pyt-triton
```

Note: How to Deactivate
```bash
conda deactivate
```