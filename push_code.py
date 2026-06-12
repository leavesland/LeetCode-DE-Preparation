import os
import sys
import subprocess

try:
    import pyperclip
except ImportError:
    print("❌ 请先在终端运行: pip install pyperclip")
    sys.exit(1)

def auto_pipeline():
    # 1. 让你输入题号和题目名字
    print("=== 🚀 LeetCode 自动化打卡神器 ===")
    prob_no = input("请输入题号 (例如 128): ").strip()
    prob_name = input("请输入题目英文名 (例如 longest_consecutive_sequence): ").strip().lower().replace(" ", "_")
    lang = input("请输入语言 (py 或 sql): ").strip().lower()

    if lang not in ['py', 'sql']:
        print("❌ 语言目前只支持 py 或 sql")
        return

    # 2. 自动决定分类文件夹
    folder = "Algorithms" if lang == "py" else "SQL"
    if not os.path.exists(folder):
        os.makedirs(folder)

    # 3. 自动生成标准文件名
    file_name = f"{prob_no}_{prob_name}.{lang}"
    file_path = os.path.join(folder, file_name)

    # 4. 自动从你的电脑剪贴板里抓取你刚复制的 LeetCode 代码
    code_content = pyperclip.paste()
    if not code_content.strip():
        print("❌ 你的剪贴板是空的，请先去 LeetCode 复制你的完美代码！")
        return

    # 5. 自动写进文件
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(code_content)
    print(f"📂 [成功] 已自动创建并写入: {file_path}")

    # 6. 自动化 Git 连招（在 Python 里调用终端命令）
    print("📦 开始自动同步到 GitHub...")
    try:
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", f"feat: add problem {prob_no} solution"], check=True)
        subprocess.run(["git", "push"], check=True)
        print("🎉 [大功告成] 代码已成功轰炸到 GitHub，绿格子已亮起！")
    except subprocess.CalledProcessError as e:
        print(f"❌ Git 操作失败，请检查网络或是否配置过 remote: {e}")

if __name__ == "__main__":
    auto_pipeline()