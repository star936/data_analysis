# data_analysis
### Conda的使用
**使用conda进行python虚拟环境和依赖包的管理,使用如下:**
```bash
# 创建名字为venv，python为2.7版本的虚拟环境
conda create -n venv python=2.7
# 开启环境
source activate venv
# 退出环境
source deactivate venv
# 依赖包导出
conda list --export > requirements.txt
# 依赖包安装
conda create -n venv --file requirements.txt
conda install -n venv pandas
# 列出所有虚拟环境(两种方法)
conda env list
conda list --envs
```
