# 使用官方Python基础镜像
FROM python:3.9-slim

# 设置工作目录
WORKDIR /app

# 复制项目文件到容器
COPY . /app

# 安装依赖
RUN pip install --no-cache-dir flask

# 暴露应用端口
EXPOSE 5000

# 启动命令
CMD ["python", "flask_app.py"]