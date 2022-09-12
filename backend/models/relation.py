from models.common import Table, fields


class RoleRelationMixin:
    rid = fields.IntField(description="角色id")


class UserRoleModel(Table, RoleRelationMixin):
    """用户角色关系表"""

    uid = fields.IntField(description="用户id")

    class Meta:
        table = "sys_user_role"
        indexes = ("uid", "rid")


class RoleMenuModel(Table, RoleRelationMixin):
    """角色菜单(权限)关系表"""

    mid = fields.IntField(description="菜单ID")

    class Meta:
        table = "sys_role_menu"
        indexes = ("mid", "rid")
