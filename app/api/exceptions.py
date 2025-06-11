class ReservationErrors(Exception):
    """Ошибки в процессе бронирования билетов"""

    def __init__(self, message: str = "Ошибка получена в процессе бронировании билета"):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return self.message


class SeatNotFoundError(ReservationErrors):
    def __init__(self, row=None, column=None):
        message = f"Место в {row} ряду и {column} столбце не найдено!"

        super().__init__(message)
        self.row = row
        self.column = column

    def __str__(self):
        return self.message


class TicketAlreadyBooked(ReservationErrors):
    def __init__(self, row=None, column=None):
        message = f"Место в {row} ряду и {column} столбце уже забронировано!"
        super().__init__(message)
        self.row = row
        self.column = column

    def __str__(self):
        return self.message


class TimeForBookingIsOver(ReservationErrors):
    def __init__(self):
        message = "До сеанса осталось менее 6-ти часов, бронирование невозможно!"
        super().__init__(message)

    def __str__(self):
        return self.message


class ReservationNotFoundError(ReservationErrors):
    def __init__(self):
        message = "Бронирование не найдено"
        super().__init__(message)

    def __str__(self):
        return self.message


class ReservationUnavailable(ReservationErrors):
    def __init__(self):
        message = "Эта бронь вам недоступна!"
        super().__init__(message)

    def __str__(self):
        return self.message


class TimeToReservationalExpired(ReservationErrors):
    def __init__(self):
        message = f"Забронировать билет на данный сеанс больше нельзя"
        super().__init__(message)

    def __str__(self):
        return self.message


class TimeOutReservation(ReservationErrors):
    def __init__(self):
        message = f"В данный момент кто-то уже бронирует билет на это место!"
        super().__init__(message)

    def __str__(self):
        return self.message
