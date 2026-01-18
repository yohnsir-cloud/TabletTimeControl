# Android Studio 编译指南

## 详细步骤

### 第一步：安装 Android Studio

1. 下载 Android Studio
   - 官网：https://developer.android.com/studio
   - 选择 Windows 版本下载

2. 安装 Android Studio
   - 运行下载的安装程序
   - 使用默认设置安装
   - 安装过程需要下载约 1GB 的组件，请耐心等待

3. 首次启动配置
   - 选择 "Standard" 标准安装
   - 等待 SDK 和组件下载完成

### 第二步：打开项目

1. 启动 Android Studio

2. 选择 "Open"
   - 或者：File → Open

3. 浏览到项目文件夹
   - 选择：`C:\Users\A\小工具合计\TabletTimeControl`
   - 点击 "OK"

4. 等待项目加载
   - Android Studio 会自动下载 Gradle 和依赖
   - 第一次打开可能需要 5-10 分钟
   - 底部状态栏显示 "Gradle Build Running..."

### 第三步：解决可能的错误

#### 错误 1：SDK 版本问题
如果提示 "SDK not found"：
```
解决方案：
1. 点击 SDK Manager 图标（或：Tools → SDK Manager）
2. 确保安装了：
   - Android 14.0 (API 34)
   - Android SDK Build-Tools 34.0.0
3. 点击 "Apply" 下载
```

#### 错误 2：Gradle 同步失败
```
解决方案：
1. File → Invalidate Caches / Restart
2. 点击 "Invalidate and Restart"
3. 重启后再次同步
```

#### 错误 3：JDK 版本问题
```
解决方案：
1. File → Project Structure
2. SDK Location
3. JDK location：选择 Android Studio 自带的 JDK
   通常在：C:\Users\你的用户名\AppData\Local\Android\Sdk\jbr
```

### 第四步：创建模拟器或连接真机

#### 方法 A：使用模拟器（推荐用于测试）

1. 打开 Device Manager
   - 工具栏点击 Device Manager 图标
   - 或：Tools → Device Manager

2. 创建新设备
   - 点击 "Create Device"
   - 选择设备类型：Tablet
   - 选择型号：Pixel Tablet 或其他
   - 选择系统镜像：API 34 (Android 14)
   - 如果没有，需要下载（约 1GB）

3. 启动模拟器
   - 点击设备旁的播放按钮 ▶️

#### 方法 B：使用真机（平板）

1. 在平板上开启开发者选项
   - 设置 → 关于平板
   - 连续点击 "版本号" 7 次

2. 开启 USB 调试
   - 设置 → 系统和更新 → 开发者选项
   - 开启 "USB 调试"

3. 用 USB 线连接平板到电脑

4. 在平板上授权
   - 弹出 "允许 USB 调试" 时点击 "确定"

5. 在 Android Studio 中查看
   - 顶部设备选择下拉框会显示你的设备

### 第五步：运行应用

1. 选择运行设备
   - 顶部工具栏选择设备（模拟器或真机）

2. 点击运行按钮
   - 绿色三角 ▶️
   - 或按 Shift + F10

3. 等待安装
   - 应用会自动编译并安装到设备
   - 首次编译可能需要几分钟

4. 应用自动启动
   - 安装完成后应用会在设备上打开

### 第六步：生成 APK 文件

如果你想分享 APK 给其他人：

1. 菜单操作
   ```
   Build → Build Bundle(s) / APK(s) → Build APK(s)
   ```

2. 等待编译完成
   - 右下角弹出通知时点击 "locate"

3. 找到 APK 文件
   ```
   位置：
   TabletTimeControl\app\build\outputs\apk\debug\app-debug.apk
   ```

4. 传输到平板
   - 复制 APK 到平板
   - 或通过 QQ/微信发送
   - 在平板上安装并开启无障碍权限

## 快速检查清单

编译前检查：
- [ ] Android Studio 已安装
- [ ] 项目已成功打开
- [ ] Gradle 同步成功（无红色错误）
- [ ] 已选择运行设备
- [ ] 无障碍权限配置文件存在

## 常见错误及解决方案

### 1. "Failed to resolve: androidx"
**解决方案**：等待 Gradle 完全同步完成

### 2. "SDK Build Tools revision not found"
**解决方案**：SDK Manager → SDK Tools → 勾选 "Show Package Details" → 安装 Build Tools 34.0.0

### 3. "Plugin [id: 'com.android.application'] was not found"
**解决方案**：检查网络连接，确保能访问 Google 服务

### 4. 编译成功但无法安装到真机
**解决方案**：
- 检查 USB 线是否连接
- 重启 Android Studio
- 在平板上重新授权 USB 调试

### 5. 应用打开后闪退
**解决方案**：
- 查看 Logcat 窗口的错误信息
- 确认已授予存储权限
- 清理应用数据后重试

## 编译成功后如何使用

1. 首次打开应用
2. 点击"开启权限"
3. 在无障碍设置中开启"平板时间控制"
4. 调整工作/休息时长
5. 点击"开始控制"
6. 应用会在后台运行，通知栏显示状态

## 需要帮助？

如果遇到问题，请提供：
1. Android Studio 版本
2. 完整的错误信息（截图更好）
3. Gradle 同步状态

---

**预计时间**：首次安装和编译需要 30-60 分钟（主要是下载组件）
**后续编译**：只需要 2-5 分钟
