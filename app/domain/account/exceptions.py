from domain.shared.exception import DomainError


class AccountNotFoundError(DomainError):
    ...


class AccountIsAlreadyExistError(DomainError):
    ...


class WrongPasswordError(DomainError):
    ...


class WrongPhoneError(DomainError):
    ...
