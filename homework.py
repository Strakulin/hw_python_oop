from dataclasses import asdict, dataclass
from typing import ClassVar

@dataclass
class InfoMessage:
    """Информационное сообщение о тренировке."""
    training_type: str
    duration: float
    distance: float
    speed: float
    calories: float
    MESSAGES: ClassVar[str]=('Тип тренировки: {training_type} \n'
                   'Длительность: {duration:.3f} ч.\n'
                   'Дистанция: {distance:.3f} км.\n'
                   'Ср. скорость: {speed:.3f} км/ч.\n'
                   'Потрачено ккал: {calories:.3f}.\n')

    def get_message(self) -> str:
        return self.MESSAGES.format(**asdict(self))


@dataclass
class Training:
    """Базовый класс тренировки."""
    LEN_STEP = 0.65
    M_IN_KM = 1000
    MIN_H = 60
    action: int
    duration: float
    weight: float

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        return self.action * self.LEN_STEP / self.M_IN_KM


    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        return self.get_distance() / self.duration


    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        pass

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        message = InfoMessage(self.__class__.__name__,
                              self.duration,
                              self.get_distance(),
                              self.get_mean_speed(),
                              self.get_spent_calories())
        return message


class Running(Training):
    """Тренировка: бег."""
    COEFF_CALORIE_1 = 18
    COEFF_CALORIE_2 = 20

    def get_spent_calories(self) -> float:
        return (self.COEFF_CALORIE_1 * self.get_mean_speed()
                    - self.COEFF_CALORIE_2) * self.weight / self.M_IN_KM \
            * (self.duration * 60)


@dataclass
class SportsWalking(Training):
    """"Тренировка: спортивная ходьба."""
    action: int
    duration: float
    weight: float
    height: float

    def get_spent_calories(self) -> float:
        return (0.035 * self.weight + (self.get_mean_speed() ** 2
                                           // self.height)
                    * 0.029 * self.weight) * (self.duration * self.MIN_H)


@dataclass
class Swimming(Training):
    """Тренировка: плавание."""
    LEN_STEP = 1.38
    COEFF_CALORIE_3 = 1.1
    COEFF_CALORIE_4 = 2
    action: int
    duration: float
    weight: float
    length_pool: float
    count_pool: float

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        return self.action * self.LEN_STEP / self.M_IN_KM

    def get_mean_speed(self) -> float:
        return self.length_pool * self.count_pool \
            / self.M_IN_KM / self.duration

    def get_spent_calories(self) -> float:
        return (self.get_mean_speed() + self.COEFF_CALORIE_3)\
            * self.COEFF_CALORIE_4* self.weight

def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    type_dict = {'SWM': Swimming,
                 'RUN': Running,
                 'WLK': SportsWalking}
    return type_dict[workout_type](*data)


def main(training: Training) -> None:
    """Главная функция."""

    print (training.show_training_info().get_message())



if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)