from pydantic import BaseModel, ConfigDict


class BaseSchema(BaseModel):
    """
    frozen for immutability
    extra garanty that fields wont be added
    """

    model_config = ConfigDict(frozen=True, extra="forbid")
