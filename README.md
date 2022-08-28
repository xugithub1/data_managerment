# 数据组成

```
projects
├── baidu
│   └── train
├── gac
│   ├── mining
│   └── train
├── mining
└── pilot
    └── train
```

# 配置git-lfs
[**Lustre**]

```bash
# 确认git-lfs安装版本
git lfs env
# 设置 git-lfs url
git config --global lfs.url "http://lfs.sensetime.com/"
# 设置自动保存username和password
git config --global credential.helper store
```

* ! git-lfs的密码不是AD密码，需要从这里获取：https://lfs.sensetime.com

[**Desktop**]

git version > 1.8.5

[下载 git-lfs](https://git-lfs.github.com/) 

```bash
tar -xzvf git-lfs-linux-amd64-v3.2.0.tar.gz
cd git-lfs-3.2.0
bash install.sh
# 确认git版本
git lfs version
```

# 如何使用


```bash
cd tools
# 生成没有重复的json
python merge_file.py unique
# 生成有mining结果的训练json
python merge_file.py repeat
```

* 你可以修改final.txt和merge_file.py来配置你想要的任何组合方式.

# 其他

* **如何更新.gitignore**

* ```bash
  # change .gitignore file, like add *.json in this file, than
  git rm -r --cached .
  git add .
  git commit -m 'update .gitignore'
  git push xxx
  ```

  

