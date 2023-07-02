# DRAGON

Pytorch implementation for "Enhancing Dyadic Relations with Homogeneous Graphs for Multimodal Recommendation"-[arxiv](https://arxiv.org/abs/2301.12097)

## Overview of DRAGON
<p>
<img src="https://github.com/hongyurain/DRAGON/blob/main/images/structure.jpg" width="800">
</p>

## Data
Data could be download from Google Drive: [Baby/Sports/Clothing](https://drive.google.com/drive/folders/1eIrFm4ZqMI9poun9fdxrRZUcGdGyBujp?usp=sharing)  
## Run the code
1. Download the data from the data link we provided above, then put the download data to the ./data folder
2. Run generate-u-u-matrix.py on the dataset you want to generate the user co-occurrence graph
3. Enter the src folder and run with
`python main.py -m DRAGON -d dataset_name`  
## The parameters to reproduce the result in our paper
| Datasets | learning rate | reg weight |
|----------|--------|---------|
| Baby     | 0.0001      | 0.001     |
| Sports   | 0.0001      | 0.001     |
| Clothing     | 0.0001      | 0.1     |

