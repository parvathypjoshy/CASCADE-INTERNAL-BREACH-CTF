FROM python:3.9

WORKDIR /app
COPY . .

RUN pip install flask

# Install sudo as root FIRST
RUN apt update && apt install -y sudo

# Create low privilege user
RUN useradd -m ctf

# Privilege escalation vector
RUN echo "ctf ALL=(ALL) NOPASSWD: /usr/bin/tar" >> /etc/sudoers

# Create directories
RUN mkdir -p /home/ctf /root /opt/backups /var/log/app

# ----------------------------
# FLAGS (clean structured)
# ----------------------------

# flag 4 → after RCE
RUN echo "FLAG{user_shell_obtained}" > /home/ctf/user.txt

# flag 5 → after privesc
RUN echo "FLAG{root_dominion}" > /root/root.txt

# hidden flag (optional bonus)
RUN echo "FLAG{internal_service_leak}" > /opt/.hidden_flag

# permissions
RUN chown -R ctf:ctf /home/ctf
RUN chmod 600 /root/root.txt

# switch to low user
USER ctf

CMD ["python", "app.py"]
