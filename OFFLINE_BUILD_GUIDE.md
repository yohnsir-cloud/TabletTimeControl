# 无需 Android Studio 的编译方法

由于无法访问 Google 服务，这里提供几种替代方案：

## 方案1：使用 GitHub 在线编译（推荐，完全免费）

### 步骤：

1. **注册 GitHub 账号**（如果没有）
   - 访问：https://github.com
   - 点击 Sign up 注册

2. **创建新仓库**
   - 点击右上角 "+" → "New repository"
   - 仓库名：`TabletTimeControl`
   - 设为 Public
   - 点击 "Create repository"

3. **上传代码**
   - 点击 "uploading an existing file"
   - 把整个 `TabletTimeControl` 文件夹内的所有文件拖进去
   - 点击 "Commit changes"

4. **启用 GitHub Actions**
   - 进入仓库
   - 点击 "Actions" 标签
   - 选择左侧 "Build Android APK"
   - 点击 "Run workflow" → "Run workflow"

5. **下载 APK**
   - 等待几分钟构建完成
   - 点击构建任务进入详情页
   - 滚动到底部 "Artifacts"
   - 下载 `app-debug` 压缩包
   - 解压后得到 `app-debug.apk`

---

## 方案2：使用国内在线编译平台

### A. 葵花码（免费）
- 网址：https://www.kaihuacode.com
- 注册账号后上传代码即可编译

### B. ApkToolBox（简单易用）
- 网址：https://www.apktoolbox.com
- 上传源码自动生成 APK

### C. Coding持续集成（国内推荐）
- 网址：https://coding.net
- 类似 GitHub，但服务器在国内
- 创建项目后启用构建功能

---

## 方案3：使用命令行工具（需要手动下载）

### 1. 下载 Android SDK 命令行工具

从国内镜像下载：
- 清华镜像：https://mirrors.tuna.tsinghua.edu.cn/android/repository/
- 下载：`commandlinetools-win-xxxx_latest.zip`

### 2. 解压并配置环境变量

```batch
# 设置环境变量
set ANDROID_HOME=C:\android-sdk
set PATH=%PATH%;%ANDROID_HOME%\cmdline-tools\latest\bin;%ANDROID_HOME%\platform-tools

# 接受许可
sdkmanager --licenses
```

### 3. 安装必要组件

```batch
sdkmanager "platform-tools" "platforms;android-34" "build-tools;34.0.0"
```

### 4. 编译 APK

```batch
cd TabletTimeControl
gradlew.bat assembleDebug
```

---

## 方案4：使用虚拟机（高级用户）

1. 下载 Android-x86 虚拟机
2. 在虚拟机内安装 Android Studio
3. 编译后导出 APK

---

## 推荐流程

**最简单的方式：**

1. 使用 **GitHub** + **GitHub Actions**（方案1）
2. 或使用 **Coding.net**（方案3-C，国内更快）

**预计时间：**
- GitHub：10-15 分钟（首次注册和上传）
- Coding：5-10 分钟

---

## APK 编译完成后

### 安装到平板：

1. **传输 APK 到平板**
   - 方法1：通过 QQ/微信文件传输助手
   - 方法2：通过百度网盘/阿里云盘
   - 方法3：通过 USB 直接复制

2. **安装应用**
   - 在平板上找到 APK 文件
   - 点击安装
   - 允许"未知来源应用"安装

3. **开启权限**
   - 打开应用
   - 点击"开启权限"
   - 在无障碍设置中开启本应用

4. **开始使用**
   - 设置工作/休息时长
   - 点击"开始控制"

---

## 需要帮助？

如果遇到问题，可以告诉我：
- 你选择了哪个方案
- 在哪一步遇到了困难
- 具体的错误信息

我会继续帮你解决！
