# mentorostudio

Proyecto base de Django preparado para producción usando Docker Compose y Nginx.

## Uso

```
docker compose up --build
```

El acceso a `http://localhost` mostrará la aplicación Django. Solo los usuarios
registrados podrán acceder a la ruta `/code-server/`, que muestra una instancia
de [code-server](https://github.com/coder/code-server) dentro de un iframe.