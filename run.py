import streamlit.web.cli as stcli
import os, sys
 
 
# def resolve_path(path):
#     resolved_path = os.path.abspath(os.path.join(os.getcwd(), path))
#     return resolved_path

#获取封装后的文件路径
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)
 
 
if __name__ == "__main__":
    sys.argv = [
        "streamlit",
        "run",
        resource_path(r"module\demo.py"),
        "--global.developmentMode=false",
    ]
    sys.exit(stcli.main())

# 相当于
# streamlit run demo.py

#打包

# 1.pyi-makespec --onefile --additional-hooks-dir=./hooks --paths 'D:\project\工具开发\streamlit' main.py run.py --clean

#修改spec文件

# 2.pyinstaller run.spec --clean

# pyarmor-7 pack -s "run.spec" run.py