FROM nginx:stable-alpine

#----------------------------------------------------------------------------------------------------------------------
# Create Users / Groups 
#----------------------------------------------------------------------------------------------------------------------

# Set the user to the www-data user
ARG APP_USER=www-data
ARG AUX_GROUP=chaz
RUN addgroup -g 69 ${AUX_GROUP} && \
  adduser --ingroup ${APP_USER} -u 69 -D --no-create-home ${APP_USER} && \
  adduser nginx ${AUX_GROUP}

# --------------------------------------------------------
# NGINX CONFIG SETUP
# --------------------------------------------------------
# Remove the stock nginx config - It just want meant to be
RUN rm /etc/nginx/conf.d/default.conf
# Add our AIO Nginx config
COPY nginx.conf /etc/nginx/conf.d/default.conf

RUN apk add bash openssl

# --------------------------------------------------------
# NGINX TLS SETUP
# --------------------------------------------------------
# Generate SnakeOil TLS for transit
RUN mkdir /etc/nginx/ssl && \
  openssl req -x509 -nodes -days 365 \
 -subj "/C=US/ST=CO/O=skynet/CN=chaz.am.io" \
 -addext "subjectAltName=DNS:chaz" \
 -newkey rsa:4096 \
 -keyout /etc/nginx/ssl/cert.key \
 -out /etc/nginx/ssl/cert.crt; 

# --------------------------------------------------------
# NGINX LOGS SETUP
# --------------------------------------------------------
# Forward logs to stdout
RUN ln -sf /dev/stdout /var/log/nginx/access.log \
    && ln -sf /dev/stderr /var/log/nginx/error.log

#---------------------------------------------------------
# Harden the container - remove all root execution
#---------------------------------------------------------

# Fix them permissions so those l337 hackers cant b naughty and Nginx is happy
RUN touch /var/run/nginx.pid && \
  chown -R ${APP_USER} /var/run/nginx.pid && \
  chown -R ${APP_USER} /etc/nginx/ && \
  chown -R ${APP_USER} /var/log/nginx/ && \
  chown -R nginx:${EXTRA_GROUP} /var/cache/nginx/ && \
  chown -R ${APP_USER} /etc/nginx/ssl  && \
  chmod -R 740 /var/log/nginx/ && \
  chmod -R 740 /var/cache/nginx/ && \
  chmod 744 /var/run/nginx.pid && \
  chmod -R 540 /etc/nginx/ && \
  chmod -R 540 /etc/nginx/ssl && \
  mkdir -p /code/static && \
  chmod -R 774 /code/static
  
# Change to a non-root user - Beacuse well duh
# USER ${APP_USER}:${APP_USER}

# --------------------------------------------------------
# CONTAINER SETUP STUFFz
# --------------------------------------------------------

# Expose HTTP/HTTPS
EXPOSE 80
EXPOSE 443

VOLUME /code/static

# Make sure we kill Nginx with no mercy
STOPSIGNAL SIGTERM

# Tell that webserver to not fork off - We need him ;P
CMD ["nginx", "-g", "daemon off;"]
