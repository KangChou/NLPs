# About this Code
参考来自： **_Cross-lingual Knowledge Graph Alignment via Graph Matching Neural Network_**.

github: https://github.com/syxu828/Crosslingula-KG-Matching
# Env Setting
Python 3.6 (**important!**)\
Tensorflow 1.15.0\
scipy\
tqdm\
argparse\
codecs

# How To Run The Codes

 DBP15K datasets: https://docs.google.com/uc?export=download&id=1ggYlYf2_kTyi7oF9g07oTNn3VDhjl7so&confirm=t

To train your model, you need:

(1) Generate the training data by using the following command under DBP15K dataset: (take zh_en as an example)
    
    python3 preprocessor.py zh_en train 20  # gen the training examples
    python3 preprocessor.py zh_en test 1000 # gen the test examples
    python3 preprocessor.py zh_en dev  1000  # gen the dev examples
    
cd DBP15K

![image](https://user-images.githubusercontent.com/36963108/175223144-0c3c9a29-7735-4979-8240-439408fb7137.png)


    
Note:
For the first time, it may take almost 3-4 hours to generate the candiate file.
You may also choose to directly download these files from https://drive.google.com/open?id=1dYJtj1_J4nYJdrDY95ucGLCuZXDXI7PL and directly use them to train the model.
    
(2) Train & Test the model: (take zh_en as an example)
  
    python3 run_model.py train zh_en zh_en_model -epochs=10 -use_pretrained_embedding
    python3 run_model.py test zh_en zh_en_model -use_pretrained_embedding
    
![image](https://user-images.githubusercontent.com/36963108/175223278-2ad78407-5a22-4be9-903e-fa620e3edd24.png)

    
    
# How To Cite The Codes
Please cite our work if you like or are using our codes for your projects!

Kun Xu, Mo Yu, Yansong Feng, Yan Song, Zhiguo Wang and Dong Yu,
"Cross-lingual Knowledge Graph Alignment via Graph Matching Neural Network", arXiv preprint arXiv:1905.11605.
 
@article{xu2019graphmatching, 
title={Cross-lingual Knowledge Graph Alignment via Graph Matching Neural Network}, 
author={Xu, Kun and Wang, Liwei and Yu, Mo and Feng, Yansong and Song, Yan and Wang, Zhiguo and Yu, Dong}, 
year={2019} 
}  

   

