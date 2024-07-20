# Microservicio con api GraphQL & Flask

## Ejecutar el proyecto

Para ejecutar el proyecto, es necesario tener instalado `docker`.

```bash
docker build -t ms_graphql_flask .
docker run -p 5002:5000 ms_graphql_flask
```

## Consultar la API

Para consultar la API, se puede acceder a `http://localhost:5002/graphql`.

## Ejemplo de consulta

### Listar
```graphql
{
  shoppicarts {
    id
    name
    quantity
  }
}
```

### Crear
```graphql
mutation {
  createCart(name: "Arroz", price: 15, quantity: 3) {
    id
    name
    price
    quantity
  }
}
```

### Actualizar
```graphql
mutation {
  updateCart(cartId: 1, name: "Arroz Integral", price: 20, quantity: 5) {
    id
    name
    price
    quantity
    lastUpdate
  }
}
```

### Eliminar
```graphql
mutation {
  deleteCart(cartId: 1)
}
```
