from models.common import Table, fields


class RoleModel(Table):
    """
    角色表
    """

    name = fields.CharField(max_length=20, description="角色名称")
    remark = fields.CharField(max_length=200, description="角色描述")

    class Meta:
        table = "sys_role"
        table_description = "角色表"
