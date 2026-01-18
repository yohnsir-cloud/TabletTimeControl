# 平板时间控制 - Android应用

一个真正的安卓应用，可以直接安装在华为平板上，控制使用时间，无需USB连接。

## 功能特点

- ⏰ **定时工作休息**：工作N分钟后自动休息N分钟
- 🔒 **自动锁屏**：休息时间自动锁屏，强制休息
- 📱 **独立运行**：无需USB连接，安装后独立运行
- 🎨 **简洁界面**：iOS风格设计，操作简单
- 📊 **实时显示**：状态栏实时显示剩余时间
- ⚙️ **灵活配置**：自定义工作/休息时长

## 使用方法

### 方法1：使用Android Studio编译（推荐）

#### 1. 安装Android Studio
下载并安装 [Android Studio](https://developer.android.com/studio)

#### 2. 打开项目
- 启动Android Studio
- 选择 "Open an Existing Project"
- 选择 `TabletTimeControl` 文件夹

#### 3. 同步项目
- 等待Gradle同步完成
- 如果提示下载SDK，点击下载

#### 4. 连接设备或创建模拟器
- **真实设备**：用USB连接平板，开启USB调试
- **模拟器**：在Android Studio中创建虚拟设备

#### 5. 运行应用
- 点击绿色三角按钮 ▶️
- 或按 `Shift + F10`

#### 6. 生成APK
- 菜单：Build → Build Bundle(s) / APK(s) → Build APK(s)
- APK位置：`app/build/outputs/apk/debug/app-debug.apk`

### 方法2：命令行编译

#### 1. 安装依赖
```bash
# 确保已安装JDK 8+
java -version

# 下载Android SDK Command-line Tools
# 下载地址：https://developer.android.com/studio#command-tools
```

#### 2. 设置环境变量
```bash
# Windows (在系统环境变量中添加)
ANDROID_HOME=C:\Users\你的用户名\AppData\Local\Android\Sdk
PATH=%PATH%;%ANDROID_HOME%\tools;%ANDROID_HOME%\platform-tools
```

#### 3. 编译APK
```bash
cd TabletTimeControl

# Windows
gradlew.bat assembleDebug

# Mac/Linux
./gradlew assembleDebug
```

生成的APK在：`app/build/outputs/apk/debug/app-debug.apk`

### 方法3：在线编译（最简单）

使用以下在线服务，只需上传代码即可生成APK：

1. [GitHub - actions](https://github.com/)（推荐）
   - 上传代码到GitHub
   - 在Actions中配置自动构建APK

2. [AppVeyor](https://www.appveyor.com/)
3. [CircleCI](https://circleci.com/)

## 安装到平板

### 1. 允许安装未知来源应用
在平板上：
- 打开【设置】→【安全和隐私】
- 开启【允许安装未知来源应用】

### 2. 传输APK到平板
方法：
- 通过USB复制
- 通过QQ/微信发送
- 通过云盘下载

### 3. 安装APK
- 在文件管理器中找到APK文件
- 点击安装
- 如提示警告，选择"继续安装"

## 首次使用设置

### 1. 开启无障碍权限（必须）
1. 打开应用
2. 点击【开启权限】按钮
3. 在无障碍设置中找到"平板时间控制"
4. 开启开关

### 2. 调整时长设置
- 拖动滑块调整工作时长（5-60分钟）
- 拖动滑块调整休息时长（5-30分钟）

### 3. 开始使用
- 点击【开始控制】按钮
- 应用会在后台运行
- 通知栏会显示当前状态

## 应用权限说明

| 权限 | 说明 | 必须性 |
|------|------|--------|
| 无障碍权限 | 用于锁屏和解锁操作 | ⚠️ 必须 |
| 前台服务 | 保持后台运行 | ⚠️ 必须 |
| 系统弹窗 | 显示锁定界面 | 可选 |
| 关闭屏幕锁 | 锁屏时使用 | 可选 |

## 工作流程

```
启动应用
    ↓
开启无障碍权限
    ↓
点击"开始控制"
    ↓
工作时段 (默认20分钟)
    ├─ 通知栏显示倒计时
    └─ 30秒前预警
    ↓
时间到 → 自动锁屏
    ↓
休息时段 (默认10分钟)
    ├─ 屏幕锁定
    └─ 通知栏显示剩余时间
    ↓
休息结束 → 自动解锁
    ↓
循环回到工作时段
```

## 常见问题

### Q: 应用没有自动锁屏
**A:**
1. 确认已开启无障碍权限
2. 在设置→应用管理中，关闭本应用的电池优化
3. 检查是否有其他锁屏应用冲突

### Q: 无法安装APK
**A:**
1. 检查"允许安装未知来源应用"是否开启
2. 卸载旧版本后再安装新版本
3. 检查平板系统版本（需要Android 7.0+）

### Q: 应用被系统杀死
**A:**
1. 设置 → 应用管理 → 平板时间控制 → 电池管理 → 关闭电池优化
2. 设置 → 应用启动管理 → 平板时间控制 → 设为"手动管理"
3. 在系统安全中心将本应用加入白名单

### Q: 编译失败
**A:**
1. 确保Android Studio版本最新
2. 检查网络连接（需要下载依赖）
3. 尝试清理：Build → Clean Project，然后 Rebuild Project

## 文件结构

```
TabletTimeControl/
├── app/
│   ├── src/
│   │   └── main/
│   │       ├── java/com/tablettimecontrol/
│   │       │   ├── MainActivity.kt           # 主界面
│   │       │   ├── ControlService.kt         # 控制服务
│   │       │   └── TabletAccessibilityService.kt  # 无障碍服务
│   │       ├── res/
│   │       │   ├── layout/
│   │       │   │   └── activity_main.xml     # 主界面布局
│   │       │   ├── values/
│   │       │   │   ├── colors.xml
│   │       │   │   └── strings.xml
│   │       │   ├── drawable/
│   │       │   │   └── ic_timer.xml          # 图标
│   │       │   └── xml/
│   │       │       └── accessibility_service_config.xml
│   │       └── AndroidManifest.xml
│   └── build.gradle
├── build.gradle
├── settings.gradle
└── gradle.properties
```

## 技术栈

- **语言**：Kotlin
- **最低SDK**：Android 7.0 (API 24)
- **目标SDK**：Android 14 (API 34)
- **架构**：Service + Accessibility Service
- **UI**：Material Design

## 注意事项

⚠️ **重要提示：**
- 本应用仅用于个人时间管理
- 锁屏功能需要无障碍权限
- 某些设备可能需要额外设置
- 建议配合平板自带的"屏幕使用时间"功能使用

## 更新日志

### v1.0 (2024-01-18)
- 🎉 首次发布
- ✨ 工作休息定时功能
- 🔒 自动锁屏功能
- 🎨 iOS风格界面

## 许可证

MIT License

---

**祝使用愉快！** 🎉
