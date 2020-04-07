# 项目描述

基于 Quart 框架的 blog 后端服务

采用 多模块 模式 来分割业务代码

该项目脚手架可以作为任意 后端服务的基础脚手架使用

## Quick Start
> Python 版本要求 >= python3.7.0

1. `git clone https://github.com/HonorIpaddr/IpaddrBlog.git`
2. `cd IpaddrBlog`
3. python3 -m venv venv-web
4. 激活 venv
   1. windows powershell
      ```powershell
      .\venv-web\Scripts\Activate.ps1
      ```
   2. windows cmd
      ```cmd
      .\venv-web\Scripts\activate.bat
      ```
   3. linux/unix/macOS
      ```shell
      source ./venv-web/bin/activate
      ```
5. 安装依赖
   ```
   pip install -r requirements.txt
   ```
6. 启动项目
   1. vscode 中 ctrl+shift+d ,点击 start 按钮
   2. 如果想要在 terminal 环境直接运行，
      ```
      python dev.py
      ```
7. 上线前，一定要关闭 debug
   ```
   python start.py
   ```

## 技术支持 及 交流

QQ 群: 255195052

商业项目、外包、技术支持：
QQ：2365553250

## 感谢

1. 首先感谢父母，带我来到这个世界，给了我最宝贵的生命；
2. 感谢 Quart 的作者 Philip Jones ，制作如此优秀的框架；
3. 感谢社会。

## 工程目录说明

1. model 用于定义实体类
2. blogApp 中为 整个 application
3. blogCtrl、userCtrl 等按照业务划分的控制器，导出对应 api
4. blogApp.**init**.py 中注册蓝图
5. cli.py 定义一些常用 cli 命令，方便快速开发

## 特性

- [x] async
- [x] 多模块应用
- [x] bluprint
- [x] 兼容 flask 扩展
- [x] 支持 http2
- [x] 已配置 vscode lunch.json ，基本上是开箱即用
- [ ] 友好的404
- [ ] 统一的 responseBody 模板
- [ ] 数据库生成实体类和基本增删改查接口
- [ ] 身份认证
- [ ] 从实体类生成数据库
- [ ] 生成 docker image
