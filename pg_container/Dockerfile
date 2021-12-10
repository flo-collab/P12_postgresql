FROM postgres:latest

ENV POSTGRES_PASSWORD=postgree
ENV POSTGRES_USER=postgres
ENV POSTGRES_DB=P12

EXPOSE 5432
COPY create_fixtures.sql /docker-entrypoint-initdb.d/create_fixtures.sql