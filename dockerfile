# 使用一个基础镜像
FROM python:3.9

# 设置工作目录
WORKDIR /app

# 复制项目文件到容器中
COPY ./web /app

#更换国内源（如果需要的话）
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple

RUN pip install --upgrade pip

# 安装项目依赖
RUN pip install -r requirements.txt

# 复制 SSL 证书和私钥到容器中
COPY ./web/server.crt /app/server.crt
COPY ./web/server.key /app/server.key

# 暴露Django运行的端口
EXPOSE 443

# 启动Django应用
CMD ["python", "manage.py", "runserver_plus", "0.0.0.0:443", "--cert", "server.crt", "--key", "server.key"]
