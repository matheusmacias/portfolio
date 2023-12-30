#!/bin/sh

certbot_dir="/etc/letsencrypt/live/matheusmacias.com.br"
fullchain_file="$certbot_dir/fullchain.pem"
privkey_file="$certbot_dir/privkey.pem"

if [ ! -f "$fullchain_file" ] || [ ! -f "$privkey_file" ]; then
    echo "Certificados não encontrados. Executando Certbot para obter certificados SSL."

    apk update
    apk add --no-cache certbot certbot-nginx

    email="matheusmacias3@gmail.com"
    domains="www.matheusmacias.com.br,matheusmacias.com.br"

    certbot --nginx --non-interactive --agree-tos -m "$email" --domains "$domains"
else
    echo "Certificados já existem. Nenhuma ação necessária."
fi
