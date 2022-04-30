# API and backend of Bingo!

欢迎来到 bingo API 的文档
**该`readme.md`在仓库页面和网站首页保持同步（通过`Jinja2`模板引擎）**

> 服务器上不知道为什么`python3.10`的`ssl`模块会报错，所以只好兼容到3.9了
> 
>**以下为近期的更新**

---

#### 破坏性地，有

- `Item`中时间戳域由`time_stamp`改名为`timestamp`了
- `User`下所有`API`都遭遇了大改

#### 近期未完成

- **时间有限**，排序和搜索的实现仍欠优化
- 还没有连接**数据库**
- 首页的`readme.md`并没有展示出所有`markdown`特性

#### 娱乐更新

- [x] **大改了主页，现在的`home.html`是一个实时渲染的`Jinja2`模板了**
- [ ] 可见的未来准备给`scales`页面也做一个`template`，让用户可以直接查看量表
- [ ] 可见的未来准备做几个debug用的页面，比如格式化展示`users`或者`items`