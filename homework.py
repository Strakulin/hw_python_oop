class InfoMessage:
    """Информационное сообщение о тренировке."""
    # получаемые парам
    def __init__(self,
                 training_type,
                 duration,
                 distance,
                 avg_speed,
                 colories
                 ):
        self.training_type = training_type
        self.duration = duration
        self.distance = distance
        self.avg_speed = avg_speed
        self.colories = colories

    def get_message(self):
        return (f'Тип тренировки: {self.training_type}; Длительность: {self.duration} ч.;'
                   f'Дистанция: {self.distance:.3f} км;'
                   f'Ср. скорость: {self.avg_speed:.3f} км/ч;'
                   f'Потрачено к/кал: {self.colories:.3f}.')


class Training:
    """Базовый класс тренировки."""
    LEN_STEP = 0.65
    M_IN_KM = 1000
    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 ) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        distance = self.action * self.LEN_STEP / self.M_IN_KM
        return distance

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        avg_speed = self.get_distance() / self.duration
        return avg_speed

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        pass

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        return InfoMessage


class Running(Training):
    """Тренировка: бег."""
    coeff_calorie_1 = 18
    coeff_calorie_2 = 20

    def get_spent_calories(self) -> float:
        colories = (self.coeff_calorie_1 * self.get.mean_speed.avg_speed- self.coeff_calorie_2) / self.M_IN_KM * self.duration
        return colories


class SportsWalking(Training):
    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 height: float
                 ) -> None:
        super().__init__(action,duration,weight)
        self.height = height

    """Тренировка: спортивная ходьба."""

    pass


class Swimming(Training):
    """Тренировка: плавание."""
    pass


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    if workout_type == 'SWM':
        tupe_tren = Swimming(*data)
    elif workout_type == 'RUN':
        tupe_tren = Running(*data)
    elif workout_type == 'WLK':
        tupe_tren = SportsWalking(*data)
    return tupe_tren



def main(training: Training) -> None:
    """Главная функция."""
    info = training.show_training_info()
    print(info.get_message())
    return


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)


