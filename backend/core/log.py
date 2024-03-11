import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# 创建一个 FileHandler，用于写入日志文件
handler = logging.FileHandler('log_file.log', encoding="utf-8")
handler.setLevel(logging.INFO)

# 设置日志格式
formatter = logging.Formatter("[%(asctime)s] %(levelname)s %(message)s")
handler.setFormatter(formatter)

# 添加 FileHandler 到日志处理器中
logger.addHandler(handler)
