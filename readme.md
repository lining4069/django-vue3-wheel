## 后端

### 后端项目初始化

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

### 后端项目基础结构

backend/  
-appfiles:系统文件存储根目录  
-apps:应用目录  
-common:公共包资源，封装公共类、方法、符合规范的统一的封装  
-conf:项目设置和部署配置  
-env:不同部署环境下的系统配置文件，包含数据库等配置信息  
-loggers:日志存储  
-service:分离、抽象出的apps下的应用的数据逻辑  
-tests:apps下应用的单元测试  
-manage.py 启动文件  
-requirement 项目环境依赖