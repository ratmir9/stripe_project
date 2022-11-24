### Запуск проекта с помощью Docker.
1. **Так, как в проекте происходит интеграция с платежной системной Stripe. Необходимо получить SECRET_KEY и PUBLIC_KEY. Их можно получить** [здесь](https://dashboard.stripe.com/test/apikeys)

1. **Создайте файл `.env` для конфигурирования проекта.**
```
touch .env
```
2. **Откройте файл `.env` и заполните следующими данными.**
```
SECRET_KEY=your_secret_key
STRIPE_SECRET_KEY=your_stripe_secret_key
STRIPE_PUBLIC_KEY=your_stripe_public_key
```
3. **Для запуска необходимо выполните следующую команду.**
```
sudo docker-compose up -d 
```
