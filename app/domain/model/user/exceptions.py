from domain.shared.exception import DomainError


class UserNotFoundError(DomainError):
    ...


class UserAlreadyExistError(DomainError):
    ...


class WrongPasswordError(DomainError):
    ...


class PasswordValidationError(DomainError):
    ...


class PhoneValidationError(DomainError):
    ...


class EmailValidationError(DomainError):
    ...
