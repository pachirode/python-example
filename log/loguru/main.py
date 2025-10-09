from loguru import logger


def log_1():
    # 终端显式不受此处控制
    # 添加一个日志处理器，输出到文件；日志最低显式级别为 INFO
    # sink 链接本地文件，不存在新建，存在追加
    logger.add(sink="myapp.log", level="INFO", format="{time:HH:mm:ss}  | {message}| {level}")

    # debug结果不被显示到本地文件
    logger.debug("这是一条调试信息")
    logger.info("这是一条普通信息")


def log_2():
    from loguru import logger
    logger.add(sink="myapp1.log", level="INFO")
    logger.add(sink="myapp2.log", level="INFO")
    # 会同时存入所有 add 添加日志处理器，按照它们被添加的顺序来处理这些信息
    logger.info("这是一条普通信息，存入myapp2")


def log_3():
    # 删除所有已经添加的日志处理器，如果只想要移除部分，需要添加指定的 handler_id
    # handler1 = logger.add("myapp1.log", enqueue=True)
    # print(handler1)  # handler_id是移除的处理器的唯一标识符
    logger.remove()
    logger.add(sink="myapp3.log", level="INFO", format="{time:HH:mm:ss}  | {message}| {level}")

    logger.debug("这是一条调试信息存入myapp3")
    logger.info("这是一条普通信息存入myapp3")
    logger.info("这是一条普通日志存入myapp3")


def log_4():
    # 当文件大小达到100MB时创建新的日志文件，旧文件保留并重命名，用于防止单个日志文件变得过大。
    logger.add("file_1.log", rotation="100 MB")
    # 每天中午12时创建新的日志文件，旧文件保留并重命名
    logger.add("file_2.log", rotation="12:00")
    # 当日志文件存在超过一周时创建新的日志文件，旧文件保留并重命名
    logger.add("file_3.log", rotation="1 week")
    # 设置日志文件保留10天
    logger.add("file_4.log", retention="10 days")
    # 当文件大小达到100MB时创建新的日志文件，旧文件保留压缩为zip文件
    logger.add('file_{time}.log', rotation="100 MB", compression='zip')


@logger.catch
def div(x, y):
    return x / y


def my_filter(context):
    # 可以根据日志消息，内容，级别或者其他属性决定是否记录日志
    return "信息" in context["message"]


def log_5():
    # 删除所有已经添加的日志处理器，如果只想要移除部分，需要添加指定的 handler_id
    # handler1 = logger.add("myapp1.log", enqueue=True)
    # print(handler1)  # handler_id是移除的处理器的唯一标识符
    logger.remove()
    logger.add(sink="myapp5.log", filter=my_filter)

    logger.debug("这是一条调试信息存入myapp5")
    logger.info("这是一条普通信息存入myapp5")
    logger.info("这是一条普通日志存入myapp5")


def filter_user(record):

    return record["extra"].get("user") == "A"


def filter_bind():
    logger.add("myapp.log", filter=filter_user)

    # 向日志记录器添加额外的上下文
    logger.bind(user="A").info("来自A")
    logger.bind(user="B").info("来自B")


if __name__ == '__main__':
    # log_1()
    # log_2()
    # log_3()
    # div(0, 0)
    # log_5()
    filter_bind()