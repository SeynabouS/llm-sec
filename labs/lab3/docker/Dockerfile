
FROM ubuntu:22.04
RUN apt-get update && apt-get install -y --no-install-recommends curl ca-certificates \
    && rm -rf /var/lib/apt/lists/*
RUN useradd -m appuser
RUN curl -sSLo /tmp/install.sh https://example.com/install.sh \
    && /bin/sh /tmp/install.sh
USER appuser
CMD ["bash"]
