# ThePainter 项目开发笔记

## 设计步骤

1. 明确工具使用方法
2. 设计指令
3. 实现 parser
4. 实现 drawer

---

## 功能开发记录

1. 明确点击位置
2. 实现图层相关功能
3. 等待后续验证

---

## 个人感想

> earlier

高估了 deepseek 的能力，本来希望 deepseek 生成的指令能画图，结果简笔画都画得不是很好。
但是 `document/others/painting.html` 又显示其具有一定能力。

也许可以训练一个专用的大语言模型来生成指令，通过按步骤生成来绘图？

> 2025年7月6日 13点38分

像写一个项目一样，我设计，deepseek 实现，我再微调。最终也是把 [/output/Sample-2.png](/output/Sample-2.png) 弄出来了