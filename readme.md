![cover](http://175.178.204.205:7777/static/cover.png)

# 欢迎来到 **bingo API** 的主页😘

###### 查看我们的接口文档：[https://sehnsucht.top/](http://175.178.204.205:8000/)

---

**该`readme.md`在[仓库页面](https://github.com/CNSeniorious000/bingo_APIs)和网站首页保持同步（通过[`Jinja2`模板引擎](http://doc.yonyoucloud.com/doc/jinja2-docs-cn/index.html)）**

而有的链接是相对链接，因此在仓库页面访问不了，只能在我们接口文档跳转。

> **2022年5月16日**
> 
> 由于对接数据库、人员调整等因素，我们决定用Java重构Bingo的后端
>
> 在所有接口均被Java实现后，这个仓库将迎来寿终正寝
>
> 接下来本项目将由 **`@hexWars`([GitHub](https://github.com/hexWars)/[gitee](https://gitee.com/hex-cxm))** 负责
>
> 那时，这个页面也会正式下线，为Bingo迎来Java的曙光让开道路
>
> **从今往后，本python项目将不再有功能更新~**
>
> 负责Java后端的新大佬是谁呢👀（见网页尾）
>
> ■

## 以下是**最近一次(最后一次)更新**的日志

#### 可以注意一下的

- 克隆下本仓库必须补齐`secret.py`才能用
- 最好每次都访问这个页面都刷新一遍[`css`](/default.css)
- 新增：[根据`ID`删除用户](/docs#/users/cancel_user_by_id_users_cancellation__id__get)，即允许**注销用户**
- [获取全部量表的接口](/docs#/scales/get_titles_scales__get)由`/scales`变成`/scales/`了（为了一些一致性）
- 搜索页面为`/scales/html`而不是`/scales/html/`，后者不能正常访问

#### 近期未完成

- **时间有限**，排序和搜索的实现仍欠优化
- 没有连数据库

#### 娱乐性的更新

- [x] **支持[直接html搜索量表](/scales/html)**
- [ ] 可见的未来准备做几个debug用的页面，比如格式化展示`users`或者`items`
