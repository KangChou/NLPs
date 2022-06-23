# pip freeze > requirements.txt
pip install -r requirements.txt

cd DBP15K
python3 preprocessor.py zh_en train 20  # gen the training exam
python3 preprocessor.py zh_en test 1000 # gen the test examples
python3 preprocessor.py zh_en dev  1000  # gen the dev examples

cd ../
python3 run_model.py train zh_en zh_en_model -epochs=10 -use_pretrained_embedd
python3 run_model.py test zh_en zh_en_model -use_pretrained_embedding
    