后端
1. 进入项目目录 cd backend
2. 在env文件夹下根据实际环境按需配置数据库信息、rabbitmq、redis等
3. 在 .env*.py 中配置数据库信息
	mysql数据库版本建议：8.0
	mysql数据库字符集：utf8mb4
4. 安装依赖环境
	pip install -r requirements.txt
5. 执行迁移命令：
	python manage.py makemigrations
	python manage.py migrate
6. 初始化数据(建立默认组，默认角色（带默认权限），普通用户)
	python manage.py init 
7. 启动项目
	python3 manage.py runserver 0.0.0.0:8000
