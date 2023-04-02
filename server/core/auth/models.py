from tortoise import fields


from server.common.database.base import BaseAuditModel


class User(BaseAuditModel):
    first_name = fields.CharField(max_length=128, null=True)
    last_name = fields.CharField(max_length=128, null=False)
    email = fields.CharField(max_length=128, unique=True, index=True, null=False)
    password = fields.CharField(max_length=128, null=False)
    is_active = fields.BooleanField(default=False)
    last_login = fields.DatetimeField(timezone=True, null=True)
