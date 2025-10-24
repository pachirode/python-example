# MCP

- 大模型，
    - 不能联网，无法操作外部工具
- 智能体
    - 操作外部工具

之前大模型写提示词调用外部工具，需要通过写提示词的方法，实现方法调用

##### 提示词案例

- 用途
    - 获取时间 `get_date` 获取时间
    - 触发场景，用户询问当前时间
- 参数设置
    - 需要提供时区
- 技术
    - 后端实现该函数
- 使用
    - 用户明确要求 `get_date`，符合调取工具的条件
    - 参数提取，引导用户输入时区
    - 后台调用该方法
    - 返回结果
- 弊端
    - 没有统一的接口

### MCP 协议

模型上下文协议，连接大模型和各种工具的统一接口

- `MCP Host`
    - 客户端软件，软件里面自带大模型
- `MCP Server`
    - 各种软件和工具的 `MCP` 接口

案例

- 百度地图 `https://github.com/baidu-maps/mcp/blob/main/src/baidu-map/python/src/mcp_server_baidu_maps/map.py`

### 配置环境

- `python`
- `nodejs`
- `MCP` 客户端
    - `Cherry Studio`
- 大模型密钥
    - `AiHubMix`
- 配置模型服务器

### 使用

```bash
# 克隆项目
git clone https://github.com/drfccv/12306-mcp-server.git
# 安装uv
curl-LsSf https://astral.sh/uv/install.sh | sh
# 安装依赖
uv sync
# 更新信息
uv run python scripts/update_stations.py
# 启动Server
uv run python scripts/start_server.py
```
