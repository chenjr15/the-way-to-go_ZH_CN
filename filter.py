'''用于去除页面中本来自带的上一节下一节链接， 因为vuepress自带这些链接
'''
from typing import List

def get_filters(kws: List[str]):
    '''
    返回一个filter，对以kws中的关键词开头的字符串返回True
    '''
    def starts_with_any(s: str, kws: List[str]) -> bool:
        return s and any((True for kw in kws if s.startswith(kw)))
    return starts_with_any


def filter_kws(filename, filter_func, dont_write=False):
    '''
    将指定的文件中符合指定滤函数的行过滤掉
    '''
    print(filename)
    lines = None
    with open(filename) as f:
        lines = f.readlines()
    filted_lines = [line for line in lines if not filter_func(line, kws)]
    diff = len(lines) - len(filted_lines)
    print(f"filtered {diff} lines ")
    if dont_write:
        return
    with open(filename, "w") as f:
        f.writelines(filted_lines)


if __name__ == "__main__":
    kws = ("## 链接", "- [目录]", "- 上一章", "- 下一节", "- 上一节",
           "- 上一部分", "- 下一节", "- 下一章", "- 下一部分")
    filter = get_filters(kws=kws)
    import os
    dir_name = "eBook"
    files = os.listdir(dir_name)
    for filename in files:
        if not filename.endswith(".md"):
            continue
        filter_kws(os.path.join(dir_name, filename), filter)
