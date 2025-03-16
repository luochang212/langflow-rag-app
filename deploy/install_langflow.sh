# https://docs.langflow.org/

conda create -n langflow python=3.11 -y

conda activate langflow

pip install langflow -U -i https://mirrors.aliyun.com/pypi/simple/

langflow run

# pre-release version
# python -m pip install langflow --pre --force-reinstall
# python -m langflow run
