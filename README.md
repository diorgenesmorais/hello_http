# hello http

> Testando uma function localmente e depois fazer o deploy no GCP

- Criar o ambiente virtual
```sh
python -m venv env
```

- Ativar o ambiente (após ativar o ambiente, verá o nome do ambiente entre parênteses no início da linha de comando)
```sh
source env/bin/activate
```

- Desativar o ambiente
```sh
deactivate
```

- Registrar as dependências do projeto
```sh
pip freeze > requirements.txt
```

- Instalar as dependências
```sh
pip install -r requirements.txt
```

- Criar gitignore
```sh
npx gitignore python
```

- Fazer o deploy no GCP
```sh
gcloud functions deploy fn-hello-http \
  --gen2 \
  --service-account=minha-conta@dev.gserviceaccount.com \
  --runtime=python311 \
  --region=us-central1 \
  --source=. \
  --entry-point=hello-http \
  --trigger-http \
```

###### Authors

[**Diorgenes Morais**](https://github.com/diorgenesmorais)

