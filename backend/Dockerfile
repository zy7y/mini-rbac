# 第一阶段：构建镜像
FROM python:3.9-slim-buster AS build
WORKDIR /app
COPY requirements.txt .
RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \
    echo 'Asia/Shanghai' >/etc/timezone && \
    pip install --no-cache-dir --user -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/
COPY . .
# 第二阶段：运行镜像
FROM python:3.9-slim-buster
WORKDIR /app
COPY --from=build /root/.local /root/.local
COPY --from=build /app .
ENV PATH=/root/.local/bin:$PATH
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
