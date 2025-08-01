# mentorostudio

Proyecto base de Django preparado para producción usando Docker Compose y Nginx.

## Uso

```
docker compose up --build
```

El acceso a `http://localhost` mostrará la aplicación Django.
Tras iniciar sesión, la página de inicio incluye un iframe con
una instancia de [code-server](https://github.com/coder/code-server).
