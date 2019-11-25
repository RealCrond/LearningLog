# LearningLog
Learning python web 

文件树：
|--LearningLog    		   #项目文件夹
	|-- ll_env		   #step1 : pip3 install virtualenv   step2 : virtualenv ll_env或者python -m venv ll_env  PS:激活该虚拟环境 soruse env1/Script/activate    退出该虚拟环境：deactivate
	|-- learming_log    	   #Django项目名称  #命令行: django-admin startproject learning_log
	|   |-- db.sqlite3
	|   |-- manage.py
	|   |-- learning_log
	|       |--__init__.py
	|       |--__pycache__
	|       |--settings.py     #在INSTALLED_APPS字段中配置自定义的APP
	|       |--urls.py         #将url访问"引流"至自定义APP
	|       `--wsgi.py
	|
	|   |--firstapp   	   #App1    #命令行: python manage.py startapp firstapp
	|       |--admin.py
	|       |--__init__.py
	|       |--migrations
	|       |--models.py
	|       |--tests.py
	|       |--view.py         #自定义的url处理函数
	|       |--urls.py         #映射url->处理函数    
	|       `--templates
	|            |--htmls
	|                 |--index.html
	|                 |--base.html
	|                 |--topic.html
	|                 `--topics.html
	|
	|   |--secondapp  	   #App2    #命令行: python manage.py startapp firstapp
	|	|--admin.py
	|	|--__init__.py
	|	|--migrations
	|	|--models.py
	|	|--tests.py
	|	|--view.py
	|	|--urls.py
	|	`--templates
	|	     |--htmls
	|	          |--index.html
	|	          |--base.html
	|	          |--topic.html	
	|	          `--topics.html
	|
