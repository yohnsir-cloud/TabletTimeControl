#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
华为平板时间控制程序
通过ADB控制平板使用时间，实现定时休息提醒和强制锁屏
"""

import subprocess
import time
import threading
from datetime import datetime, timedelta
from pathlib import Path
import json
import sys

class TabletController:
    def __init__(self, config_file="config.json"):
        """初始化平板控制器"""
        self.config_file = config_file
        self.config = self.load_config()
        self.running = False
        self.monitor_thread = None
        self.rest_thread = None
        self.current_session_start = None
        self.total_rest_time = 0

        print("=" * 60)
        print("华为平板时间控制程序")
        print("=" * 60)

    def load_config(self):
        """加载配置文件"""
        default_config = {
            "work_duration": 20,  # 工作时长（分钟）
            "rest_duration": 10,  # 休息时长（分钟）
            "warning_time": 30,   # 休息前警告时间（秒）
            "daily_limit": 180,   # 每日总时长限制（分钟）可选
            "enable_daily_limit": False,
            "device_id": None     # 指定设备ID（多设备时使用）
        }

        config_path = Path(self.config_file)
        if config_path.exists():
            try:
                with open(config_path, 'r', encoding='utf-8') as f:
                    user_config = json.load(f)
                    default_config.update(user_config)
            except Exception as e:
                print(f"⚠️  配置文件读取失败，使用默认配置: {e}")
        else:
            self.save_config(default_config)
            print(f"✅ 已创建默认配置文件: {self.config_file}")

        return default_config

    def save_config(self, config=None):
        """保存配置文件"""
        if config is None:
            config = self.config
        try:
            with open(self.config_file, 'w', encoding='utf-8') as f:
                json.dump(config, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"⚠️  配置文件保存失败: {e}")

    def check_adb_connection(self):
        """检查ADB连接"""
        try:
            result = subprocess.run(
                ['adb', 'devices'],
                capture_output=True,
                text=True,
                encoding='utf-8',
                timeout=5
            )
            devices = []
            for line in result.stdout.strip().split('\n')[1:]:
                if '\tdevice' in line:
                    device_id = line.split('\t')[0]
                    devices.append(device_id)

            if not devices:
                print("❌ 未检测到连接的设备")
                print("请确保：")
                print("  1. 平板已通过USB连接到电脑")
                print("  2. 平板已开启USB调试模式")
                print("  3. 已在平板上授权此电脑进行USB调试")
                return False

            if len(devices) == 1:
                self.config['device_id'] = devices[0]
                print(f"✅ 检测到设备: {devices[0]}")
            else:
                if self.config.get('device_id') and self.config['device_id'] in devices:
                    print(f"✅ 使用指定设备: {self.config['device_id']}")
                else:
                    print(f"⚠️  检测到多个设备: {', '.join(devices)}")
                    print("请在配置文件中指定 device_id")
                    return False

            return True

        except FileNotFoundError:
            print("❌ 未找到ADB命令")
            print("请确保已安装Android SDK Platform-tools")
            print("下载地址: https://developer.android.com/studio/releases/platform-tools")
            return False
        except Exception as e:
            print(f"❌ ADB连接检查失败: {e}")
            return False

    def execute_adb_command(self, command):
        """执行ADB命令"""
        try:
            full_command = ['adb']
            if self.config.get('device_id'):
                full_command.extend(['-s', self.config['device_id']])
            full_command.extend(command)

            result = subprocess.run(
                full_command,
                capture_output=True,
                text=True,
                encoding='utf-8',
                timeout=10
            )
            return result.returncode == 0
        except Exception as e:
            print(f"⚠️  ADB命令执行失败: {e}")
            return False

    def lock_screen(self):
        """强制锁屏"""
        print(f"\n🔒 [{datetime.now().strftime('%H:%M:%S')}] 正在锁屏...")
        # 使用各种方法尝试锁屏
        methods = [
            ['shell', 'input', 'keyevent', 'KEYCODE_POWER'],  # 电源键
            ['shell', 'input', 'keyevent', '26'],              # 电源键备用
        ]

        for method in methods:
            if self.execute_adb_command(method):
                print("✅ 锁屏成功")
                return True

        print("❌ 锁屏失败")
        return False

    def turn_off_screen(self):
        """关闭屏幕"""
        # 先按电源键确保屏幕关闭
        self.execute_adb_command(['shell', 'input', 'keyevent', 'KEYCODE_POWER'])
        time.sleep(1)
        # 再按一次确保熄屏
        self.execute_adb_command(['shell', 'input', 'keyevent', 'KEYCODE_POWER'])

    def show_rest_notification(self, remaining_seconds):
        """在平板上显示休息提醒"""
        message = f"休息时间: {remaining_seconds//60}分{remaining_seconds%60}秒"
        try:
            # 尝试显示Toast通知
            cmd = [
                'shell', 'am', 'start', '-a', 'android.intent.action.MAIN',
                '-e', 'message', message
            ]
            self.execute_adb_command(cmd)
        except:
            pass

    def work_session(self):
        """工作会话"""
        work_minutes = self.config['work_duration']
        warning_seconds = self.config['warning_time']

        print(f"\n📱 [{datetime.now().strftime('%H:%M:%S')}] 开始工作时段")
        print(f"⏱️  工作时长: {work_minutes} 分钟")
        print(f"⏰  将在 {work_minutes} 分钟后强制锁屏休息")

        self.current_session_start = datetime.now()

        # 计算总秒数
        total_seconds = work_minutes * 60

        # 倒计时显示
        for remaining in range(total_seconds, 0, -1):
            if not self.running:
                return False

            # 显示倒计时
            if remaining % 60 == 0 or remaining <= warning_seconds:
                mins = remaining // 60
                secs = remaining % 60
                print(f"\r⏳ 剩余时间: {mins:2d}分{secs:2d}秒", end='', flush=True)

                # 最后warning_time秒显示警告
                if remaining == warning_seconds:
                    print(f"\n⚠️  注意：{warning_seconds}秒后即将锁屏休息！")
                    # 可以添加声音提醒
                    # self.play_warning_sound()

            time.sleep(1)

        print()  # 换行
        return True

    def rest_session(self):
        """休息会话"""
        rest_minutes = self.config['rest_duration']

        print(f"\n💤 [{datetime.now().strftime('%H:%M:%S')}] 开始休息时段")
        print(f"⏱️  休息时长: {rest_minutes} 分钟")

        # 强制锁屏
        self.lock_screen()
        self.turn_off_screen()

        total_seconds = rest_minutes * 60

        # 休息倒计时
        for remaining in range(total_seconds, 0, -1):
            if not self.running:
                return False

            # 每分钟显示一次剩余时间
            if remaining % 60 == 0:
                mins = remaining // 60
                print(f"😴 休息中... 剩余 {mins} 分钟")

            time.sleep(1)

        # 休息结束，唤醒用户
        print(f"\n☀️ [{datetime.now().strftime('%H:%M:%S')}] 休息结束！")

        # 尝试唤醒屏幕
        self.execute_adb_command(['shell', 'input', 'keyevent', 'KEYCODE_WAKEUP'])

        return True

    def start(self):
        """启动控制程序"""
        if not self.check_adb_connection():
            return False

        self.running = True

        print("\n" + "=" * 60)
        print("控制程序已启动")
        print(f"⏰ 工作时长: {self.config['work_duration']} 分钟")
        print(f"😴 休息时长: {self.config['rest_duration']} 分钟")
        print("=" * 60)
        print("\n按 Ctrl+C 停止程序\n")

        try:
            while self.running:
                # 工作时段
                if self.work_session():
                    # 休息时段
                    if not self.rest_session():
                        break
                else:
                    break

        except KeyboardInterrupt:
            print("\n\n⏸️  程序已停止")
        finally:
            self.stop()

        return True

    def stop(self):
        """停止控制程序"""
        self.running = False
        print("👋 再见！")

    def get_stats(self):
        """获取统计信息"""
        if self.current_session_start:
            elapsed = datetime.now() - self.current_session_start
            print(f"本次会话已运行: {elapsed}")
        print(f"总休息时间: {self.total_rest_time} 分钟")


def main():
    """主函数"""
    print("\n" + "="*60)
    print(" " * 15 + "华为平板时间控制程序")
    print("=" * 60)
    print()

    controller = TabletController()

    # 显示菜单
    while True:
        print("\n请选择操作:")
        print("1. 启动时间控制")
        print("2. 修改配置")
        print("3. 查看当前配置")
        print("4. 测试ADB连接")
        print("5. 退出")

        choice = input("\n请输入选项 (1-5): ").strip()

        if choice == '1':
            controller.start()
        elif choice == '2':
            print("\n当前配置:")
            print(f"1. 工作时长: {controller.config['work_duration']} 分钟")
            print(f"2. 休息时长: {controller.config['rest_duration']} 分钟")
            print(f"3. 预警时间: {controller.config['warning_time']} 秒")

            try:
                work = int(input("\n输入工作时长(分钟): "))
                rest = int(input("输入休息时长(分钟): "))
                warning = int(input("输入预警时间(秒): "))

                controller.config['work_duration'] = max(1, work)
                controller.config['rest_duration'] = max(1, rest)
                controller.config['warning_time'] = max(5, warning)

                controller.save_config()
                print("\n✅ 配置已保存")
            except ValueError:
                print("\n❌ 输入无效，请输入数字")

        elif choice == '3':
            print("\n当前配置:")
            for key, value in controller.config.items():
                print(f"  {key}: {value}")

        elif choice == '4':
            controller.check_adb_connection()

        elif choice == '5':
            print("\n再见！")
            break

        else:
            print("\n❌ 无效选项，请重新选择")


if __name__ == "__main__":
    main()
