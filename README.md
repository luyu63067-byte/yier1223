# Python Demo：CSV 数据读取练习
这是我学习GitHub的第一个练习项目。
这个个人练习项目用于学习：编写 Python、使用 Git 保存版本，以及将代码备份到 GitHub。

## 运行

需要 Python 3.9 或更新版本；不需要安装第三方库。

```powershell
python main.py
```

默认读取 `data/sample.csv`，显示商品数量、订单数量和销售额。也可以指定自己的 CSV：

```powershell
python main.py "你的文件.csv"
```

CSV 必须包含 `product`、`quantity`、`unit_price` 三列。示例数据是虚构数据。

## 日常提交

在本项目目录打开 PowerShell：

```powershell
git status
git add .
git diff --cached
git commit -m "修改：描述这次做了什么"
git push
```

`commit` 保存到电脑，`push` 才上传到 GitHub。只有推送过的版本才能从另一台电脑恢复。

如果在 GitHub 网页或另一台电脑改过代码，先保存本地改动，再执行 `git pull --rebase`。

## 文件说明

- `main.py`：读取 CSV 并汇总销售额。
- `data/sample.csv`：虚构练习数据。
- `.gitignore`：忽略虚拟环境、缓存和本地密钥。

不要提交真实密码、API Key、Cookie 或个人敏感数据。
