- This is the repository for the paper "Two-stage Denoising Diffusion Model for Source Localization in Graph Inverse Problems".

- The code has been tested under Pytorch 2.0.

- Datasets names are 'Digg', 'Memetracker', 'Android', 'Christianity', 'Twitter'.

## Model Overview
Two stage framework:

 <img src="assets/OVERVIEW_00.png" alt="isolated" width="500"/>

which is composed  by the **coarse initialization stage**:
![twostage](https://github.com/marooncabbage/SL-Diff/blob/main/assets/STAGE1.png)

and the **fine stage**:
![twostage](https://github.com/marooncabbage/SL-Diff/blob/main/assets/STAGE2.png)
