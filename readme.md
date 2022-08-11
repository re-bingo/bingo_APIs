# 欢迎来到 **bingo API** 的主页😘

## about BINGO

> 近年来，我们高校学子，尤其是心理学及人文社科类专业的学生正越来越频繁地在朋友圈、微信群里发布有关问卷调查或实验招募的邀请信息，
> 为了招募到更多被试，主试方往往需要花费大量时间金钱成本，不遗余力地从自己的“人脉资源”里寻求支援，
> 这一现状促使我们产生了一个想法：搭建一个专门化的平台，在不改变现有被试招募生态的前提下，
> 将招募过程转移到一个更加公开透明且不受地域、人脉限制的平台上，让高校师生不再需要进行低效的社交管理和被试管理。BINGO为此而生。

以上内容节选自我们的立项答辩讲稿。在<https://cdn.muspimerol.site/ppt.html>能观看我们的答辩ppt(快放版)

## 关于该仓库

由于我们整个生产环境已经不再用python了，所以这个仓库只是保留作历史参考用途

这个DNS网址部署了该仓库的最新版本：[bingo.muspimerol.site](https://bingo.muspimerol.site/)

bingo开放平台的最新文档参考 [Apifox文档](https://bingo.muspimerol.site/apifox)

🎉 2022年8月9日，我们的[全新官网](https://cdn.muspimerol.site/bingo.html)上线啦：
[bingo.muspimerol.site/index.html](https://bingo.muspimerol.site/index.html)

---

**该`readme.md`在[仓库页面](https://github.com/CNSeniorious000/bingo_APIs)
和网站首页保持同步（通过[`Jinja2`模板引擎](https://doc.yonyoucloud.com/doc/jinja2-docs-cn/index.html)）**

而有的链接是相对链接，因此在仓库页面访问不了，只能在我们接口文档跳转。

![cover](https://cos.muspimerol.site/bingo_webplus_ppt_cover.png)

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
> 负责Java后端的新大佬是谁呢👀（见网页头）
>
> ■

## 以下是**最近一次(最后一次)更新**的日志

#### 可以注意一下的

- 克隆下本仓库必须补齐`secret.py`才能用
- 最好每次都访问这个页面都刷新一遍[`css`](https://bingo.muspimerol.site/default.css)
- 新增：[根据`ID`删除用户](https://bingo.muspimerol.site/docs#/users/cancel_user_by_id_users_cancellation__id__get)
  ，即允许**注销用户**
- [获取全部量表的接口](https://bingo.muspimerol.site/docs#/scales/get_titles_scales__get)由`/scales`变成`/scales/`
  了（为了一些一致性）
- 搜索页面为`/scales/html`而不是`/scales/html/`，后者不能正常访问

#### 近期未完成

- **时间有限**，排序和搜索的实现仍欠优化
- 没有连数据库

#### 娱乐性的更新

- [x] **支持[直接html搜索量表](https://bingo.muspimerol.site/scales/html)**
- [ ] 可见的未来准备做几个debug用的页面，比如格式化展示`users`或者`items`

