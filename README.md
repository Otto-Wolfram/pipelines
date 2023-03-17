# Подготовка проекта
Перед началом работы необходимо запустить файл **prepare.bat**.

Или в корне проекта выполнить команду:
```commandline
poetry install
```

# Prefect
Для запуска проекта на Prefect необходимо запустить файл **run_prefect.bat**.

Или в корне проекта выполнить команду:
```commandline
poetry run prefect
```

# Dagster
Для запуска проекта на Dagster необходимо запустить файл **run_dagster.bat**.

Или в корне проекта выполнить команды:
```commandline
cd pipelines
poetry run dagit -f dagster_flow.py
```

