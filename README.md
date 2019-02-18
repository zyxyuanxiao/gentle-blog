gentle-blog

采用 django2.0 + xadmin + mysql + 杨青个人模板《绅士》 打造的一款安全稳定的博客



# 开始

### 1. 安装（mysql 的安装这里不演示，mysql 的版本要>=4.5）

需要安装 python3.6 并通过 pip 安装 django 和 xadmin (见 1.1)

 ```
  pip install django-crispy-forms
  pip install django-formtools 
  pip install django-import-export
  pip install django-simple-captcha
  pip install django-pure-pagination
  pip install pillow
  pip install django
  pip install django-crispy-forms
  pip install django-import-export
  pip install django-reversion
  pip install django-formtools
  pip install future
  pip install httplib2
  pip install six
  pip install mysqlclient
 ```

#### 1.1 安装 xadmin

- ###### 下载 xadmin

  - git 用户

  `git clone https://github.com/sshwsfc/xadmin.git`

  如果有 ssh

  `git clone git@github.com:sshwsfc/xadmin.git`

  __克隆到本地之后需要打包成 zip__

  - 其他用户

  直接访问 https://github.com/sshwsfc/xadmin 下载

  ![1550461969086](C:\Users\JasonBanjui\AppData\Roaming\Typora\typora-user-images\1550461969086.png)

  ![1550461997891](C:\Users\JasonBanjui\AppData\Roaming\Typora\typora-user-images\1550461997891.png)

- ###### pip 安装 xadmin

  ​	  1. __确保文件在文件加下后，在地址栏上输入 cmd 打开 cmd__

  ![1550461582701](C:\Users\JasonBanjui\AppData\Roaming\Typora\typora-user-images\1550461582701.png)

  ​	  2. __命令行 pip 安装__

  ![1550461764735](C:\Users\JasonBanjui\AppData\Roaming\Typora\typora-user-images\1550461764735.png)

  代码 `pip install xadmin-django2.zip`

  看到 successful 就可以了

### 使用

在项目路径打开 cmd 输入以下命令

```
python manage makemigrations
python manage migrate
python manage createsuperuser
python manage runserver 8080
```

代码解释：

1. 检查数据表是否有更新
2. 生成数据表
3. 创建超级用户
4. 在 8080 端口运行服务
5. 输入完后通过URL __localhost:8080__ 访问

__如果中间有疑问的话请发送邮箱到 794130574@qq.com__



# 开发者文档

###	页面

- base 基础模板页面（导航栏 + 底部）

- index 首页
- article 文章页面
- list 文章类型 × 文章标签 × 关键字搜索
- comment 留言

### apps

- MainCoreApp 博客的重要部分
  1. model 表单设计
  2. adminx 注册后台表单
  3. url 路由
  4. form 设计表单验证
  5. views 业务逻辑
- CommonComment 留言模块



### 2.1 404 和 500 页面自定义

将 404 和 500 的页面替换 MainCoreApp 中 templates 文件夹中的 404 和 500 的 html

![1550463277665](C:\Users\JasonBanjui\AppData\Roaming\Typora\typora-user-images\1550463277665.png)



### 2.2 更换表单在后台显示的字段等自定义（建议配合 models.py 文件查看）

1. 只需要修改 MainCoreApp 中的 adminx 文件即可

一些常见的字段

```
list_display # 显示字段 （值：<list:字段>）
search_fields # 可以被查找的字段 （值：<list:字段>）
list_filter # 使用过滤器 （值：<list:字段>）
model_icon # 使用图标 样式是 font-awesome 的 （值：<str:样式>）
ordering # 排序 （字段前加 - 是倒序，比如 ['-name']） （值：<list:字段>）
readonly_fields # 设置只读字段（就是不可通过 xadmin 后台修改） （值：<list:字段>）
relfield_style # 一次性不会全部加载所有内容，比如说下拉框 （一般是 fk-ajax）
list_editable # 设置某些字段在表单列表中直接可以编辑 （值：<list:字段>）
refresh_times # 设置提供几秒刷新页面 （值：<list:秒数>）
```

2. 修改

比如是想修改 StromInfo 这个表单就在 xadmin.py 中找到 StromInfoAdmin 类

![1550463664784](C:\Users\JasonBanjui\AppData\Roaming\Typora\typora-user-images\1550463664784.png)

__改写其中的字段以及对应的值即可__



### 2.3  自定义后台全局设置（比如左上角的标题，底部的内容，是否开启主题功能）

只需要修改 MainCoreApp 中的 adminx 文件即可

__主要的是 BaseSetting 和 GlobalSettings __

```python
class BaseSetting(object):
    enable_themes = True # 开启主题功能
    use_bootswatch = True # 开启主题选择功能
    menu_style = 'accordion' # APP折叠
    
    
class GlobalSettings(object):
    site_title = "XXX管理系统" #改标题
    site_footer = "XXX网" # 底部版权
    menu_style = "accordion" # 收齐导航栏
```



未待完续....