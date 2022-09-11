from tortoise import fields, models

from core.enums import Status


class Table(models.Model):
    """
    抽象模型
    """

    id = fields.IntField(pk=True, description="主键")
    status = fields.IntEnumField(Status, description="状态", default=Status.ACTIVE)
    created = fields.DatetimeField(auto_now_add=True, description="创建时间", null=True)
    modified = fields.DatetimeField(auto_now=True, description="更新时间", null=True)

    class Meta:
        abstract = True
        ordering = ["-created"]
        indexes = ("status",)
