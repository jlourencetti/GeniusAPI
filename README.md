# GeniusFlaskAPI


                                                                                              


> INTERAÇÃO COM API DO GENIUS PARA CAPTURAR AS 10 MÚSICAS MAIS POPULARES DE UM ARTISTA.



## Requisitos

- Python 3+
- Conta Genius API
- Redis Server
- DynamoDB

## Como fazer a consulta

- Fazer um requisição GET para a URL:
```
http://127.0.0.1:5000/artist/u2
```

- Se funcionar corretamente, o retorno será:
```
{
    "U2": [
        "One",
        "With or Without You",
        "I Still Haven’t Found What I’m Looking For",
        "Sunday Bloody Sunday",
        "Pride (In the Name of Love)",
        "Beautiful Day",
        "Get Out of Your Own Way",
        "Where the Streets Have No Name",
        "Every Breaking Wave",
        "Song for Someone"
    ]
}

```

