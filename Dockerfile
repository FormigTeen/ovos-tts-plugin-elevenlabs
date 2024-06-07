FROM python:3.9-alpine

COPY . .

RUN pip3 -v install . \
    && rm -rf "${HOME}/.cache"

#ENTRYPOINT ["ovos-skill-launcher", "skill-ovos-wikipedia.openvoiceos"]
