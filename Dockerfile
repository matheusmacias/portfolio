FROM alpine:latest

RUN apk update && apk add --no-cache zsh git python3 py3-pip tzdata pkgconfig
# Add PostgreSQL dependencies
RUN apk add --no-cache postgresql-dev gcc musl-dev python3-dev libffi-dev openssl-dev

SHELL ["/bin/zsh", "-c"]

RUN sh -c "$(wget -O- https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

RUN ln -fs /usr/share/zoneinfo/America/Belem /etc/localtime
RUN echo "America/Belem" > /etc/timezone

WORKDIR /app

COPY requirements.txt .
# Install psycopg2-binary instead of psycopg2 for PostgreSQL
RUN pip install --break-system-packages -r requirements.txt

COPY . .

EXPOSE 8000
