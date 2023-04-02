import uuid

from tortoise.models import Model
from tortoise import fields


class BaseModel(Model):
    id = fields.IntField(pk=True)
    gid = fields.UUIDField(null=False, default=uuid.uuid4)

    class Meta:
        abstract = True


class BaseAuditModel(BaseModel):
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        abstract = True
