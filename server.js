const express = require('express');
const app = express();
const { exec } = require('child_process');

// 处理根路径请求
app.get('/', (req, res) => {
    // 执行Python脚本
    exec('python flask_app.py', (error, stdout, stderr) => {
        if (error) {
            console.error(`执行错误: ${error}`);
            res.status(500).send('执行Python脚本时出错');
            return;
        }
        res.send('Python脚本执行成功');
    });
});

// 启动服务器
const port = process.env.PORT || 3000;
app.listen(port, () => {
    console.log(`服务器运行在端口 ${port}`);
});