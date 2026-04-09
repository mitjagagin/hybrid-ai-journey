import sys
import os

# Профессиональный способ проверить, где мы находимся
print("-" * 30)
print(f"Текущий интерпретатор: {sys.executable}")
print(f"Версия Python: {sys.version.split()}")
print("-" * 30)

# Проверяем, активна ли среда Conda
conda_env = os.environ.get('CONDA_DEFAULT_ENV')
if conda_env:
    print(f"Активная Conda-среда: {conda_env}")
else:
    print("Внимание: Среда Conda не обнаружена в переменных окружения!")
print("-" * 30)