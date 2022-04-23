class InfoMessage:
    """Информационное сообщение о тренировке."""

#0  message = print(f'Информация')
#   return message


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
        distance = training.action * Training.LEN_STEP / Training.M_IN_KM
        return distance


    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        av_speed = training.get.distance / time_training
        return av_speed


    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        pass

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        return InfoMessage.message


class Running(Training):
    """Тренировка: бег."""
    coeff_calorie_1 = 18
    coeff_calorie_2 = 20
    def run (self, action , duration , weight ):
        super().__init__(action,duration,weight)
    def get_spent_calories(self) -> float:
        return (Running.coeff_calorie_1 * training.get_mean_speed() - Running.coeff_calorie_2) / Training.M_IN_KM * time_training



class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    def wall (self, action , duration , weight, height):
        super().__init__(action,duration,weight)
    pass


class Swimming(Training):
    """Тренировка: плавание."""
    pass


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""

    pass


def main(training: Training) -> None:
    """Главная функция."""

    pass


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)

Training(13,45,34)

