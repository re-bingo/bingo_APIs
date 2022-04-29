# API and backend of Bingo!

> 欢迎来到 bingo API 的文档
>
> 因为openssl的缘故没法支持python3.10,
> 因此代码可能并不是最简
>
> 以下是更新计划

---

#### 最近一次更新，破坏性的功能有：

- **时间戳域由`time_stamp`改名为`timestamp`了**
- 改`user`为`author`

#### 近期重要更新：

- [x] 需要让`post`请求返回新建对象的`id`
- [ ] 需要实现排序和搜索`Item`的接口

#### 近期纯娱乐更新：

- [ ] 尝试重写主页，使得主页直接呈现该`readme.md`
    - [ ] 可能直接用字符串拼接实现，也可能可以用上`Jinja2`