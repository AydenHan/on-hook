# on-hook
A script app for Yys (private).

<font color="red">**仅用于学习。**</font>

![主界面](.\sample\2-1.png)![主界面](.\sample\2-2.png)![主界面](.\sample\2-3.png)

嗯，主界面如上图所示，挂在客户端的左上角，面积很小，然后改了改UI，看上去还行哈哈。

设计的灵感来自于炉石的HDT插件（看胜率那个），也是悬挂在炉石界面的顶部，看上去轻便美观，一目了然。

**第二块**用于显示挂机成功的轮数，简洁明了~停止后再次开始就会重新计数。

**第三块**是控制开始结束的按钮，主要绑定了三个事件：1.按钮图标的变化；2.挂机线程的启动/停止；3.时间统计框的弹出/落下，如下图所示。

![动态1](.\sample\gif1.gif)

**第一块**用于打开设置选项，如上图所示。选项中包含挂机方案的选择、创建桌面快捷方式和关闭程序的按钮。如下所示。

![动态2](.\sample\gif2.gif)

挂机方案是内置好了的，写死了用于识别的相应图片。



