# F1-API 🏎️ (FAETERJ • PAV)

Trabalho da disciplina **Programação em Ambiente Visual (PAV)** – FAETERJ.

API RESTful em **Flask 3** + **PostgreSQL** que gerencia o universo da Fórmula 1:

* Temporadas, equipes, pilotos, circuitos, corridas, contratos e resultados
* 10 requisitos funcionais garantidos via constraints SQL + regras de serviço
* Seed opcional com temporada 2024 e GP do Bahrain (dados reais)

---

## Cronograma das entregas

| Fase | Conteúdo | Tag Git | Data de entrega |
|------|----------|---------|-----------------|
| **Parte 1** | **Definição de requisitos** (10 regras funcionais) | `part1` | 12-abr-2025 ✅ |
| **Parte 2** | **Modelagem de banco**, repositórios CRUD e seed com dados reais | `part2` | 23-mai-2025 ✅ |
| **Parte 3** | Services, validações de negócio e controllers REST | `part3` | 6-jun-2025 ✅ |
| **Parte 4** | Implementação de um jupyter notebook | `part4` | 12-jun-2025 ✅ |

---

## Índice
1. [Requisitos](#requisitos)
2. [Instalação rápida](#instalação-rápida)
3. [Estrutura do projeto](#estrutura-do-projeto)
4. [Endpoints principais](#endpoints-principais)
5. [Seed de dados](#seed-de-dados)
6. [Regras de negócio implementadas](#regras-de-negócio-implementadas)
7. [Contribuindo](#contribuindo)
8. [Licença](#licença)

---

## Requisitos
| Software   | Versão mínima |
|------------|---------------|
| Python     | **3.12**      |
| PostgreSQL | 12+           |

---

## Instalação rápida

```bash
git clone https://github.com/brenojm/f1-api.git
cd f1-api

python -m venv venv
# Windows PowerShell → .\venv\Scripts\Activate.ps1
# macOS / Linux     → source venv/bin/activate

pip install -r requirements.txt           # Flask, Flask-RESTful, Flask-SQLAlchemy, flask-apispec, marshmallow

# String de conexão (ou edite src/__init__.py)
export DATABASE_URL="postgresql+psycopg://postgres:secret@localhost:5432/f1db"

# Executar (cria tabelas + seed se vazio)
python manage.py
