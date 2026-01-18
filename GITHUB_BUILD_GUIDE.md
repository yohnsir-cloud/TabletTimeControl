# GitHub 在线编译详细步骤

## 📋 完整操作流程

### 第一步：注册 GitHub 账号（如果没有）

1. 访问：https://github.com
2. 点击右上角 **"Sign up"**
3. 填写信息：
   - Username: 用户名
   - Email: 邮箱地址
   - Password: 密码
4. 验证邮箱
5. 完成注册

### 第二步：创建新仓库

1. 登录 GitHub 后，点击右上角 **"+"** → **"New repository"**
2. 填写仓库信息：
   - **Repository name**: `TabletTimeControl`
   - **Description**: 华为平板时间控制应用
   - 选择 **Public**（公开）
3. 点击 **"Create repository"**

### 第三步：上传代码

#### 方法 A：网页上传（最简单）

1. 在新创建的仓库页面，点击 **"uploading an existing file"**
2. 打开文件夹：`C:\Users\A\小工具合计\TabletTimeControl`
3. 把所有文件和文件夹拖到 GitHub 上传区域
4. 等待上传完成
5. 滚动到底部，填写提交信息：
   - "Upload files"
6. 点击 **"Commit changes"**

#### 方法 B：使用 Git 命令（如果熟悉 Git）

```batch
cd C:\Users\A\小工具合计
git init
git add TabletTimeControl/*
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/你的用户名/TabletTimeControl.git
git push -u origin main
```

### 第四步：启用 GitHub Actions

1. 在仓库页面，点击顶部的 **"Actions"** 标签
2. 如果提示启用 Workflows，点击 **"I understand my workflows, go ahead and enable them"**
3. 在左侧会看到 **"Build Android APK"**
4. 点击进入
5. 点击右侧 **"Run workflow"** 按钮
6. 确认运行，点击绿色的 **"Run workflow"**

### 第五步：等待编译

1. 页面会显示 "Build Android APK" 正在运行
2. 等待约 **3-5 分钟**
3. 状态变为 ✓ 绿色勾表示完成

### 第六步：下载 APK

1. 点击完成的构建任务
2. 滚动到页面最底部 **"Artifacts"** 部分
3. 点击 **"app-debug"** 下载
4. 下载的是一个 `.zip` 压缩包
5. 解压后得到 **"app-debug.apk"**

### 第七步：安装到平板

1. **传输 APK 到平板**：
   - 方法1：通过 QQ/微信文件传输助手
   - 方法2：通过百度网盘/阿里云盘
   - 方法3：USB 复制

2. **在平板上安装**：
   - 找到 APK 文件
   - 点击安装
   - 如提示"未知来源"，去设置里允许安装

3. **开启权限**：
   - 打开应用
   - 点击"开启权限"
   - 在无障碍设置里找到并开启"平板时间控制"

4. **开始使用**：
   - 设置工作/休息时长
   - 点击"开始控制"

---

## 🔧 可能遇到的问题

### 问题1：找不到 "Actions" 标签
**解决**：Actions 可能需要几分钟后才出现，刷新页面重试

### 问题2：Actions 编译失败
**解决**：查看失败原因，通常是 Gradle 配置问题，我已经配置好了阿里云镜像

### 问题3：下载的 APK 无法安装
**解决**：
- 去设置 → 允许安装未知来源应用
- 或卸载旧版本后重新安装

---

## ⏱️ 预计时间

| 步骤 | 时间 |
|------|------|
| 注册 GitHub | 3 分钟 |
| 上传代码 | 5 分钟 |
| 在线编译 | 3-5 分钟 |
| 下载安装 | 2 分钟 |
| **总计** | **约 15 分钟** |

---

## 📱 安装后使用

1. 打开应用，看到简洁的控制界面
2. 拖动滑块设置：
   - 工作时长：默认 20 分钟
   - 休息时长：默认 10 分钟
3. 点击"开启权限"，在无障碍设置里开启
4. 点击"开始控制"
5. 应用会在后台运行，通知栏显示倒计时

---

## 🎯 开始吧！

现在可以：
1. 打开 https://github.com
2. 创建新仓库
3. 上传代码
4. 几分钟后就能下载 APK

有问题随时告诉我！
