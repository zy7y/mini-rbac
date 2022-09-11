from core.enums import MenuType
from core.table import Table, fields


class MenuModel(Table):
    """
    菜单表
    """

    name = fields.CharField(max_length=20, description="名称", null=True)
    meta = fields.JSONField(description="元数据信息", null=True)
    path = fields.CharField(max_length=128, description="菜单url", null=True)
    type = fields.IntEnumField(MenuType, description="菜单类型")
    component = fields.CharField(max_length=128, description="组件地址", null=True)
    pid = fields.IntField(description="父id", null=True)
    identifier = fields.CharField(max_length=30, description="权限标识 user:add", null=True)
    api = fields.CharField(max_length=128, description="接口地址", null=True)
    method = fields.CharField(max_length=10, description="接口请求方式", null=True)
    regx = fields.CharField(max_length=50, description="接口地址正则表达式", null=True)

    class Meta:
        table = "sys_menu"
        table_description = "菜单表"
        # 非唯一的索引
        indexes = ("type", "name")
