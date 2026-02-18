# Database Documentation

## SQLite Configuration

Configured in `app.py` inside `create_app()`.

| Setting | Value |
|---|---|
| URI | `sqlite:///<basedir>/income_tracker.db` |
| File location | `income_tracker/income_tracker.db` |
| Track modifications | `False` |
| Connection management | Flask-SQLAlchemy (SQLAlchemy connection pool) |
| Table creation | `db.create_all()` on app startup — no migration tool |

The `SECRET_KEY` defaults to `"dev-secret-change-in-production"` unless overridden by the `SECRET_KEY` environment variable.

---

## Schema

Defined as SQLAlchemy ORM models in `models.py`. No separate SQL schema file exists.

### `users`

| Column | Type | Constraints |
|---|---|---|
| `id` | INTEGER | PRIMARY KEY |
| `username` | VARCHAR(80) | UNIQUE, NOT NULL |
| `password_hash` | VARCHAR(256) | NOT NULL |

### `journal_entries`

| Column | Type | Constraints |
|---|---|---|
| `id` | INTEGER | PRIMARY KEY |
| `user_id` | INTEGER | NOT NULL, FOREIGN KEY → `users.id` |
| `date` | DATE | NOT NULL |
| `expenses` | FLOAT | DEFAULT 0.0 |
| `income` | FLOAT | DEFAULT 0.0 |
| `withdrawals` | FLOAT | DEFAULT 0.0 |
| `notes` | TEXT | nullable |

**Unique constraint:** `(user_id, date)` — one entry per user per day (`uq_user_date`).

---

## Relationships

```
users (1) ──< journal_entries (many)
  via journal_entries.user_id → users.id
```
