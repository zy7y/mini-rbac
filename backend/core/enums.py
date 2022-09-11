import enum


class Status(enum.IntEnum):
    """
    数据库状态枚举值
    9 删除 5 无效 1 有效 3 使用
    """

    DELETED: int = 9
    INACTIVE: int = 5
    ACTIVE: int = 1
    SELECTED: int = 3


class UserType(enum.IntEnum):
    """
    数据库超级管理员枚举
    0 超级管理员 1用户
    """

    ADMIN: int = 0
    USER: int = 1


class MenuType(enum.IntEnum):
    """
    菜单类型枚举
    目录 0
    组件 1 按钮 2
    """

    DIR = 0
    CPN = 1
    BTN = 2
