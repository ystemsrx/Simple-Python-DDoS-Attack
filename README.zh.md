[English](README.md)

# 简单DDOS攻击Python脚本

## 免责声明
此脚本仅供教育目的使用。作者不对由此脚本引起的任何误用或损害负责。使用风险自负。

## 概述
这个Python脚本旨在通过向指定的IP地址或URL发送大量数据包来执行DDOS攻击。它支持使用UDP和TCP发送数据包。此工具仅供学习之用，不应恶意使用。

## 特点
- 验证IP地址。
- 如果提供了URL，将URL转换为IP地址。
- 使用UDP和TCP持续向目标IP地址或URL发送数据包。

## 要求
- Python 3.x
- 访问终端或命令行界面。

## 如何使用
1. 确保系统已安装Python。
2. 打开终端或命令行。
3. 导航到包含`ddos-attack.py`脚本的目录。
4. 使用以下命令运行脚本：
   ```
   python ddos-attack.py
   ```
5. 根据提示，输入您希望目标的IP地址或URL。

## 注意
- 脚本当前默认目标端口为443（HTTPS）和80（HTTP）。
- 注意执行DDOS攻击的法律后果。未经许可，针对网络或服务器的攻击是非法的。
