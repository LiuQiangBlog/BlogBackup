import os

def git_operation():
    '''
    git 命令行函数，将仓库提交
    
    ----------
    需要安装git命令行工具，并且添加到环境变量中
    '''
    os.system('git init')
    os.system('git add --all')
    os.system('git commit -m "add photos"')
    os.system('git remote add origin git@github.com:LiuQiangBlog/BlogBackup.git')
    os.system('git push -u origin master')


if __name__ == "__main__":
    git_operation()    # 提交到github仓库
