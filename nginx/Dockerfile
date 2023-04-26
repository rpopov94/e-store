FROM nginx:1.21-alpine

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d
RUN openssl req -x509 -newkey rsa:4096 -nodes -keyout server.key -out server.crt -days 365
RUN sudo mkdir -p /etc/nginx/certs/
RUN sudo mv server.crt /etc/nginx/certs/
RUN sudo mv server.key /etc/nginx/certs/
