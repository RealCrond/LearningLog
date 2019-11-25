# LearningLog
Learning python web<br>
文件树:<br>
>|--LearningLog    		   #项目文件夹<br> 
>>>|-- ll_env		   #step1 : pip3 install virtualenv   step2 : virtualenv ll_env或者python -m venv ll_env  PS:激活该虚拟环境 soruse env1/Script/activate    退出该虚拟环境：deactivate<br>
>>>|-- learming_log    	   #Django项目名称  #命令行: django-admin startproject learning_log<br>
>>>|>>>>>>|-- db.sqlite3<br>
>>>|>>>>>>|-- manage.py<br> 
>>>|>>>>>>|-- learning_log<br> 
>>>|>>>>>>>>>>>>|--__init__.py<br> 
>>>|>>>>>>>>>>>>|--__pycache__<br> 
>>>|>>>>>>>>>>>>|--settings.py     #在INSTALLED_APPS字段中配置自定义的APP<br> 
>>>|>>>>>>>>>>>>|--urls.py         #将url访问"引流"至自定义APP<br> 
>>>|>>>>>>>>>>>>|--wsgi.py<br> 
>>>|>>>>>>|--firstapp   	   #App1    #命令行: python manage.py startapp firstapp<br> 
>>>|>>>>>>>>>>>>|--admin.py<br> 
>>>|>>>>>>>>>>>>|--__init__.py<br> 
>>>|>>>>>>>>>>>>|--migrations<br> 
>>>|>>>>>>>>>>>>|--models.py<br> 
>>>|>>>>>>>>>>>>|--tests.py<br> 
>>>|>>>>>>>>>>>>|--view.py         #自定义的url处理函数<br> 
>>>|>>>>>>>>>>>>|--urls.py         #映射url->处理函数<br>
>>>|>>>>>>>>>>>>|--templates<br> 
>>>|>>>>>>>>>>>>>>>>>|--htmls<br>
>>>|>>>>>>>>>>>>>>>>>>>>|--index.html<br>
>>>|>>>>>>>>>>>>>>>>>>>>|--base.html<br>
>>>|>>>>>>>>>>>>>>>>>>>>|--topic.html<br>
>>>|>>>>>>>>>>>>>>>>>>>>|--topics.html<br>
>>>|>>>>>>|--secondapp  	   #App2    #命令行: python manage.py startapp firstapp<br>
>>>|>>>>>>>>>>>>|--admin.py<br>
>>>|>>>>>>>>>>>>|--__init__.py<br>
>>>|>>>>>>>>>>>>|--migrations<br>
>>>|>>>>>>>>>>>>|--models.py<br>
>>>|>>>>>>>>>>>>|--tests.py<br>
>>>|>>>>>>>>>>>>|--view.py<br>
>>>|>>>>>>>>>>>>|--urls.py<br>
>>>|>>>>>>>>>>>>|--templates<br>
>>>|>>>>>>>>>>>>>>>>>|--htmls<br>
>>>|>>>>>>>>>>>>>>>>>>>>|--index.html<br>
>>>|>>>>>>>>>>>>>>>>>>>>|--base.html<br>
>>>|>>>>>>>>>>>>>>>>>>>>|--topic.html<br> 
>>>|>>>>>>>>>>>>>>>>>>>>|--topics.html<br>
