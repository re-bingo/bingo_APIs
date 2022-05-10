# 欢迎来到 **bingo API** 的文档😘

###### 访问我们的网页：[https://sehnsucht.top/](https://sehnsucht.top/)

---

**该`readme.md`在[仓库页面](https://github.com/CNSeniorious000/bingo_APIs)和网站首页保持同步（通过[`Jinja2`模板引擎](http://doc.yonyoucloud.com/doc/jinja2-docs-cn/index.html)）**

## 以下为近期的更新

#### 可以注意一下的

- 新增：[根据`ID`删除用户](/docs#/users/cancel_user_by_id_users_cancellation__id__get)，即允许**注销用户**
- [获取全部量表的接口](/docs#/scales/get_titles_scales__get)由`/scales`变成`/scales/`了（为了一些一致性）
- 搜索页面为`/scales/html`而不是`/scales/html/`，后者不能正常访问

#### 近期未完成

- 首页的`readme.md`并没有展示出所有`markdown`特性，[css](/default.css)也没有针对**quote block**进行优化
- **时间有限**，排序和搜索的实现仍欠优化

#### 娱乐更新

- [x] **支持[直接html搜索量表](/scales/html)**
- [ ] 可见的未来准备做几个debug用的页面，比如格式化展示`users`或者`items`