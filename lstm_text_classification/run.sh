
#环境配置
#pip install PyQt5==5.15.4 PyQt5-Qt5==5.15.2 PyQt5-sip==12.8.1 pyqt5-tools pyqt5-plugins matplotlib==3.2.0
#sudo apt-get install graphviz
#pip install keras==2.6
#tensorflow                2.6.2
#tensorflow-addons         0.13.0
#tensorflow-datasets       4.4.0
#tensorflow-estimator      2.6.0
#tensorflow-gpu            2.5.0
#tensorflow-hub            0.12.0
#tensorflow-metadata       1.2.0
#tensorflow-serving-api    2.6.2
#pip install pydot-ng graphviz pydot pydotplus
#sudo apt-get install -y mesa-utils libgl1-mesa-glx

# 运行命令
export DISPLAY=:0
export QT_XKB_CONFIG_ROOT=/usr/share/X11/xkb
export QT_DEBUG_PLUGINS=1
export FONTCONFIG_FILE=/etc/fonts/fonts.conf
export FONTCONFIG_PATH=/etc/fonts/
export PYTHONIOENCODING=utf-8;python processing.py
export PYTHONIOENCODING=utf-8;python train.py
export PYTHONIOENCODING=utf-8;python predicts.py
#终端的输出信息保存到log中:bash run.sh >& screen.log

# 记录
#<<comment
#Requirement already satisfied: PyQt5-Qt5==5.15.2 in /opt/conda/lib/python3.6/site-packages (5.15.2)
#Collecting PyQt5-sip==12.8.1
#  Downloading https://mirrors.aliyun.com/pypi/packages/f5/a7/3c52a17b065bcc69a6ca791b88901feeacd410235ec4b23441d975d0ecf4/PyQt5_sip-12.8.1-cp36-cp36m-manylinux1_x86_64.whl (278 kB)
#     |################################| 278 kB 1.1 MB/s
#Installing collected packages: PyQt5-sip
#  Attempting uninstall: PyQt5-sip
#    Found existing installation: PyQt5-sip 12.9.1
#    Uninstalling PyQt5-sip-12.9.1:
#      Successfully uninstalled PyQt5-sip-12.9.1
#ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.
#pyqt5-tools 5.14.2.1.7.3 requires pyqt5==5.14.2, but you have pyqt5 5.15.4 which is incompatible.
#pyqt5-plugins 5.14.2.2.2 requires pyqt5==5.14.2, but you have pyqt5 5.15.4 which is incompatible.
#
#Installing collected packages: matplotlib
#  Attempting uninstall: matplotlib
#    Found existing installation: matplotlib 3.3.4
#    Uninstalling matplotlib-3.3.4:
#      Successfully uninstalled matplotlib-3.3.4
#ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.
#osmnx 1.1.1 requires matplotlib>=3.3, but you have matplotlib 3.2.0 which is incompatible.
#mmdet3d 0.15.0 requires networkx<2.3,>=2.2, but you have networkx 2.5.1 which is incompatible.
#mmdet3d 0.15.0 requires numba==0.48.0, but you have numba 0.53.1 which is incompatible.
#Successfully installed matplotlib-3.2.0
#
#comment


