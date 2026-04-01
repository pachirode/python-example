# hatch 库

一款现代，可扩展的 python 项目管理器

### 构建后端

##### 默认值

可以根据版本控制系统提供默认值 (.gitignore)
包含 `Wheel` 包更加谨慎

##### 配置

采用类似 `.gitignore` 的语法
配置文件写在单个文件中

### 版本管理

能在请求版本不存在时，自动下载发行版本

### 虚拟环境隔离

# 使用

```bash
pip install hatch
```

### 创建新项目

```bash
hatch new "Hatch Demo"
```

### 配置文件

在 `pyproject.toml` 文件中定义元数据

特定的配置项目可以放在 `hatch.toml` 文件

### 虚拟环境

```bash
hatch env create
```

> 除非显示指定环境，否则默认使用 `default`

### 启动 shell

```bash
hatch shell
```

### 安装查看

```bash
pip install -e .
pip show hatch-demo 
```

### 查看环境

```bash
hatch run python -c "import sys;print(sys.executable)"
AppData\Local\hatch\env\virtual\hatch\KM98KXxF\hatch\Scripts\python.exe
```

### 依赖

将 `cowsay` `pyproject.toml` 中添加到 `dependencies` 数组

```bash
# 修改完执行
hatch env prune
hatch env create
hatch run cowsay -t "Hello, world!"
```