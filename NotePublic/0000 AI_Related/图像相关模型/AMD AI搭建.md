#### Ubuntu 搭建 AMD GPU AI
### 显卡测试
```
python -c "import torch; print(torch.cuda.is_available())"
```


```
sudo apt update  
wget https://repo.radeon.com/amdgpu-install/6.4.2.1/ubuntu/noble/amdgpu-install_6.4.60402-1_all.deb  
sudo apt install ./amdgpu-install_6.4.60402-1_all.deb  
sudo amdgpu-install -y --usecase=graphics,rocm  
sudo usermod -a -G render,video $LOGNAME

1. 查看官方手册，看当前AMD显卡是否支持GPU 的ROCM
    - 大概率要更换linux kernel
2\. 去官网下载UBUNTU系统的AMD GPU Driver amdgpu-install_6.4.60402-1_all.deb  
3\. 安装Python虚拟环境  
4\. 安装PyTorch  
5\. 验证GPU ? (失败，切换Linux内核)  
    - sudo apt update  
    - sudo apt install linux-image-generic  
6\. 验证Python虚拟环境，并且安装ROCM，适配版本(更新到合适版本或者最新版，这个很重要)  
    - dpkg -l | grep rocm
```

## ComfyUI

```
cd ~/ComfyUI
python3 -m venv venv
source venv/bin/activate
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/rocm6.4
pip install -r requirements.txt

cd ComfyUI/custom_nodes/ComfyUI-Manager
pip install -r requirements.txt

```

### Models Download Link

```
https://huggingface.co/join
zhoushangjun1984@gmail.com/Hgt8964.
```