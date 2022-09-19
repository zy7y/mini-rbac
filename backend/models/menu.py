from models.common import Table, fields


class MenuModel(Table):
    """
    菜单表
    """

    name = fields.CharField(max_length=20, description="名称", null=True)
    icon = fields.CharField(max_length=100, description="菜单图标", null=True)
    path = fields.CharField(max_length=128, description="菜单url", null=True)
    type = fields.SmallIntField(description="菜单类型 0目录 1组件 2按钮 3数据")
    component = fields.CharField(max_length=128, description="组件地址", null=True)
    pid = fields.IntField(description="父id", null=True)
    identifier = fields.CharField(max_length=30, description="权限标识 user:add", null=True)
    api = fields.CharField(max_length=128, description="接口地址", null=True)
    method = fields.CharField(max_length=10, description="接口请求方式", null=True)

    class Meta:
        table = "sys_menu"
        table_description = "菜单表"
        # 非唯一的索引
        indexes = ("type", "name")
