from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


class RunConfig(BaseModel):
    host: str = "127.0.0.1"
    port: int = 8000


class DatetimeConfig(BaseModel):
    value: str = "%Y-%m-%d %H:%M:%S"


class AccessToken(BaseModel):
    lifetime_seconds: int = 3600


class AuthenticationPrefix(BaseModel):
    auth: str = "/auth"
    login: str = "/login"


class Authentication(BaseModel):
    reset_password_token_secret: str
    verification_token_secret: str


class Reservation(BaseModel):
    hours_before_start: int = 6
    hours_expires_at: int = 1


class ReservationPrefix(BaseModel):
    reservation_prefix: str = "/create"
    confirm_reservation_prefix: str = "/confirm/{id}"


class ApiPrefix(BaseModel):
    """
    Prefix to main api router, path: app.api.main_router
    """

    prefix: str = "/api"
    auth: AuthenticationPrefix = AuthenticationPrefix()

    @property
    def bearer_token_transport(self) -> str:
        parts = (self.prefix, self.auth.auth, self.auth.login)
        path = "".join(parts)
        return path[1:]


class DatabaseConfig(BaseModel):
    hostname: str
    port: str
    password: str
    name: str
    username: str

    naming_convention: dict[str, str] = {
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_N_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s",
    }


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        env_nested_delimiter="__",
    )

    run: RunConfig = RunConfig()
    api: ApiPrefix = ApiPrefix()
    db: DatabaseConfig
    dt: DatetimeConfig = DatetimeConfig()
    access_token: AccessToken = AccessToken()
    authentication: Authentication
    reservation_time: Reservation = Reservation()
    reservation_prefix: ReservationPrefix = ReservationPrefix()


settings = Settings()
