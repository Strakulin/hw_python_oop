from dataclasses import asdict, dataclass
from typing import ClassVar, Dict, List, Type


@dataclass
class InfoMessage:
    """Информационное сообщение о тренировке."""
    training_type: str
    duration: float
    distance: float
    speed: float
    calories: float
    MESSAGES: ClassVar[str] = (
        'Тип тренировки: {training_type};'
        ' Длительность: {duration:.3f} ч.;'
        ' Дистанция: {distance:.3f} км;'
        ' Ср. скорость: {speed:.3f} км/ч;'
        ' Потрачено ккал: {calories:.3f}.'
    )

    def get_message(self) -> str:
        return self.MESSAGES.format(**asdict(self))


@dataclass
class Training:
    """Базовый класс тренировки."""
    action: int
    duration: float
    weight: float
    LEN_STEP: ClassVar[float] = 0.65
    M_IN_KM: ClassVar[float] = 1000
    MIN_H: ClassVar[float] = 60

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        return self.action * self.LEN_STEP / self.M_IN_KM

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        return self.get_distance() / self.duration

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        raise NotImplementedError('Ошибка метод обьявлен в дочерних классах')

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        return InfoMessage(
            self.__class__.__name__,
            self.duration,
            self.get_distance(),
            self.get_mean_speed(),
            self.get_spent_calories()
        )


class Running(Training):
    """Тренировка: бег."""
    COEFF_CALORIE_1: ClassVar[float] = 18
    COEFF_CALORIE_2: ClassVar[float] = 20

    def get_spent_calories(self) -> float:
        return ((self.COEFF_CALORIE_1 * self.get_mean_speed()
                - self.COEFF_CALORIE_2)
                * self.weight / self.M_IN_KM
                * (self.duration * self.MIN_H))


@dataclass
class SportsWalking(Training):
    """"Тренировка: спортивная ходьба."""
    action: int
    duration: float
    weight: float
    height: float
    COEFF_CALORIE_5: ClassVar[float] = 0.035
    COEFF_CALORIE_6: ClassVar[float] = 0.029

    def get_spent_calories(self) -> float:
        return ((self.COEFF_CALORIE_5 * self.weight
                + (self.get_mean_speed() ** 2 // self.height)
                * self.COEFF_CALORIE_6 * self.weight)
                * (self.duration * self.MIN_H))


@dataclass
class Swimming(Training):
    """Тренировка: плавание."""
    LEN_STEP: ClassVar[float] = 1.38
    COEFF_CALORIE_3: ClassVar[float] = 1.1
    COEFF_CALORIE_4: ClassVar[float] = 2
    action: int
    duration: float
    weight: float
    length_pool: float
    count_pool: float

    def get_mean_speed(self) -> float:
        return (self.length_pool
                * self.count_pool
                / self.M_IN_KM
                / self.duration)

    def get_spent_calories(self) -> float:
        return ((self.get_mean_speed() + self.COEFF_CALORIE_3)
                * self.COEFF_CALORIE_4 * self.weight)


def read_package(workout_type: str, data: List[int]) -> Training:
    """Прочитать данные полученные от датчиков."""
    sensors: Dict[str, Type[Training]] = {
        'SWM': Swimming,
        'RUN': Running,
        'WLK': SportsWalking
    }
    if workout_type not in sensors:
        raise KeyError(f'Ошибка ключа {workout_type}')
    return sensors[workout_type](*data)


def main(training: Training) -> None:
    """Главная функция."""
    print(training.show_training_info().get_message())


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)