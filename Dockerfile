FROM python:3.10
ENV PYTHONUNBUFFERED=1
RUN mkdir /pipelinesApp
WORKDIR /pipelinesApp
RUN mkdir /pipelinesApp/pipelines
RUN mkdir /pipelinesApp/example_pipeline
COPY /pipelines /pipelinesApp/pipelines
COPY /example_pipeline /pipelinesApp/example_pipeline
COPY setup.py /pipelinesApp
COPY poetry.lock /pipelinesApp
COPY README.md /pipelinesApp
COPY ex_script.sh /pipelinesApp
COPY pyproject.toml /pipelinesApp
RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install
ENTRYPOINT [ "bash", "/pipelinesApp/ex_script.sh" ]