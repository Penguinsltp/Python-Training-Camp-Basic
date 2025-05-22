"""
练习: 列表操作

描述：
实现对学生列表的添加、删除和修改操作。

请补全下面的函数，对学生列表进行各种操作。
"""

def student_list_operations(students, operation, *args):
    """
    对学生列表进行操作
    
    参数:
    - students: 学生列表
    - operation: 操作类型 ("add", "remove", "update")
    - args: 操作所需的额外参数
    
    返回:
    - 操作后的学生列表
    """
    if operation == "add":
        # args[0] 是要添加的学生姓名
        if args:
            students.append(args[0].strip())  # 去除前后空格
    elif operation == "remove":
        if args:
            name = args[0].strip()
            if name in students:
                students.remove(name)
    elif operation == "update":
        if len(args) >= 2:
            old_name = args[0].strip()
            new_name = args[1].strip()
            if old_name in students:
                index = students.index(old_name)
                students[index] = new_name
    return students
