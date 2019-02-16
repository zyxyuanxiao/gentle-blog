# gentle-blog
采用 django2.0 + xadmin + mysql + 杨青个人模板《绅士》 打造的一款安全稳定的博客



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